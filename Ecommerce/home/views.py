from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Home.html')

def product_detail(request):
 return render(request, 'Productdetail.html')

def add_to_cart(request):
 return render(request, 'Addtocart.html')

def buy_now(request):
 return render(request, 'Buynow.html')

def profile(request):
 return render(request, 'Profile.html')


def orders(request):
 return render(request, 'Orders.html')

def change_password(request):
 return render(request, 'Changepassword.html')

def mobile(request):
 return render(request, 'Mobile.html')

def login(request):
 return render(request, 'Login.html')

def customerregistration(request):
 return render(request, 'Customeregistration.html')

def checkout(request):
 return render(request, 'checkout.html')