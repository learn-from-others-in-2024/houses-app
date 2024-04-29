from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import House
from .models import Checker
from .serializers import HouseSerializer
import random


# Creating the House view:
class HouseViewSet(viewsets.ViewSet):

    # Creating the list action:
    def list(self, request):
        houses = House.objects.all()
        houses_serializer = HouseSerializer(houses, many=True)
        return Response(houses_serializer.data)

    # Creating the create action:
    def create(self, request):
        house_serializer = HouseSerializer(data=request.data)
        house_serializer.is_valid(raise_exception=True)
        house_serializer.save()
        return Response(house_serializer.data, status=status.HTTP_201_CREATED)

    # Creating the retrieve action:
    def retrieve(self, request, pk=None):
        house = House.objects.get(id=pk)
        house_serializer = HouseSerializer(house)
        return Response(house_serializer.data)

    # Creating the update action:
    def update(self, request, pk=None):
        house = House.objects.get(id=pk)
        house_serializer = HouseSerializer(instance=house, data=request.data)
        house_serializer.is_valid(raise_exception=True)
        house_serializer.save()
        return Response(house_serializer.data, status=status.HTTP_202_ACCEPTED)

    # Creating the destroy action:
    def destroy(self, request, pk=None):
        house = House.objects.get(id=pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Creating the Checker view:
class CheckerAPIView(APIView):

    # Creating the get method:
    def get(self, request):
        checkers = Checker.objects.all()
        checker = random.choice(checkers)
        return Response({
            'id': checker.id
        })
