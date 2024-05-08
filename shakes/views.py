from django.shortcuts import render

from . serializers import DrinkSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . models import Drink

# Create your views here.


@api_view(['GET', 'POST'])
def shakes(request, format=None):

    if request.method == 'GET':
        # get all the datas
        shakes = Drink.objects.all()

        # serialize them
        serializer = DrinkSerializer(shakes, many=True)

        # return json
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def details(request, pk, format=None):

    try:
        drink = Drink.objects.get(id=pk)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
