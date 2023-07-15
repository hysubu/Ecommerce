
from django.urls import path,include
from home import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from product .models import Product
# from user import urls
urlpatterns = [

    path('admin/',admin.site.urls),
    path('', views.home,name="home"),
    path('user/',include("user.urls")),
    path('product/',include("product.urls")),
   
    path('buy/', views.buy_now, name='buy-now'),
    # path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    # path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]   + static (settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)

