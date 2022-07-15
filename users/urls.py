
from django.urls import path, include

from users.views import SignupView

urlpatterns = [
    path('/signup', SignupView.as_view()),

]
