import json
import time
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.views.decorators.http import require_POST
from django.utils import timezone

from .models import Category, SubCategory, FoodItem, Order, OrderItem, Review
from .forms import FoodItemForm, CheckoutForm, ReviewForm, LoginForm, RegisterForm

# Helper decorator
def staff_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

# User-facing views
def home(request):
    categories = Category.objects.all().order_by('display_order')
    featured_items = FoodItem.objects.filter(is_available=True).order_by('-rating')[:8]
    recent_reviews = Review.objects.all().order_by('-created_at')[:5]
    return render(request, 'store/home.html', {
        'categories': categories,
        'featured_items': featured_items,
        'recent_reviews': recent_reviews
    })

def menu(request):
    categories = Category.objects.all().order_by('display_order')
    subcategories = SubCategory.objects.all().order_by('display_order')
    
    food_items = FoodItem.objects.filter(is_available=True)
    
    category_slug = request.GET.get('category')
    if category_slug:
        food_items = food_items.filter(category__slug=category_slug)
        
    subcategory_slug = request.GET.get('subcategory')
    if subcategory_slug:
        food_items = food_items.filter(subcategory__slug=subcategory_slug)
        
    query = request.GET.get('q')
    if query:
        food_items = food_items.filter(name__icontains=query)
        
    return render(request, 'store/menu.html', {
        'categories': categories,
        'subcategories': subcategories,
        'food_items': food_items,
    })

@login_required
def cart_page(request):
    return render(request, 'store/cart.html')

@login_required
def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cart_data_str = request.POST.get('cart_data', '[]')
            try:
                cart_items = json.loads(cart_data_str)
            except json.JSONDecodeError:
                cart_items = []
                
            if not cart_items:
                return redirect('cart')
                
            order_number = f"MGR{int(time.time())}"
            total_amount = sum(float(item['price']) * item['quantity'] for item in cart_items)
            
            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                order_number=order_number,
                customer_name=form.cleaned_data['customer_name'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                pincode=form.cleaned_data['pincode'],
                total_amount=total_amount,
                payment_method=form.cleaned_data['payment_method'],
                special_instructions=form.cleaned_data['special_instructions']
            )
            
            for item in cart_items:
                food_item = FoodItem.objects.filter(id=item.get('id')).first()
                OrderItem.objects.create(
                    order=order,
                    food_item=food_item,
                    food_name=item.get('name', 'Unknown'),
                    quantity=item.get('quantity', 1),
                    price=item.get('price', 0)
                )
                
            return redirect('order_success', order_number=order_number)
    else:
        form = CheckoutForm()
        
    return render(request, 'store/checkout.html', {'form': form})

def order_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    review_form = ReviewForm()
    return render(request, 'store/order_success.html', {
        'order': order,
        'review_form': review_form
    })

def order_status(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    
    # Auto-simulate status progression over 5 minutes (300 seconds)
    if order.order_status not in ['delivered', 'cancelled']:
        elapsed = timezone.now() - order.created_at
        seconds = elapsed.total_seconds()
        
        new_status = 'pending'
        if seconds >= 300:        # 5 minutes
            new_status = 'delivered'
        elif seconds >= 180:      # 3 minutes
            new_status = 'out_for_delivery'
        elif seconds >= 100:      # 1.6 minutes
            new_status = 'preparing'
        elif seconds >= 30:       # 30 seconds
            new_status = 'confirmed'
            
        status_order = {
            'pending': 0,
            'confirmed': 1,
            'preparing': 2,
            'out_for_delivery': 3,
            'delivered': 4
        }
        
        current_rank = status_order.get(order.order_status, 0)
        new_rank = status_order.get(new_status, 0)
        
        if new_rank > current_rank:
            order.order_status = new_status
            order.save()
            
    return render(request, 'store/order_status.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/order_history.html', {'orders': orders})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                return render(request, 'store/login.html', {'form': form, 'error': 'Invalid username or password. Please try again.'})
    else:
        form = LoginForm()
    return render(request, 'store/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'store/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')


# API views
def api_menu_items(request):
    items = FoodItem.objects.filter(is_available=True)
    
    category_slug = request.GET.get('category')
    if category_slug:
        items = items.filter(category__slug=category_slug)
        
    data = [{
        'id': item.id,
        'name': item.name,
        'description': item.description,
        'price': str(item.price),
        'image': item.image,
        'is_veg': item.is_veg,
        'category': item.category.name if item.category else None
    } for item in items]
    return JsonResponse({'items': data})

@require_POST
@login_required
def api_submit_review(request):
    try:
        data = json.loads(request.body)
        order_id = data.get('order_id')
        rating = data.get('rating', 5)
        comment = data.get('comment', '')
        
        order = get_object_or_404(Order, id=order_id, user=request.user)
        Review.objects.create(
            user=request.user,
            order=order,
            rating=rating,
            comment=comment
        )
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@require_POST
@staff_required
def api_update_order_status(request, order_id):
    try:
        data = json.loads(request.body)
        status = data.get('status')
        order = get_object_or_404(Order, id=order_id)
        if status in dict(Order.STATUS_CHOICES):
            order.order_status = status
            order.save()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'message': 'Invalid status'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


# Admin views
@staff_required
def admin_dashboard(request):
    total_orders = Order.objects.count()
    total_revenue = Order.objects.filter(order_status='delivered').aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    pending_orders = Order.objects.filter(order_status='pending').count()
    total_users = Order.objects.values('email').distinct().count() # rough estimate of customers
    
    recent_orders = Order.objects.order_by('-created_at')[:10]
    recent_reviews = Review.objects.order_by('-created_at')[:5]
    
    return render(request, 'store/admin/dashboard.html', {
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'pending_orders': pending_orders,
        'total_users': total_users,
        'recent_orders': recent_orders,
        'recent_reviews': recent_reviews
    })

@staff_required
def admin_food_list(request):
    items = FoodItem.objects.all().order_by('-created_at')
    return render(request, 'store/admin/food_list.html', {'items': items})

@staff_required
def admin_food_add(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_food_list')
    else:
        form = FoodItemForm()
    return render(request, 'store/admin/food_form.html', {'form': form})

@staff_required
def admin_food_edit(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    if request.method == 'POST':
        form = FoodItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('admin_food_list')
    else:
        form = FoodItemForm(instance=item)
    return render(request, 'store/admin/food_form.html', {'form': form})

@staff_required
@require_POST
def admin_food_delete(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    item.delete()
    return redirect('admin_food_list')

@staff_required
def admin_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'store/admin/orders.html', {'orders': orders})

@staff_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in dict(Order.STATUS_CHOICES):
            order.order_status = status
            if status == 'delivered':
                order.payment_status = True
            order.save()
            return redirect('admin_order_detail', order_id=order.id)
            
    subtotal = sum(item.subtotal for item in order.items.all())
    delivery = order.total_amount - subtotal
    return render(request, 'store/admin/order_detail.html', {
        'order': order,
        'subtotal': subtotal,
        'delivery': delivery
    })

@staff_required
def admin_reviews(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'store/admin/reviews.html', {'reviews': reviews})
