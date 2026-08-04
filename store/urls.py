from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('cart/', views.cart_page, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/success/<str:order_number>/', views.order_success, name='order_success'),
    path('order/<str:order_number>/', views.order_status, name='order_status'),
    path('orders/', views.order_history, name='order_history'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),

    path('api/menu/', views.api_menu_items, name='api_menu'),
    path('api/review/submit/', views.api_submit_review, name='api_submit_review'),
    path('api/order/<int:order_id>/status/', views.api_update_order_status, name='api_update_order_status'),

    path('mgr-admin/', views.admin_dashboard, name='admin_dashboard'),
    path('mgr-admin/food/', views.admin_food_list, name='admin_food_list'),
    path('mgr-admin/food/add/', views.admin_food_add, name='admin_food_add'),
    path('mgr-admin/food/<int:item_id>/edit/', views.admin_food_edit, name='admin_food_edit'),
    path('mgr-admin/food/<int:item_id>/delete/', views.admin_food_delete, name='admin_food_delete'),
    path('mgr-admin/orders/', views.admin_orders, name='admin_orders'),
    path('mgr-admin/orders/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    path('mgr-admin/reviews/', views.admin_reviews, name='admin_reviews'),
]
