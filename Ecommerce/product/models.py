from django.db import models
from django.utils.text import slugify
# from product.models import Product
from django.shortcuts import render
from user.models import User,Address

# Create your models here.


# Product Catagory Details >>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class Catagory(models.Model):
    CATAGORY_CHOICES = ((
    ("Mens","Mens"),
    ("Womens","Womens"),
    ("Electronics","Electronics"),
    ("Furniture","Furniture"),
    ("Medicine","Medicine"),   
    ))
    catagory = models.CharField(choices=CATAGORY_CHOICES,max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)

    def __str__(self):
        return self.catagory


    def save(self,*args,**kwargs):
        self.slug = slugify(self.catagory)
        super(Catagory,self).save(*args,*kwargs)
    

# Product Sub Catagory details>>>>>>>>>>>>>>>>>>>>


class Subcatagory(models.Model):
    sub_catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE,related_name="subcatagory")
    slug = models.SlugField(unique=True,null=True,blank=True)
    sub_catagory_name = models.CharField(max_length=100)

    def __str__(self):
            return self.sub_catagory_name
    def save(self,*args,**kwargs):
        self.slug = slugify(self.sub_catagory)
        super(Subcatagory,self).save(*args,*kwargs)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.sub_catagory_name)
        super(Subcatagory,self).save(*args,*kwargs)



# Product detail >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class Product(models.Model):
    product = models.ForeignKey(Subcatagory,on_delete=models.CASCADE,related_name="product")
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    slug = models.SlugField(unique=False,null=True,blank=True)
    brand = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to="product_images") 



    def save(self,*args,**kwargs):
        self.slug = slugify(self.product)
        super(Product,self).save(*args,*kwargs)


    def __str__(self):
        return self.title +  self.product.sub_catagory.catagory

  
# Product Photo details <>>>>>>>>>>>>>>>>>>>.>>>>>>>>>>>>>>>>>>>>>

class Product_Photo(models.Model):
    prduct_name = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="image")
    product_photo = models.ImageField(upload_to="product_image")



# Add-to-cart detail models >>>>>>>>>>>>>>>>>>>>>>>>>>>>>.


class Add_To_Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    def __str__(self):
        return str(self.quantity * self.product.discount_price) 
         
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)



# Order Details >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class Order_deatil(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    order_id = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    total_price = models.CharField(max_length=100,null=True)
    order_date = models.DateTimeField(auto_now_add=True,null=True)
    payment_method  = models.CharField(max_length=200,null=True) 
    order_address = models.TextField(max_length=500,null=True) 

