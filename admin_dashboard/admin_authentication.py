from django.contrib.auth import authenticate,login,logout
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['POST'])
def adminLogin(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        
        user = authenticate(username=username, password=password)
     
        if user and user.is_superuser:
            token = get_tokens_for_user(user)
            login(request, user)
            return Response({'message': 'user logged in successfully','tokens':token })
        else:
            return Response({'error': 'invalid credentials'})
        


