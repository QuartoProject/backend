from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


"""
JWT endpoints: /api/token/ and /api/token/refresh/
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),

    path('', include('quarto.urls')),
]

    # path('api/token/', TokenObtainPairView.as_view()),
    # path('api/token/refresh/', TokenRefreshView.as_view()),


