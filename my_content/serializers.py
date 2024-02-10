from rest_framework import serializers

from .models import *


class DjangoContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoContentType
        fields = ['id', 'app_label', 'model']


class DjangoAdminLogListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = ['id', 'user', 'content_type', 'object_repr', 'url']


class DjangoAdminLogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = ['id', 'user', 'content_type', 'object_repr', 'change_message', 'object_id', 'action_flag',
                  'action_time']
