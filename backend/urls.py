from django.contrib import admin
from django.urls import path, include

"""
JWT endpoints:
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),

    path('', include('quarto.urls')),
]



