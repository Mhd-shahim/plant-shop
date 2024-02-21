from rest_framework.response import Response
from .models import Cart
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import AnonymousUser


@api_view(['POST'])
def add_to_cart(request):
    user = request.user
    
    if not user.is_authenticated:
        return Response({'message': 'user is not authenticated'})
    
    plant_id = request.data['plant_id']
    quantity = request.data['quantity']

    try:
        plant_in_cart = Cart.objects.get(user=user, plant_id=plant_id)
        plant_in_cart.quantity += 1
        plant_in_cart.save()
    except Cart.DoesNotExist:
        Cart.objects.create(user=user, plant_id=plant_id, quantity=quantity)

    return Response({'message':'Product added to cart successfully'}, status=status.HTTP_201_CREATED)