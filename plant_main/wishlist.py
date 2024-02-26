from rest_framework.response import Response
from .models import Wishlist
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import WishlistSerializer


@api_view(['POST'])
def add_to_wishlist(request):
    user = request.user
    plant_id = request.data['plant_id']

    try:
        plant_in_wishlist = Wishlist.objects.get(user=user, plant_id=plant_id)
        if plant_in_wishlist:
            return Response({'message':'product already in wishlist'}, status=status.HTTP_302_FOUND)
        
    except Wishlist.DoesNotExist:
        Wishlist.objects.create(user=user, plant_id=plant_id)

        return Response({'message':'plant added to wishlist successfully'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def viewWishlist(request):
    if request.method == 'GET':
        wishlist_item = Wishlist.objects.filter(user=request.user)
        seriaizer = WishlistSerializer(wishlist_item, many=True)
        return Response(seriaizer.data, status=status.HTTP_200_OK)
    

@api_view(['DELETE'])
def deleteWishlist(request, pk):
    if request.method == 'DELETE':
        try:
            wishlist_item = Wishlist.objects.get(user=request.user, plant_id=pk)
            wishlist_item.delete()
            return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Wishlist.DoesNotExist:
            return Response({'message': 'Item does not exist in the wishlist'}, status=status.HTTP_404_NOT_FOUND)
