
from myapp.views import *
from django.urls import path






urlpatterns = [
    # User login & register
    path('register', RegisterUserAPIView.as_view(), name="register"),
    path('log/', LoginView.as_view()),

    # Registerd User
    path('user/', Userlist.as_view(), name="user"),
    path('user/<int:pk>/', Userdetails.as_view(), name='user-detail'),

    # Register User Details
    path('info/', info.as_view()),
    path('info/<int:pk>/', infodetails.as_view(), name='info-detail'),

    # Login User Detail
    path('loginuser-detail/', UserDetailAPI.as_view()),
    # Change the user password 
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),


]
