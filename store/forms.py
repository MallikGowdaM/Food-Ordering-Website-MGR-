from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import FoodItem, Review

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        exclude = ['rating']

class CheckoutForm(forms.Form):
    PAYMENT_CHOICES = [
        ('upi', 'UPI'),
        ('cod', 'Cash on Delivery'),
    ]
    customer_name = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField(required=False)
    address = forms.CharField(widget=forms.Textarea)
    city = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=10)
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES)
    special_instructions = forms.CharField(widget=forms.Textarea, required=False)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']
