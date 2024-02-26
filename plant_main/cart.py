from rest_framework.response import Response
from .models import Cart
from rest_framework.decorators import api_view
from rest_framework import status
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
        if plant_in_cart:
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
    

@api_view(['DELETE'])
def deleteCart(request,pk):
    if request.method == 'DELETE':
        cart_item = Cart.objects.get(user=request.user, plant_id=pk)
        print(cart_item)
        cart_item.delete()
        return Response({'message':'item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def update_cart_item_quantity(request):
    if request.method == 'POST':
        data = request.data
        cart_item_id = data.get('cart_item_id')
        action = data.get('action')

        try:
            cart_item = Cart.objects.get(id=cart_item_id)
            if action == 'increment':
                cart_item.quantity += 1
            elif action == 'decrement':
                if cart_item.quantity > 1:
                    cart_item.quantity -= 1

                else:
                    cart_item.delete()
                    return Response({'message' : 'Cart item removed successfully'}, status=status.HTTP_204_NO_CONTENT)
            
            cart_item.save()
            serializer = CartSerializer(cart_item, many=True)
            return Response(serializer.data)
        except :
            return Response({'error': 'cart item not found'}, status=status.HTTP_404_NOT_FOUND)