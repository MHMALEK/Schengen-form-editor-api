from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions

from .models import Account
from django.http import HttpResponse, JsonResponse
import json
from . import services
from django.views.decorators.csrf import csrf_exempt
from user.serializers import UserSerializer
from rest_framework.authentication import (
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from .serializers import AccountCreateSerializer, AccountListSerializer, AccountUpdateSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the Account index.")


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = AccountCreateSerializer(data=request.data)
    if serializer.is_valid():
        services.create_account(request.user, serializer.validated_data)
        return HttpResponse("Account created successfully")
    else:
        return JsonResponse(serializer.errors, status=400)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list(request):
    accounts = Account.objects.filter(user=request.user)
    serializer = AccountListSerializer(accounts, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_account(request, account_id):
    try:
        account = Account.objects.get(id=account_id, user=request.user)
    except Account.DoesNotExist:
        return Response({"error": "Account not found."}, status=404)

    serializer = AccountListSerializer(account)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_account(request, account_id):
    try:
        account = Account.objects.get(id=account_id, user=request.user)
    except Account.DoesNotExist:
        return Response({"error": "Account not found."}, status=404)

    serializer = AccountUpdateSerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_account(request, account_id):
    try:
        account = Account.objects.get(id=account_id, user=request.user)
    except Account.DoesNotExist:
        return Response({"error": "Account not found."}, status=404)

    account.delete()
    return Response({"message": "Account deleted successfully."})
