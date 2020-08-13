from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Room, Images_Room, Favorites

admin.site.register(User,UserAdmin)
admin.site.register(Room)
admin.site.register(Images_Room)
admin.site.register(Favorites)
