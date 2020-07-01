"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quarto.views import inicio, return_users, signup, edit_user, return_rooms, create_room

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', return_users),
    path('user/<int:id>;<int:anfi>/', edit_user),
    path('signin/<str:nombre>;<str:apellido>;<str:passwd>;<str:email>;<str:lugar>;<int:anfi>;<str:desc>;<int:tel>/', signup),
    path('rooms/', return_rooms),
    path('create_room/<int:iu>;<int:price>;<str:ne_pl>;<int:mts2>;<str:furn>;<str:pri_bath>;<int:wifi>;<int:closet>;<int:kitchen>;<int:pet>;<int:w_m>;<int:furnished>;<int:tv>;<int:smoke>;<int:couple>;<int:family>;<str:desc>/', create_room)
]
