from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, UserLoginSerializer, UserConfirmationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import random


# @api_view(['POST'])
# def registration_api_view(request):
#     serializer = UserCreateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     username = serializer.validated_data.get('username')
#     email = serializer.validated_data.get('email')
#     password = serializer.validated_data.get('password')
#
#     user = User.objects.create_user(username=username, password=password, is_active=False)
#     # Create ActivationCode
#     return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED)
#
#
# @api_view(['POST'])
# def authorization_api_view(request):
#     serializer = UserLoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     username = serializer.validated_data.get('username')
#     password = serializer.validated_data.get('password')
#
#     user = authenticate(username=username, password=password)
#     if user:
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response(data={'key': token.key})
#     return Response(status=status.HTTP_401_UNAUTHORIZED,
#                     data={'error': 'User credentials are wrong!'})
#
# @api_view(['POST'])
# def confirm_api_view(request):
#     serializer = UserConfirmationSerializer(data=request.data)
#     if serializer.is_valid():
#             try:
#                 user = User.objects.get(username=serializer.validated_data['username'], confirmation_code=serializer.validated_data['confirmation_code'])
#                 user.is_active = True
#                 user.confirmation_code = ''
#                 user.save()
#                 return Response(data={'detail': 'User confirmed and activated.'}, status=status.HTTP_200_OK)
#             except User.DoesNotExist:
#                 return Response(data={'detail': 'Invalid confirmation code or username.'}, status=status.HTTP_400_BAD_REQUEST)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        user = User.objects.create_user(username=username, password=password, is_active=False)
        confirmation_code = str(random.randint(100000, 999999))
        user.profile.confirmation_code = confirmation_code
        user.profile.save()

        return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED)

class AuthorizationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error': 'User credentials are wrong!'})

class ConfirmAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserConfirmationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(username=serializer.validated_data['username'],
                                        profile__confirmation_code=serializer.validated_data['confirmation_code'])
                user.is_active = True
                user.profile.confirmation_code = ''
                user.save()
                user.profile.save()
                return Response(data={'detail': 'User confirmed and activated.'}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response(data={'detail': 'Invalid confirmation code or username.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
