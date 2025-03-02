from django.urls import path
from .views import send_otp, verify_otp
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('verify/', views.verify, name='verify'),
    path('send-otp/', send_otp),
    path('verify-otp/', verify_otp),
]


