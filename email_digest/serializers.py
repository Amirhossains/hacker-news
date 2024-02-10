from rest_framework import serializers

from .models import *


class EmailDigestSubscriptionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailDigestSubscription
        fields = ['id', 'frequency', 'weekly_weekday', 'url']


class EmailDigestSubscriptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestSubscription
        fields = ['id', 'frequency', 'weekly_weekday', 'verified_email', 'is_active']


class EmailDigestEmailDigestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestEmailDigest
        fields = ['id', 'frequency', 'weekly_weekday']


class EmailDigestUnsubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestUnsubscription
        fields = ['id', 'from_digest', 'subscription']


class EmailDigestEmailDigestStoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestEmailDigestStories
        fields = ['id', 'email_digest', 'story']


class EmailDigestUserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestUserSubscription
        fields = ['subscription', 'user']


class EmailDigestAnonymousSubscriptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestAnonymousSubscription
        fields = ['subscription_ptr', 'logged_in_user', 'verified']


class EmailDigestAnonymousSubscriptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestAnonymousSubscription
        fields = ['subscription_ptr', 'logged_in_user', 'verified', 'verified_at', 'verified_code', 'email']
