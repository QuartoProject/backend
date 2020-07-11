from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, ChangePasswordSerializer, LoginSerializer
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from quarto.models import User, Room
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

"""
Register API
"""
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    model = User
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data})

"""
Login
"""
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    model = User

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        return Response({
            "User": UserSerializer(user, context=self.get_serializer_context()).data})


"""
Change password
"""
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)
    
    
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            # check old password
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Wrong password.']}, status=status.HTTP_400_BAD_REQUEST)
            
            # set password
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


