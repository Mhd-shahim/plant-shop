from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def register(request):
    if request.method == 'POST':

        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        confirm_password = request.data['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username):
                return Response({'message':'username already exist'})
                
                
        else:
            return Response({'message':'password not matching '})