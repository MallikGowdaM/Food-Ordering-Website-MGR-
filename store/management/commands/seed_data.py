from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Category, SubCategory, FoodItem
import random

class Command(BaseCommand):
    help = 'Seeds the database with categories, subcategories, and food items'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating superuser...')
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@mgr.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Superuser created.'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))

        self.stdout.write('Creating categories and subcategories...')
        
        categories_data = {
            'Starters': ['Veg Starters', 'Non-Veg Starters'],
            'Main Course': ['Veg Main Course', 'Non-Veg Main Course'],
            'Rice & Biryani': ['Veg Biryani', 'Non-Veg Biryani', 'Fried Rice'],
            'Breads': ['Roti', 'Naan', 'Paratha'],
            'Desserts': ['Indian Sweets', 'Ice Cream', 'Cakes'],
            'Juices & Beverages': ['Fresh Juices', 'Milkshakes', 'Soft Drinks'],
            'Sweets': ['Traditional Sweets', 'Modern Sweets']
        }
        
        order = 1
        for cat_name, subcats in categories_data.items():
            cat_slug = cat_name.lower().replace(' ', '-').replace('&', 'and')
            category, created = Category.objects.get_or_create(
                name=cat_name, 
                slug=cat_slug,
                defaults={'display_order': order}
            )
            
            sub_order = 1
            for sub_name in subcats:
                sub_slug = sub_name.lower().replace(' ', '-').replace('&', 'and')
                SubCategory.objects.get_or_create(
                    name=sub_name,
                    slug=sub_slug,
                    category=category,
                    defaults={'display_order': sub_order}
                )
                sub_order += 1
            order += 1

        self.stdout.write(self.style.SUCCESS('Categories created.'))
        self.stdout.write('Creating food items...')

        food_items_data = [
            # Starters
            {'name': 'Paneer Tikka', 'cat': 'Starters', 'sub': 'Veg Starters', 'price': 249, 'is_veg': True, 'desc': 'Spicy paneer roasted in tandoor.'},
            {'name': 'Veg Manchurian', 'cat': 'Starters', 'sub': 'Veg Starters', 'price': 199, 'is_veg': True, 'desc': 'Indo-chinese fried veg balls.'},
            {'name': 'Hara Bhara Kebab', 'cat': 'Starters', 'sub': 'Veg Starters', 'price': 219, 'is_veg': True, 'desc': 'Healthy green kebabs.'},
            {'name': 'Chicken Tandoori', 'cat': 'Starters', 'sub': 'Non-Veg Starters', 'price': 349, 'is_veg': False, 'desc': 'Classic roasted chicken.'},
            {'name': 'Chicken 65', 'cat': 'Starters', 'sub': 'Non-Veg Starters', 'price': 289, 'is_veg': False, 'desc': 'Spicy deep fried chicken.'},
            {'name': 'Fish Fry', 'cat': 'Starters', 'sub': 'Non-Veg Starters', 'price': 399, 'is_veg': False, 'desc': 'Crispy fried fish.'},
            
            # Main Course
            {'name': 'Dal Makhani', 'cat': 'Main Course', 'sub': 'Veg Main Course', 'price': 199, 'is_veg': True, 'desc': 'Creamy black lentils.'},
            {'name': 'Paneer Butter Masala', 'cat': 'Main Course', 'sub': 'Veg Main Course', 'price': 279, 'is_veg': True, 'desc': 'Rich paneer gravy.'},
            {'name': 'Aloo Gobi', 'cat': 'Main Course', 'sub': 'Veg Main Course', 'price': 179, 'is_veg': True, 'desc': 'Potato and cauliflower.'},
            {'name': 'Butter Chicken', 'cat': 'Main Course', 'sub': 'Non-Veg Main Course', 'price': 299, 'is_veg': False, 'desc': 'Iconic creamy chicken curry.'},
            {'name': 'Mutton Rogan Josh', 'cat': 'Main Course', 'sub': 'Non-Veg Main Course', 'price': 449, 'is_veg': False, 'desc': 'Kashmiri mutton curry.'},
            {'name': 'Chicken Tikka Masala', 'cat': 'Main Course', 'sub': 'Non-Veg Main Course', 'price': 329, 'is_veg': False, 'desc': 'Spicy roasted chicken curry.'},

            # Rice & Biryani
            {'name': 'Veg Dum Biryani', 'cat': 'Rice & Biryani', 'sub': 'Veg Biryani', 'price': 249, 'is_veg': True, 'desc': 'Aromatic vegetable biryani.'},
            {'name': 'Paneer Biryani', 'cat': 'Rice & Biryani', 'sub': 'Veg Biryani', 'price': 279, 'is_veg': True, 'desc': 'Biryani with paneer cubes.'},
            {'name': 'Hyderabadi Chicken Biryani', 'cat': 'Rice & Biryani', 'sub': 'Non-Veg Biryani', 'price': 329, 'is_veg': False, 'desc': 'Authentic Hyderabadi style.'},
            {'name': 'Mutton Biryani', 'cat': 'Rice & Biryani', 'sub': 'Non-Veg Biryani', 'price': 429, 'is_veg': False, 'desc': 'Rich mutton layered biryani.'},
            {'name': 'Chicken Fried Rice', 'cat': 'Rice & Biryani', 'sub': 'Fried Rice', 'price': 219, 'is_veg': False, 'desc': 'Wok tossed chicken and rice.'},
            {'name': 'Veg Fried Rice', 'cat': 'Rice & Biryani', 'sub': 'Fried Rice', 'price': 189, 'is_veg': True, 'desc': 'Classic Chinese fried rice.'},

            # Breads
            {'name': 'Tandoori Roti', 'cat': 'Breads', 'sub': 'Roti', 'price': 29, 'is_veg': True, 'desc': 'Whole wheat flatbread.'},
            {'name': 'Roomali Roti', 'cat': 'Breads', 'sub': 'Roti', 'price': 49, 'is_veg': True, 'desc': 'Thin soft flatbread.'},
            {'name': 'Butter Naan', 'cat': 'Breads', 'sub': 'Naan', 'price': 59, 'is_veg': True, 'desc': 'Soft flatbread with butter.'},
            {'name': 'Garlic Naan', 'cat': 'Breads', 'sub': 'Naan', 'price': 79, 'is_veg': True, 'desc': 'Naan topped with garlic.'},
            {'name': 'Lachha Paratha', 'cat': 'Breads', 'sub': 'Paratha', 'price': 69, 'is_veg': True, 'desc': 'Flaky layered bread.'},
            {'name': 'Aloo Paratha', 'cat': 'Breads', 'sub': 'Paratha', 'price': 89, 'is_veg': True, 'desc': 'Stuffed potato bread.'},

            # Desserts
            {'name': 'Gulab Jamun', 'cat': 'Desserts', 'sub': 'Indian Sweets', 'price': 99, 'is_veg': True, 'desc': 'Sweet milk solid balls.'},
            {'name': 'Rasmalai', 'cat': 'Desserts', 'sub': 'Indian Sweets', 'price': 129, 'is_veg': True, 'desc': 'Cottage cheese in sweetened milk.'},
            {'name': 'Vanilla Ice Cream', 'cat': 'Desserts', 'sub': 'Ice Cream', 'price': 79, 'is_veg': True, 'desc': 'Classic vanilla.'},
            {'name': 'Chocolate Brownie', 'cat': 'Desserts', 'sub': 'Cakes', 'price': 149, 'is_veg': True, 'desc': 'Warm brownie with ice cream.'},
            
            # Beverages
            {'name': 'Fresh Orange Juice', 'cat': 'Juices & Beverages', 'sub': 'Fresh Juices', 'price': 119, 'is_veg': True, 'desc': 'Freshly squeezed.'},
            {'name': 'Watermelon Juice', 'cat': 'Juices & Beverages', 'sub': 'Fresh Juices', 'price': 99, 'is_veg': True, 'desc': 'Refreshing summer drink.'},
            {'name': 'Mango Lassi', 'cat': 'Juices & Beverages', 'sub': 'Milkshakes', 'price': 129, 'is_veg': True, 'desc': 'Sweet yogurt mango drink.'},
            {'name': 'Oreo Shake', 'cat': 'Juices & Beverages', 'sub': 'Milkshakes', 'price': 159, 'is_veg': True, 'desc': 'Thick oreo milkshake.'},
            {'name': 'Cola', 'cat': 'Juices & Beverages', 'sub': 'Soft Drinks', 'price': 59, 'is_veg': True, 'desc': 'Chilled cola.'},
            
            # Sweets
            {'name': 'Kaju Katli', 'cat': 'Sweets', 'sub': 'Traditional Sweets', 'price': 199, 'is_veg': True, 'desc': 'Cashew fudge.'},
            {'name': 'Motichoor Laddoo', 'cat': 'Sweets', 'sub': 'Traditional Sweets', 'price': 149, 'is_veg': True, 'desc': 'Sweet gram flour balls.'},
        ]

        # Reliable food image URLs - using loremflickr for guaranteed food images
        food_images = {
            'Paneer Tikka': 'https://images.unsplash.com/photo-1567188040759-fb8a883dc6d6?w=400&h=300&fit=crop',
            'Veg Manchurian': 'https://images.unsplash.com/photo-1645177628172-a94c1f96e6db?w=400&h=300&fit=crop',
            'Hara Bhara Kebab': 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400&h=300&fit=crop',
            'Chicken Tandoori': 'https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=400&h=300&fit=crop',
            'Chicken 65': 'https://images.unsplash.com/photo-1610057099443-fde6c99db9e1?w=400&h=300&fit=crop',
            'Fish Fry': 'https://images.unsplash.com/photo-1580476262798-bddd9f4b7369?w=400&h=300&fit=crop',
            'Dal Makhani': 'https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400&h=300&fit=crop',
            'Paneer Butter Masala': 'https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=400&h=300&fit=crop',
            'Aloo Gobi': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&h=300&fit=crop',
            'Butter Chicken': 'https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400&h=300&fit=crop',
            'Mutton Rogan Josh': 'https://images.unsplash.com/photo-1545247181-516773cae754?w=400&h=300&fit=crop',
            'Chicken Tikka Masala': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=400&h=300&fit=crop',
            'Veg Dum Biryani': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=400&h=300&fit=crop',
            'Paneer Biryani': 'https://images.unsplash.com/photo-1589302168068-964664d93dc0?w=400&h=300&fit=crop',
            'Hyderabadi Chicken Biryani': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=400&h=300&fit=crop',
            'Mutton Biryani': 'https://images.unsplash.com/photo-1642821373181-696a54913e93?w=400&h=300&fit=crop',
            'Chicken Fried Rice': 'https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400&h=300&fit=crop',
            'Veg Fried Rice': 'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400&h=300&fit=crop',
            'Tandoori Roti': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=400&h=300&fit=crop',
            'Roomali Roti': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&h=300&fit=crop',
            'Butter Naan': 'https://images.unsplash.com/photo-1596560548464-f010549b84d7?w=400&h=300&fit=crop',
            'Garlic Naan': 'https://images.unsplash.com/photo-1596560548464-f010549b84d7?w=400&h=300&fit=crop',
            'Lachha Paratha': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=400&h=300&fit=crop',
            'Aloo Paratha': 'https://images.unsplash.com/photo-1589302168068-964664d93dc0?w=400&h=300&fit=crop',
            'Gulab Jamun': 'https://images.unsplash.com/photo-1666190020719-718adf515a4a?w=400&h=300&fit=crop',
            'Rasmalai': 'https://images.unsplash.com/photo-1571006752167-3547750ce7f3?w=400&h=300&fit=crop',
            'Vanilla Ice Cream': 'https://images.unsplash.com/photo-1570197788417-0e82375c9be7?w=400&h=300&fit=crop',
            'Chocolate Brownie': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400&h=300&fit=crop',
            'Fresh Orange Juice': 'https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?w=400&h=300&fit=crop',
            'Watermelon Juice': 'https://images.unsplash.com/photo-1534353473418-4cfa6c56fd38?w=400&h=300&fit=crop',
            'Mango Lassi': 'https://images.unsplash.com/photo-1527661591475-527312dd65f5?w=400&h=300&fit=crop',
            'Oreo Shake': 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&h=300&fit=crop',
            'Cola': 'https://images.unsplash.com/photo-1554866585-cd94860890b7?w=400&h=300&fit=crop',
            'Kaju Katli': 'https://images.unsplash.com/photo-1645177628172-a94c1f96e6db?w=400&h=300&fit=crop',
            'Motichoor Laddoo': 'https://images.unsplash.com/photo-1666190020719-718adf515a4a?w=400&h=300&fit=crop',
        }

        default_img = 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400&h=300&fit=crop'

        for item in food_items_data:
            category = Category.objects.get(name=item['cat'])
            subcategory = SubCategory.objects.get(name=item['sub'], category=category)
            
            FoodItem.objects.get_or_create(
                name=item['name'],
                defaults={
                    'category': category,
                    'subcategory': subcategory,
                    'price': item['price'],
                    'is_veg': item['is_veg'],
                    'description': item['desc'],
                    'image': food_images.get(item['name'], default_img),
                    'rating': round(random.uniform(3.5, 5.0), 1)
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with food items.'))

