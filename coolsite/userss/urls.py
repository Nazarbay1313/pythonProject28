from django.urls import path

from userss.views import Login, Register, UserProfile, logout_user

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout_user/', logout_user, name='logout_user'),
    path('update_profile/', UserProfile.as_view(), name='update_profile'),
]
