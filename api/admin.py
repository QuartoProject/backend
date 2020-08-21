"""Api admin."""

# Django modules
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Local modules
from .models import User, UserProfile, Images_Room, Favorites, Room

"""
It defines an Inline object for the admin panel
"""
class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False



@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal information'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    
    list_display = ('email', 
                    'first_name', 
                    'last_name', 
                    'is_staff',)
    
    search_fields = ('email', 
                     'first_name', 
                     'last_name')
    
    ordering = ('email',)
    
    inlines = (UserProfileInLine,)


admin.site.register(UserProfile)
admin.site.register(Images_Room)
admin.site.register(Favorites)
admin.site.register(Room)