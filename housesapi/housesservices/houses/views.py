from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from .models import House
from .models import Checker
from .producer import publish
from .serializers import HouseSerializer
import random


# http://localhost:8000/api/
def home(request):
    return JsonResponse({
        'message': 'Welcome to the API endpoint!'
    })


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

        print('House Created publishing... to core with Content: house_created and Data: ',
              house_serializer.data)
        publish('house_created', house_serializer.data)

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

        print('House Updated publishing... to core with Content: house_updated and Data: ',
              house_serializer.data)
        publish('house_updated', house_serializer.data)

        return Response(house_serializer.data, status=status.HTTP_202_ACCEPTED)

    # Creating the destroy action:
    def destroy(self, request, pk=None):
        house = House.objects.get(id=pk)
        house.delete()

        print(
            'House Deleted publishing... to core with Content: house_deleted, and PK: ', pk)
        publish('house_deleted', pk)

        return Response(status=status.HTTP_204_NO_CONTENT)


# Creating the Checker view:
class CheckerAPIView(APIView):

    # Creating the get method:
    def get(self, request):
        checkers = Checker.objects.all()
        if not checkers.exists():  # Check if there are any checkers
            return Response({'error': 'No checkers available'}, status=status.HTTP_404_NOT_FOUND)

        checker = random.choice(checkers)
        return Response({'id': checker.id})
