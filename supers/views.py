from operator import methodcaller
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Supers

@api_view(['GET'])
def supers_list(request, pk):
    if request.method == 'GET':
        supers = get_object_or_404(Supers, pk=pk)
        print(supers)
