from django.urls import path

from .views import *


urlpatterns = [
    path('email_digest_subscriptions/', EmailDigestSubscriptionListView.as_view(), name='ED_subscription-list'),
    path('email_digest_subscriptions/<int:pk>/', EmailDigestSubscriptionDetailView.as_view(),
         name='emaildigestsubscription-detail'),
    path('email_digest_email_digests/', EmailDigestEmailDigestListView.as_view(), name='emailDigestEmailDigest-list'),
    path('email_digest_email_digests/<int:pk>/', EmailDigestEmailDigestDetailView.as_view(),
         name='emailDigestEmailDigest-detail'),
    path('email_digest_un_subscriptions/', EmailDigestUnsubscriptionListView.as_view(), name='unsubscription-list'),
    path('email_digest_un_subscriptions/<int:pk>/', EmailDigestUnsubscriptionDetailView.as_view(),
         name='unsubscription-detail'),
    path('email_digest_email_digest_stories/', EmailDigestEmailDigestStoriesListView.as_view(), name='stories-list'),
    path('email_digest_email_digest_stories/<int:pk>/', EmailDigestEmailDigestStoriesDetailView.as_view(),
         name='stories-detail'),
    path('email_digest_user_subscriptions/', EmailDigestUserSubscriptionListView.as_view(), name='user_sub-list'),
    path('email_digest_user_subscriptions/<int:pk>/', EmailDigestUserSubscriptionDetailView.as_view(),
         name='user_sub-detail'),
    path('email_digest_anonymous_subscriptions/', EmailDigestAnonymousSubscriptionListView.as_view(),
         name='anonymous_subscription-list'),
    path('email_digest_anonymous_subscriptions/<int:pk>/', EmailDigestAnonymousSubscriptionDetailView.as_view(),
         name='anonymous-list'),
]
