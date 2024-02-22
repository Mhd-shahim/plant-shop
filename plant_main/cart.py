from rest_framework.response import Response
from .models import Cart
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import AnonymousUser
from .serializers import CartSerializer


@api_view(['POST'])
def add_to_cart(request):
    user = request.user
    
    if not user.is_authenticated:
        return Response({'message': 'user is not authenticated'})
    
    plant_id = request.data['plant_id']
    quantity = request.data['quantity']

    try:
        plant_in_cart = Cart.objects.get(user=user, plant_id=plant_id)
        #plant_in_cart.quantity += quantity
        #plant_in_cart.save()
        return Response({'message':'product already in cart'})
    except Cart.DoesNotExist:
        Cart.objects.create(user=user, plant_id=plant_id, quantity=quantity)

    return Response({'message':'Product added to cart successfully'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def viewCart(request):
    if request.method == 'GET':
        cart_items = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)