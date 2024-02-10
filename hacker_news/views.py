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


class AccountCustomUserListView(APIView):

    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        accounts = AccountCustomUser.objects.all()
        serializer = AccountCustomUserListSerializer(accounts, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AccountCustomUserDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response


class AccountCustomUserDetailView(APIView):

    def get(self, request, pk):
        account = find(AccountCustomUser, pk)
        serializer = AccountCustomUserDetailSerializer(account)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        account = find(AccountCustomUser, pk)
        serializer = AccountCustomUserDetailSerializer(instance=account, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        account = find(AccountCustomUser, pk)
        account.delete()
        return Response(data={'detail': 'The user deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class AccountsInvitationListView(APIView):

    def get(self, request):
        invitations = AccountsInvitation.objects.all()
        serializer = AccountsInvitationListSerializer(invitations, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AccountsInvitationDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountsInvitationDetailView(APIView):

    def get(self, request, pk):
        invitation = find(AccountsInvitation, pk)
        serializer = AccountsInvitationDetailSerializer(invitation)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        invitation = find(AccountsInvitation, pk)
        serializer = AccountsInvitationDetailSerializer(instance=invitation, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        invitation = find(AccountsInvitation, pk)
        invitation.delete()
        return Response(data={'detail': 'The invitation deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class AccountsEmailVerificationListView(APIView):

    def get(self, request):
        accountsEmailVerification = AccountsEmailVerification.objects.all()
        serializer = AccountsEmailVerificationListSerializer(accountsEmailVerification, many=True,
                                                             context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AccountsEmailVerificationDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountsEmailVerificationDetailView(APIView):

    def get(self, request, pk):
        accountsEmailVerification = find(AccountsEmailVerification, pk)
        serializer = AccountsEmailVerificationDetailSerializer(accountsEmailVerification)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        accountsEmailVerification = find(AccountsEmailVerification, pk)
        serializer = AccountsEmailVerificationDetailSerializer(instance=accountsEmailVerification, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        accountsEmailVerification = find(AccountsEmailVerification, pk)
        accountsEmailVerification.delete()
        return Response(data={'detail': 'The account Email verification deleted successfully.'},
                        status=status.HTTP_205_RESET_CONTENT)


class AccountPasswordResetRequestListView(APIView):

    def get(self, request):
        accountPasswordResetRequest = AccountPasswordResetRequest.objects.all()
        serializer = AccountPasswordResetRequestSerializer(accountPasswordResetRequest, many=True,
                                                           context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AccountPasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountPasswordResetRequestDetailView(APIView):

    def get(self, request, pk):
        accountPasswordResetRequest = find(AccountPasswordResetRequest, pk)
        serializer = AccountPasswordResetRequestSerializer(accountPasswordResetRequest)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        accountPasswordResetRequest = find(AccountPasswordResetRequest, pk)
        serializer = AccountPasswordResetRequestSerializer(instance=accountPasswordResetRequest, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        accountPasswordResetRequest = find(AccountPasswordResetRequest, pk)
        accountPasswordResetRequest.delete()
        return Response(data={'detail': 'The account password rest request deleted successfully.'},
                        status=status.HTTP_205_RESET_CONTENT)


class AuthPermissionListView(APIView):

    def get(self, request):
        authPermission = AuthPermission.objects.all()
        serializer = AuthPermissionListSerializer(authPermission, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AuthPermissionDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthPermissionDetailView(APIView):

    def get(self, request, pk):
        authPermission = find(AuthPermission, pk)
        serializer = AuthPermissionDetailSerializer(authPermission)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        authPermission = find(AuthPermission, pk)
        serializer = AuthPermissionDetailSerializer(instance=authPermission, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        authPermission = find(AuthPermission, pk)
        authPermission.delete()
        return Response(data={'detail': 'The auth permission deleted successfully.'})


class AuthGroupListView(APIView):

    def get(self, request):
        authGroup = AuthGroup.objects.all()
        serializer = AuthGroupSerializer(authGroup, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AuthGroupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthGroupDetailView(APIView):

    def get(self, request, pk):
        authGroup = find(AuthGroup, pk)
        serializer = AuthGroupSerializer(authGroup)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        authGroup = find(AuthGroup, pk)
        serializer = AuthGroupSerializer(instance=authGroup, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        authGroup = find(AuthGroup, pk)
        authGroup.delete()
        return Response(data={'detail': 'the auth group deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
