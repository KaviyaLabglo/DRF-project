
from myapp.views import (User_Detail_ViewSet,
    RegisterUserAPIView,
    LoginView,
    LogoutView,
    UserDetailAPI,
    ChangePasswordView,
    )
from django.urls import path, include


from myapp.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-information', User_Detail_ViewSet)


urlpatterns = [
    
    # User login & register
    path('register', RegisterUserAPIView.as_view(), name="register"),
    path('log/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    # Login User Detail
    path('loginuser-detail/', UserDetailAPI.as_view()),
    # Change the user password
    path('change_password/<int:pk>/', ChangePasswordView.as_view(),
         name='auth_change_password'),

    path('', include(router.urls)),

]
