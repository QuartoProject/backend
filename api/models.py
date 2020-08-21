"""Api models."""

# Django modules
from django.db import models
from django.contrib.auth.models import AbstractUser
# ugettext_lazy is a translation hook. Good practices
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    
    USERNAME_FIELD = 'email'
    """REQUIRED_FIELDS array specified the fields that are required by the
    createsuperuser command.
    The username has to be in that list, because otherwise Django complains
    when creating super users.
    """
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    location = models.CharField(max_length=120, blank=False, default='bogota')
    description = models.TextField(blank=True)
    phone = models.PositiveIntegerField(blank=True, default=1112223344)
    active = models.BooleanField(default=True)
    favorite_rooms = models.ForeignKey('Favorites', on_delete=models.CASCADE, blank=True, null=True)
    picture = models.ImageField('profile picture', upload_to='users/pitures/',default='/media/rooms/pictures/user_profile.png',blank=True,null=True)
    
    def __str__(self):
        return "{}".format(self.user)


class Room(models.Model):
    id_user = models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=True, default=999999)
    nearest_places = models.CharField(max_length=120)
    mts2 = models.CharField(max_length=120, blank=False, default='10mts2')
    furniture = models.TextField(blank=True)
    private_bath = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    closet = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    pet = models.BooleanField(default=False)
    washing_machine = models.BooleanField(default=False)
    furnish = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    smoke = models.BooleanField(default=False)
    couple = models.BooleanField(default=False)
    family_atmosphere = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    id_images = models.ForeignKey('Images_Room', null=True, on_delete=models.CASCADE)
    #picture = models.ImageField('room pictures',upload_to='media/rooms/pictures',default='/media/rooms/pictures/photo.png',blank=True,null=True)
    def __str__(self):
        return 'id: {_id} id_user: {_id_user} available: {_available}'.format(
            _id = self.id,
            _id_user = self.id_user,
            _available = self.available,
        )


class Images_Room(models.Model):

    image = models.URLField(blank=False)
    #id_room = models.ForeignKey('Room', on_delete=models.CASCADE)

    def __str__(self):
        return 'id: {_id}'.format(
            _id = self.id,
        )


class Favorites(models.Model):
    id_user = models.ForeignKey('User', on_delete=models.CASCADE)
    id_room = models.ForeignKey('Room', on_delete=models.CASCADE)
    def __str__(self):
        return 'id = {_id} id_user = {_id_user} id_room = {_id_room}'.format(
            _id = self.id,
            _id_user = self.id_user,
            _id_room = self.id_room,
        )