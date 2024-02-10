from rest_framework import serializers

from .models import *


class NewsItemListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsItem
        fields = ['id', 'user', 'up_votes', 'down_votes', 'url']


class NewsItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = ['id', 'user', 'up_votes', 'down_votes', 'is_ask', 'is_show', 'points', 'num_comments', 'left',
                  'right', 'tree_id', 'level', ]


class NewsVoteListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsVote
        fields = ['id', 'item', 'user', 'url']


class NewsVoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsVote
        fields = ['id', 'item', 'user', 'vote']


class NewsStoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsStory
        fields = ['item_ptr', 'title', 'text', 'url']


class NewsStoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsStory
        fields = ['item_ptr', 'title', 'text', 'url', 'do_mail']


class NewsCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsComment
        fields = ['item_ptr', 'to_story']


class NewsCommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsComment
        fields = ['item_ptr', 'to_story', 'text']
