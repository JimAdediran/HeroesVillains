from operator import methodcaller
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
import super_types
from supers.serializers import SupersSerializer
from super_types.serializers import SuperTypeSerializer
from .models import Supers
from super_types.models import SuperType
from supers import serializers

@api_view(['GET', 'POST'])
def supers_list(request):
    supers = Supers.objects.all()
    custom_response_dict = {}
    super_types = SuperType.objects.all()
    if request.method == 'GET':
        super_type_name = request.query_params.get('super_type')
        print(super_type_name)
        queryset = Supers.objects.all()

        if super_type_name:
            queryset = queryset.filter(super_type__type=super_type_name)
            serializer = SupersSerializer(queryset, many=True)
            return Response(serializer.data)
        else: 
            for super_type in super_types:
                super_types = Supers.objects.filter(super_type_id=1)
                hero_serializer = SupersSerializer(super_types, many=True)
                super_types2 = Supers.objects.filter(super_type_id=2)
                villain_serializer = SupersSerializer(super_types2, many=True)
                custom_response_dict = {
                    "Heroes": hero_serializer.data,
                    "Villains": villain_serializer.data
                }
            return Response(custom_response_dict)
    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


        
        
            
    



@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(supers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


