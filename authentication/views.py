from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSignInSerializer, UserSignUpSerializer
from .utils import get_user_from_model
from django.http import JsonResponse
# Create your views here.

class UserSignUpView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]


    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({'refresh':str(refresh), 'access':str(refresh.access_token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSignInView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserSignInSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh), 'access':str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
def get_user_info(request):
    token = request.headers.get('Authorization').split(' ')[1]
    user, user_id = get_user_from_model(token)
    if user is not None:
        return JsonResponse({'user_id': user_id, 'username': user.username}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
    