from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('spinwheel/', include('spinwheel.urls')),
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('users.urls')),  # User app
#     path('game/', include('spinwheel.urls')),  # Spinwheel app
# ]