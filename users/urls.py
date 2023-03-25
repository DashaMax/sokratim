from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (MainPageView, UserEnterView, UserProfileView,
                         UserRegistrationView)

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('enter/', UserEnterView.as_view(), name='enter'),
    path('profile/<slug>/', UserProfileView.as_view(), name='profile'),
    path('exit/', LogoutView.as_view(), name='exit'),
]