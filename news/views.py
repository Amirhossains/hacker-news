from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from .serializers import *


def find(model, pk):
    try:
        r = model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise Http404
    return r


class NewsItemListView(APIView):

    def get(self, request):
        newsItems = NewsItem.objects.all()
        serializer = NewsItemListSerializer(newsItems, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NewsItemDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsItemDetailView(APIView):

    def get(self, request, pk):
        newsItem = find(NewsItem, pk)
        serializer = NewsItemDetailSerializer(newsItem)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        newsItem = find(NewsItem, pk)
        serializer = NewsItemDetailSerializer(newsItem, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        newsItem = find(NewsItem, pk)
        newsItem.delete()
        return Response(data={'detail': 'The news item deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class NewsStoryListView(APIView):

    def get(self, request):
        newsStories = NewsStory.objects.all()
        serializer = NewsStoryListSerializer(newsStories, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NewsStoryDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsStoryDetailView(APIView):

    def get(self, request, pk):
        newsStory = find(NewsStory, pk)
        serializer = NewsStoryDetailSerializer(newsStory)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        newsStory = find(NewsStory, pk)
        serializer = NewsStoryDetailSerializer(instance=newsStory, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        newsStory = find(NewsStory, pk)
        newsStory.delete()
        return Response(data={'detail': 'The news story deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class NewsVoteListView(APIView):

    def get(self, request):
        newsVote = NewsVote.objects.all()
        serializer = NewsVoteListSerializer(newsVote, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NewsVoteDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsVoteDetailView(APIView):

    def get(self, request, pk):
        newsVote = find(NewsVote, pk)
        serializer = NewsVoteDetailSerializer(newsVote)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        newsVote = find(NewsVote, pk)
        serializer = NewsVoteDetailSerializer(instance=newsVote, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        newsVote = find(NewsVote, pk)
        newsVote.delete()
        return Response(data={'detail': 'The news vote deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class NewsCommentListView(APIView):

    def get(self, request):
        newsComments = NewsComment.objects.all()
        serializer = NewsCommentListSerializer(newsComments, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NewsCommentDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsCommentDetailView(APIView):

    def get(self, request, pk):
        newsComment = find(NewsComment, pk)
        serializer = NewsCommentDetailSerializer(newsComment)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        newsComment = find(NewsComment, pk)
        serializer = NewsCommentDetailSerializer(instance=newsComment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)

    def delete(self, request, pk):
        newsComment = find(NewsComment, pk)
        newsComment.delete()
        return Response(data={'detail': 'The news comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
