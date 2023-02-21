from django.contrib import admin
from User .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','contact_number','profile_photo','password_key','password','created_at','is_active']
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display  = ['city']