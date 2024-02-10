from django.urls import path

from .views import *


urlpatterns = [
    path('account_customusers/', AccountCustomUserListView.as_view(), name='account_customusers-list'),
    path('account_customusers/<int:pk>/', AccountCustomUserDetailView.as_view(), name='accountcustomuser-detail'),
    path('account_invitations/', AccountsInvitationListView.as_view(), name='accountInvitation-list'),
    path('account_invitations/<int:pk>/', AccountsInvitationDetailView.as_view(), name='accountsinvitation-detail'),
    path('account_email_verifications/', AccountsEmailVerificationListView.as_view(), name='verifications-list'),
    path('account_email_verifications/<int:pk>/', AccountsEmailVerificationDetailView.as_view(),
         name='accountsemailverification-detail'),
    path('account_password_rest_requests/', AccountPasswordResetRequestListView.as_view(), name='rest_password-list'),
    path('account_password_rest_requests/<int:pk>/', AccountPasswordResetRequestDetailView.as_view(),
         name='rest_password-detail'),
    path('auth_permissions/', AuthPermissionListView.as_view(), name='auth_permissions-list'),
    path('auth_permissions/<int:pk>/', AuthPermissionDetailView.as_view(), name='authpermission-detail'),
    path('auth_groups/', AuthGroupListView.as_view(), name='auth_group-list'),
    path('auth_groups/<int:pk>/', AuthGroupDetailView.as_view(), name='auth_group-detail'),
    path('django_admin_log/', DjangoAdminLogListView.as_view(), name='django_admin_log-list'),
    path('django_admin_log/<int:pk>/', DjangoAdminLogDetailView.as_view(), name='djangoadminlog-detail')
]

