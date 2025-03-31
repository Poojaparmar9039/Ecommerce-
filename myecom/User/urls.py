from django.urls import path  
from . import views


urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('forgot/',views.forgot_password,name='forgot_password'),
    path('send_otp/',views.send_otp,name='send_otp'),
    path('verifyOtp/',views.verifyOtp,name='verifyOtp'),
    path('change_password/',views.change_password,name='change_password'),

]
