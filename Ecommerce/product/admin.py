from django.contrib import admin
from .models import *
# Register your models here
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
    # list_display = ['id','product','title','selling_price',"discount_price","description",'brand','product_image','catagory']

# Catagory ..............
admin.site.register(Catagory)


# Sub Catagory ....................
admin.site.register(Subcatagory)
#     

admin.site.register(Product)

# Product_ photo
admin.site.register(Product_Photo)

# Add-to Cart ............
admin.site.register(Add_To_Cart)


# Wishlist ........
admin.site.register(Wishlist)


# product Details ....................
admin.site.register(Order_deatil)


