from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Plant
from admin_dashboard.serializers import PlantSerializer
from rest_framework.response import Response


# Create your views here.

@api_view(['POST'])
def plantSearch(request):
    if request.method == 'POST':

        query = request.query_params.get('search', '')
        
        if query:
            plants = Plant.objects.filter(name__icontains=query)
        else:
            plants = Plant.objects.all()
        
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)


    
