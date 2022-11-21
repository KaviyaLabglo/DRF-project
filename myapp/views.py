from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate

from myapp.serializers import (
    LoginSerializer,
    ChangePasswordSerializer,
    RegisterSerializer,
    UserSerializer,
    DetailSerializer,
)
from myapp.permission import IsOwnerOrReadOnly
from myapp.models import User_Detail

from rest_framework import generics, views, viewsets
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


from rest_framework import filters
 

class LoginView(views.APIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LogoutView(views.APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        print(request.user)
        logout(request)
        return Response(status=status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserDetailAPI(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        detail = User_Detail.objects.get(user=user)
        serializer = DetailSerializer(detail, context={'request': request})
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['username']


class User_Detail_ViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    serializer_class = DetailSerializer
    queryset = User_Detail.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['user']
