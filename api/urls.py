"""Api urls."""

# Django modules
from django.conf.urls import url, include

from rest_framework import routers
from api.views import UserAPIView, UserDetail, UserViewSet, RoomAPIView, RoomDetail, RoomViewSet, FavoritesDetail, Search




# Api
from api.views import UserViewSet

"""
DefaultRouter will define the standard REST
GET, POST, PUT, DELETE...
"""
router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename = 'user')
router.register(r'room', RoomViewSet, basename = 'room')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    
    url('viewset/', include(router.urls)),

    url('user/', UserAPIView.as_view()),
    url('room/', RoomAPIView.as_view()),

    # UserDetail shows user detail
    url('user_detail/<int:id>/', UserDetail.as_view()),
    url('room_detail/<int:id>/', RoomDetail.as_view()),

    # Favorites 
    url('favorites/<int:id_user>,<int:id_room>/', FavoritesDetail.as_view()),
    url('favorites/<int:id>/', FavoritesDetail.as_view()),

    # Search
    url('search/<str:location>/', Search.as_view()),
]