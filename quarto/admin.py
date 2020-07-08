from django.contrib import admin
from .models import User, Room, Images_Room, Favorites

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Images_Room)
admin.site.register(Favorites)
