from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login,logout
from rest_framework import status
from django.shortcuts import get_object_or_404




@api_view(['POST'])
def registerUser(request):
    if request.method == 'POST':

        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        
        try:
            validate_email(email)
        except ValidationError:
            return Response({'message': 'Invalid email address'})

        if password == confirm_password:
            if User.objects.filter(username=username):
                return Response({'message':'username already exist'})
            elif User.objects.filter(email=email):
                return Response({'message':'an account with same email is already exists'})  
            else:
                User.objects.create(username=username, email=email, password=password)
                return Response({'message':'user registered successfully'})
        else:
            return Response({'message':'password not matching '})


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
def loginUser(request):
    if request.method == 'POST':
        
        username = request.data.get('username')
        password = request.data.get('password')
        
        try:
            user = get_object_or_404(User, username=username, password=password)

        except :
            return Response({'message': 'user does not exist'})

        if user:
            token = get_tokens_for_user(user)
            login(request, user)
            return Response({'message': 'user logged in successfully','tokens':token},status=status.HTTP_200_OK)
        else:
            return Response({'message':'invalid credentials'})
        
@api_view(['POST'])
def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)