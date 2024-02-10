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


class DjangoContentTypeListView(APIView):

    def get(self, request):
        djangoContentType = DjangoContentType.objects.all()
        serializer = DjangoContentTypeSerializer(djangoContentType, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DjangoContentTypeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DjangoContentTypeDetailView(APIView):

    def get(self, request, pk):
        djangoContentType = find(DjangoContentType, pk)
        serializer = DjangoContentTypeSerializer(djangoContentType)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        djangoContentType = find(DjangoContentType, pk)
        serializer = DjangoContentTypeSerializer(instance=djangoContentType, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        djangoContentType = find(DjangoContentType, pk)
        djangoContentType.delete()
        return Response(data={'detail': 'The django content type deleted successfully.'},
                        status=status.HTTP_204_NO_CONTENT)


class DjangoAdminLogListView(APIView):

    def get(self, request):
        djangoAdminLog = DjangoAdminLog.objects.all()
        serializer = DjangoAdminLogListSerializer(djangoAdminLog, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DjangoAdminLogDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DjangoAdminLogDetailView(APIView):

    def get(self, request, pk):
        djangoAdminLog = find(DjangoAdminLog, pk)
        serializer = DjangoAdminLogDetailSerializer(djangoAdminLog)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        djangoAdminLog = find(DjangoAdminLog, pk)
        serializer = DjangoAdminLogDetailSerializer(instance=djangoAdminLog, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        djangoAdminLog = find(DjangoAdminLog, pk)
        djangoAdminLog.delete()
        return Response(data={'detail': 'The django admin log deleted successfully.'})
