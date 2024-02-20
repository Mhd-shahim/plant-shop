from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Banner,Category,Plant
from .serializers import BannerSerializer,CategorySerializer,PlantSerializer
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser


# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated,IsAdminUser])
def banners(request):

    if request.method == 'GET':
        banners = Banner.objects.all()
        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = BannerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Banner created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['GET','PUT', 'DELETE'])        
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated,IsAdminUser])
def bannerMethod(request,pk):
    banner = get_object_or_404(Banner, pk=pk)

    if request.method == 'GET':
        serializer = BannerSerializer(banner)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = BannerSerializer(banner, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'banner edited successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'DELETE':
        banner.delete()
        return Response({'message': 'banner deleted successfully'},status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated,IsAdminUser])
def category(request):

    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Category created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)



@api_view(['GET','PUT', 'DELETE'])   
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated,IsAdminUser])
def categoryMethod(request,pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = CategorySerializer(category, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'category edited successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'DELETE':
        category.delete()
        return Response({'message': 'category deleted successfully'},status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated,IsAdminUser])
def plants(request):

    if request.method == 'GET':
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data =request.data
        serializer = PlantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'plant created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated,IsAdminUser])
def plantMethod(request, pk):
    plant = get_object_or_404(Plant, pk=pk)

    if request.method == 'GET':
        serializer = PlantSerializer(plant)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = request.data
        serializer =PlantSerializer(plant, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message': 'plant edited successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'DELETE':
        plant.delete()
        return Response({'message': 'plant deleted successfully'}, status=status.HTTP_204_NO_CONTENT)