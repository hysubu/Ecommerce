from django.contrib import admin
from django.urls import path
from User import views




urlpatterns = [
    path('profilepage/',views.profile,name="profile"),
    path('regestration/',views.regestration,name="regestration"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('updateprofile/<int:id>/',views.profile_update,name="update-profile"),
    path('address/',views.address,name="address"),
    path('forgetpassword/',views.forgetpassword,name="forget-password"),
]