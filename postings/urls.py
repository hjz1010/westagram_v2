from django.urls import path

from postings.views import PostingView

urlpatterns = [
    path('/posting', PostingView.as_view()),

]
