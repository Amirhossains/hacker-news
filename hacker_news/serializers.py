from rest_framework import serializers

from .models import *


class AccountCustomUserListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountCustomUser
        fields = ['id', 'username', 'email', 'is_staff', 'is_superuser', 'url']


class AccountCustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountCustomUser
        fields = ['id', 'used_invitation', 'username', 'email', 'password', 'first_name', 'last_name', 'is_active',
                  'is_staff', 'is_superuser', 'last_login', 'karma', 'about', 'level', 'left', 'right', 'tree_id',
                  'date_joined']


class AccountsInvitationListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountsInvitation
        fields = ['id', 'invite_code', 'invited_email_address', 'url']


class AccountsInvitationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsInvitation
        fields = ['id', 'invite_code', 'invited_email_address', 'num_signups']


class AccountsEmailVerificationListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountsEmailVerification
        fields = ['id', 'user', 'verified', 'url']


class AccountsEmailVerificationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsEmailVerification
        fields = ['id', 'user', 'verified', 'verified_at', 'verification_code', 'email']


class AccountPasswordResetRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountPasswordResetRequest
        fields = ['id', 'user', 'verified_code']


class AuthPermissionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = AuthPermission
      fields = ['id', 'custom_user', 'content_type', 'url']


class AuthPermissionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPermission
        fields = ['id', 'custom_user', 'content_type', 'name', 'codename']


class AuthGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroup
        fields = ['id', 'name', 'permission', 'custom_user']
