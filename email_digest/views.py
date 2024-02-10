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


class EmailDigestSubscriptionListView(APIView):

    def get(self, request):
        emailDigestSubscriptions = EmailDigestSubscription.objects.all()
        serializer = EmailDigestSubscriptionListSerializer(emailDigestSubscriptions, many=True,
                                                           context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmailDigestSubscriptionDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailDigestSubscriptionDetailView(APIView):

    def get(self, request, pk):
        emailDigestSubscription = find(EmailDigestSubscription, pk)
        serializer = EmailDigestSubscriptionDetailSerializer(emailDigestSubscription)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emailDigestSubscription = find(EmailDigestSubscription, pk)
        serializer = EmailDigestSubscriptionDetailSerializer(instance=emailDigestSubscription, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emailDigestSubscription = find(EmailDigestSubscription, pk)
        emailDigestSubscription.delete()
        return Response(data={'detail': 'The email digest subscription deleted successfully.'})


class EmailDigestEmailDigestListView(APIView):

    def get(self, request):
        emailDigestEmailDigest = EmailDigestEmailDigest.objects.all()
        serializer = EmailDigestEmailDigestSerializer(emailDigestEmailDigest, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmailDigestEmailDigestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailDigestEmailDigestDetailView(APIView):

    def get(self, request, pk):
        emailDigestEmailDigest = find(EmailDigestEmailDigest, pk)
        serializer = EmailDigestEmailDigestSerializer(emailDigestEmailDigest)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emailDigestEmailDigest = find(EmailDigestEmailDigest, pk)
        serializer = EmailDigestEmailDigestSerializer(instance=emailDigestEmailDigest, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emailDigestEmailDigest = find(EmailDigestEmailDigest, pk)
        emailDigestEmailDigest.delete()
        return Response(data={'detail': 'The digest email deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class EmailDigestUnsubscriptionListView(APIView):

    def get(self, request):
        emailDigestUnSubscription = EmailDigestUnsubscription.objects.all()
        serializer = EmailDigestUnsubscriptionSerializer(emailDigestUnSubscription, many=True,
                                                         context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmailDigestUnsubscriptionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailDigestUnsubscriptionDetailView(APIView):

    def get(self, request, pk):
        emailDigestUnsubscription = find(EmailDigestUnsubscription, pk)
        serializer = EmailDigestUnsubscriptionSerializer(emailDigestUnsubscription)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emailDigestUnsubscription = find(EmailDigestUnsubscription, pk)
        serializer = EmailDigestUnsubscriptionSerializer(instance=emailDigestUnsubscription, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emailDigestUnsubscription = find(EmailDigestUnsubscription, pk)
        emailDigestUnsubscription.delete()
        return Response(data={'detail': 'The email digest unSubscription deleted successfully.'},
                        status=status.HTTP_204_NO_CONTENT)


class EmailDigestEmailDigestStoriesListView(APIView):

    def get(self, request):
        emailDigestEmailDigestStories = EmailDigestEmailDigestStories.objects.all()
        serializer = EmailDigestEmailDigestStoriesSerializer(emailDigestEmailDigestStories, many=True,
                                                             context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmailDigestEmailDigestStoriesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailDigestEmailDigestStoriesDetailView(APIView):

    def get(self, request, pk):
        emailDigestEmailDigestStories = find(EmailDigestEmailDigestStories, pk)
        serializer = EmailDigestEmailDigestStoriesSerializer(emailDigestEmailDigestStories)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emailDigestEmailDigestStories = find(EmailDigestEmailDigestStories, pk)
        serializer = EmailDigestEmailDigestStoriesSerializer(instance=emailDigestEmailDigestStories, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emailDigestEmailDigestStories = find(EmailDigestEmailDigestStories, pk)
        emailDigestEmailDigestStories.delete()
        return Response(data={'detail': 'The email digest Story deleted successfully.'})


class EmailDigestUserSubscriptionListView(APIView):

    def get(self, request):
        emailDigestUserSubscription = EmailDigestUserSubscription.objects.all()
        serializer = EmailDigestUserSubscriptionSerializer(emailDigestUserSubscription, many=True,
                                                           context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmailDigestUserSubscriptionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailDigestUserSubscriptionDetailView(APIView):

    def get(self, request, pk):
        emailDigestUserSubscription = find(EmailDigestUserSubscription, pk)
        serializer = EmailDigestUserSubscriptionSerializer(emailDigestUserSubscription)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emailDigestUserSubscription = find(EmailDigestUserSubscription, pk)
        serializer = EmailDigestUserSubscriptionSerializer(instance=emailDigestUserSubscription, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emailDigestUserSubscription = find(EmailDigestUserSubscription, pk)
        emailDigestUserSubscription.delete()
        return Response(data={'detail': ' The email digest user subscription deleted successfully.'},
                        status=status.HTTP_204_NO_CONTENT)


class EmailDigestAnonymousSubscriptionListView(APIView):

    def get(self, request):
        emailDigestAnonymousSubscription = EmailDigestAnonymousSubscription.objects.all()
        serializer = EmailDigestAnonymousSubscriptionListSerializer(emailDigestAnonymousSubscription, many=True,
                                                                    context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmailDigestAnonymousSubscriptionDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailDigestAnonymousSubscriptionDetailView(APIView):

    def get(self, request, pk):
        emailDigestAnonymousSubscription = find(EmailDigestAnonymousSubscription, pk)
        serializer = EmailDigestAnonymousSubscriptionDetailSerializer(emailDigestAnonymousSubscription)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emailDigestAnonymousSubscription = find(EmailDigestAnonymousSubscription, pk)
        serializer = EmailDigestAnonymousSubscriptionDetailSerializer(instance=emailDigestAnonymousSubscription,
                                                                      data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emailDigestAnonymousSubscription = find(EmailDigestAnonymousSubscription, pk)
        emailDigestAnonymousSubscription.delete()
        return Response(data={'detail': 'The email digest anonymous subscription deleted successfully.'},
                        status=status.HTTP_204_NO_CONTENT)
