from django.urls import path
from .views import TweetListCreateAPIView, CommentListCreateAPIView, MarkListCreateAPIView

urlpatterns = [
    path('tweets/', TweetListCreateAPIView.as_view()),
    path('comments/', CommentListCreateAPIView.as_view()),
    path('marks/', MarkListCreateAPIView.as_view()),
]