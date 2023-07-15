from django.urls import path
from user import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    
    path('usersignup/',views.Usersignup,name="signup"),
    path('login/',views.userlogin,name="login"),
    path('logout/',views.userlogout,name="logout"),
    path('forgetpassword/',views.forgetpassword,name="forgetpassword"),
    path('profile/',views.profile,name="profile"),
    path('update_profile/<int:id>/',views.profile_update,name="update"),
    path('user/address/',views.user_address,name="address"),
    path('view/address/<int:id>/',views.view_address,name="view-address"),
    # path('address/view/',views.view_address,name="view-address")

]