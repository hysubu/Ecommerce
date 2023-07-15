from django.shortcuts import render,redirect
from product.models import Product,Subcatagory,Catagory,Product_Photo,User,Add_To_Cart,Order_deatil
from django.db.models import Q
from user .models import *
from user import views
from xhtml2pdf import pisa
from django.template.loader import get_template
import random

# from django.shortcuts import get_object_or_404



 #<<<<<<<<<<<<<<<<<<<<<<<<< Catagory View >>>>>>>>>>>>>>>>>>>>


def product_catagory(request):
    try:
        all_catagory = Catagory.objects.all() 
        print("catagory",all_catagory)
        return render(request,'Product_View.html',{'all_catagory':all_catagory})
    except Exception as e :
        print(e)


# Sub-Catagory and product filter view function 


def sub_catagory(request,slug):
    try :
        product = Product.objects.filter( Q( product__slug = slug )| Q(product__sub_catagory__slug = slug))
        return render(request,'Product_View.html',{"product":product})
    except Exception as e :
        print(e)


#<<<<<<<<<<<<<<<<<<<<<<< Single Product View >>>>>>>>>>>>>>>>>>>>>

def single_product(request,id):
    try:
        get_product = Product.objects.get(id=id)
        return render(request,'SingleProduct.html',{"get_product":get_product})
    except Exception as e  :
        print(e)



#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Add To Cart Product View >>>>>>>>>>>>>>>>>>>>>>>>>>>.


def add_to_cart(request):
    try :
        if request.method == "GET":
            user = User.objects.get(id=request.session['id'])
            product_id = request.GET.get('item')
            print("p_id",product_id)
            product = Product.objects.get(id = product_id)
            print("produ",product)
            Add_To_Cart(user=user,product=product).save()
            return redirect('add-to-cart')
    except Exception as e :
        print(e)    
    return render(request,'Addtocart.html')



# <<<<<<<<<<<<<<Show Cart view Function >>>>>>>>>>>>>>>>>>>>>>>>>


def show_cart(request):
    user = User.objects.get(id=request.session['id'])
    print("user",user)
    cart = Add_To_Cart.objects.filter(user=user)
    print("user",cart.values())
    total_amount = 0
    for c in cart :
        print("qq",c.quantity)
        total_amount = total_amount  + (c.product.discount_price * int(c.quantity))   
    return render(request,"Addtocart.html",{"cart":cart,"total":total_amount})


# Increase cart item >>>>>>>>>>>>>>>>>>>>>>>>>>>.


def increse_cart_item(request):
    if request.method == "POST":
        product_quantity = request.POST['quantity']
        Add_To_Cart.objects.filter(id=request.POST['id']).update(    
            quantity =int(product_quantity)+1
        )
        return redirect('show-cart')
    return render(request,'Addtocart.html')
    

# remove decrese - cart - product 


def decrese_cart_item(request):
    if request.method =="POST":
        product_quantity = request.POST['quantity']
        Add_To_Cart.objects.filter(id=request.POST['id']).update(
            quantity = int(product_quantity)-1
        )
        return redirect('show-cart')
    return render(request,'Addtocart.html')




# <<<<<<<<< Remove Cart Item >..................

def remove_item(request,id):
    try :
        remove_item = Add_To_Cart.objects.get(id=id)
        remove_item.delete()
        return redirect('show-cart')

    except Exception as e :
        print(e)

        
# Search Product View function >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>. 



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
    return render(request,'Product_View.html',{"p_detail":product}) 



# Select Order Address >>>>>>>>>>>>>>>>>>>>

def select_address(request):
    address = Address.objects.filter(username =  User.objects.get(id=request.session['id'])).first
    address2 = Address.objects.filter(username =  User.objects.get(id=request.session['id'])).last
    print("address",address)

    # if request.method =="POST":
    
    return render(request,'Selectadd.html',{"address":address,"address2":address2})


# Select Address >>>>>>>>>>>>>>>>>>>

def order_address(request):
    if request.method == "POST":
        ord_address = request.POST['address']
        print("order address",ord_address)
        ord_user = User.objects.get(id=request.session['id'])
        print("order user",ord_user)
        Order_deatil(user=ord_user,order_address=ord_address).save()
        return redirect('place-order')
    return render(request,'Selectadd.html')


#<<<<<<<<<<<<<<<< Place order >>>>>>>>>>>>>>>>>>>>>>>.
def place_order(request):
    login_user = User.objects.get(id = request.session['id'])
    print('user',login_user)
    
    placholder_user = Add_To_Cart.objects.filter(user=login_user)
    print('place_holder',placholder_user)
    print(placholder_user.values())
    quantity = 0  
    total_amount = 0
    for p in placholder_user :
        quantity = quantity +  p.quantity       
        total_amount =total_amount +(p.quantity * p.product.discount_price) 
    print("q",quantity)
    print('tam',total_amount)
    return render(request,"Checkout.html",{"product_quantity":quantity,
                                            "total_amount":total_amount,
                                            "search":True})   




# Select Product Detail>>>>>>>>>>

def product_detail(request):
    if request.method == "POST":
        random_number  = "1234567895"
        order_id  = ""
        for i in range(0,12):
            o_id = random.choice(random_number)
            order_id = order_id + o_id
        print("empp",order_id)
        user = User.objects.get(id = request.session['id'])
        print('us',user)
        ord_user = user
        # ord_product = request.POST['']
        ord_num = order_id
        ord_quantity = request.POST['quantity']
        ord_price = request.POST['totalprice']
        ord_method = request.POST['order_method']
        ord_address = request.POST['address']
        order = Order_deatil(user=ord_user,order_id = ord_num,quantity=ord_quantity,total_price = ord_price, payment_method  = ord_method,product_address=ord_address)
        order.save() 
    return render(request,'Addtocart.html')


def pdf_create(request):
    return render(request,'pdf.html')






def debitcard(request):
    return render(request,'Debitcard.html')



