from django.urls import path

from .views import *

urlpatterns = [
    path('django_content_types/', DjangoContentTypeListView.as_view(), name='django_content_type-list'),
    path('django_content_types/<int:pk>/', DjangoContentTypeDetailView.as_view(), name='djangocontenttype-detail'),
]
