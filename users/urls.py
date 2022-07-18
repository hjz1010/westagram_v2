
from django.urls import path

from users.views import LoginView, SignupView, FollowView

urlpatterns = [
    path('/signup', SignupView.as_view()),
    path('/login', LoginView.as_view()),
    path('/follow', FollowView.as_view()),
]
