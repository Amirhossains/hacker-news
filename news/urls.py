from django.urls import path

from .views import *

urlpatterns = [
    path('news_items/', NewsItemListView.as_view(), name='newsItem-list'),
    path('news_items/<int:pk>/', NewsItemDetailView.as_view(), name='newsitem-detail'),
    path('news_votes/', NewsVoteListView.as_view(), name='newsVote-list'),
    path('news_votes/<int:pk>/', NewsVoteDetailView.as_view(), name='newsvote-detail'),
    path('news_stories/', NewsStoryListView.as_view(), name='newsStory-list'),
    path('news_stories/<int:pk>/', NewsStoryDetailView.as_view(), name='newsstory-detail'),
    path('news_comments/', NewsCommentListView.as_view(), name='newsComment-list'),
    path('news_comments/<int:pk>/', NewsCommentDetailView.as_view(), name='newsComment-detail'),
]
