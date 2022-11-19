from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import login

from myapp.models import *
from myapp.serializers import *
from myapp.permission import *

from rest_framework import generics, mixins, views
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


from rest_framework import filters


class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(views.APIView):
    #renderer_classes = [StaticHTMLRenderer]

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


class Userlist(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_class = ['id']

    filter_backends = [filters.SearchFilter]
    search_fields = ['id']
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Userdetails(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class info(mixins.ListModelMixin,
           mixins.CreateModelMixin,
           generics.GenericAPIView):
    queryset = userdetail.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    serializer_class = DetailSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetailAPI(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        detail = userdetail.objects.get(user=user)
        serializer = DetailSerializer(detail, context={'request': request})
        return Response(serializer.data)


class infodetails(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = userdetail.objects.all()
    serializer_class = DetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    


    
    
from rest_framework.permissions import IsAuthenticated

class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
