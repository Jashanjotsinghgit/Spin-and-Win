from django.urls import path
from .views import spin_wheel
from . import views

urlpatterns = [
    # path('spin/', spin_wheel),
    path('spin/', views.spin, name='spin'),
]

