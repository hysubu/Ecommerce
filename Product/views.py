from django.shortcuts import render,redirect
from Product.models import Product,Subcatagory,Catagory,Product_Photo,User,Add_To_Cart,Order_deatil
from django.db.models import Q
from User .models import *
from User import views
from django.views.decorators.csrf import csrf_exempt
# from xhtml2pdf import pisa
from django.template.loader import get_template
import random

# Create your views here.

csrf_exempt
def shopping(request):
    return render(request,'Shopping.html')



csrf_exempt
def product_catagory(request):
    try:
        all_catagory = Catagory.objects.all() 
        print("catagory",all_catagory)
        return render(request,'Shopping.html',{'all_catagory':all_catagory})
    except Exception as e :
        print(e)


# Sub-Catagory and product filter view function 

csrf_exempt
def sub_catagory(request,slug):
    try :
        product = Product.objects.filter( Q( product__slug = slug )| Q(product__sub_catagory__slug = slug))
        print("product",product)
        return render(request,'Shopping.html',{"product":product})
    except Exception as e :
        print(e)



#<<<<<<<<<<<<<<<<<<<<<<< Single Product View >>>>>>>>>>>>>>>>>>>>>
csrf_exempt
def single_product(request,id):
    try:
        get_product = Product.objects.get(id=id)
        return render(request,'Product_Card.html',{"get_product":get_product})
    except Exception as e  :
        print(e)









# <<<<<<<<<<<<<<<<<<<<<<<<<<<< Search product >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
csrf_exempt
def search_product(request):
    search_product = request.GET.get('query')
    print("search",search_product)
    if len(search_product)>= 70 and len(search_product = 0):
        Product.objects.none()
    else:
        product_detail = Product.objects.filter(title__icontains = search_product)
        product_brand = Product.objects.filter(brand__icontains = search_product)
        # sub_product = Product.objects.filter(subcatagory__sub_catagory_name__icontains = search_product)
        product = product_detail.union(product_brand)
        print("product_detail",product_detail)
    return render(request,'Shopping.html',{"search_product":product,"search":True}) 

csrf_exempt
def single_product(request,id):
    try:
        get_product = Product.objects.get(id=id)
        return render(request,'Product_Card.html',{"get_product":get_product})
    except Exception as e  :
        print(e)

csrf_exempt
def add_to_cart(request):
    try :
        if request.method == "POST":
            user = User.objects.get(id=request.session['id'])
            print("user",user)
            product_id = request.POST['item']
            print("p_id",product_id)
            product = Product.objects.get(id = product_id)
            print("produ",product)
            Add_To_Cart(user=user,product=product).save()
            return redirect('cart-product')
    except Exception as e :
        print(e)    
    return render(request,'Shopping.html')


csrf_exempt
def cart_product(request):
    cartuser = User.objects.get(id = request.session["id"])
    print("user",cartuser)
    cart_item = Add_To_Cart.objects.filter(user=cartuser)
    print("cart_item",cart_item)
    total_price = 0
    total_quantity = 0
    for i in cart_item :
        total_quantity = total_quantity + i.quantity
        total_price = total_price + (i.quantity * i.product.discount_price)
    print("total_price",total_price)
    print("total_price",total_quantity)
   
    return render(request,'Cart_Product.html',{"cart_item":cart_item,
                                                "total_quantity":total_quantity,
                                                 "total_price":total_price})

csrf_exempt
def remove_item(request,id):
    Add_To_Cart.objects.get(id=id).delete()
    return redirect('cart-product')

csrf_exempt
def increse_cart_item(request):
    if request.method == "POST":
        product_quantity = request.POST['quantity']
        Add_To_Cart.objects.filter(id=request.POST['id']).update(    
            quantity =int(product_quantity)+1
        )
        return redirect('cart-product')
    return render(request,'Cart_Product.html')


csrf_exempt
def decrese_cart_item(request):
    if request.method =="POST":
        product_quantity = request.POST['quantity']
        Add_To_Cart.objects.filter(id=request.POST['id']).update(
            quantity = int(product_quantity)-1
        )
        return redirect('cart-product')
    return render(request,'Cart_Product.html')




#  Address Selection 


csrf_exempt
def addres_selection(request):
    address = Address.objects.filter(username =  User.objects.get(id=request.session['id'])).first
    address2 = Address.objects.filter(username =  User.objects.get(id=request.session['id'])).last
    print("address",address)
    print("address",address2)
    
    return render(request,"Select_Address.html",{"address":address,"address2":address2})

csrf_exempt
def order_address(request):
    if request.method == "POST":
        ord_address = request.POST['address']
        print("order address",ord_address)
        ord_user = User.objects.get(id=request.session['id'])
        print("user",ord_user)
        ord_add = Address.objects.filter(username = ord_user)
        print("user",ord_add)
        print("order user",ord_user)
        Order_deatil(user=ord_user,order_address=ord_address).save()
        return redirect('place-order')
    return render(request,'Selectadd.html')
csrf_exempt
def placeorder(request):
    return render(request,'PlaceOrder.html')
