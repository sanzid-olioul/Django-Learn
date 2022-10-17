from django.shortcuts import render

# Create your views here.
from .models import Flight,Passenger,Reservation
from .serializers import FlightSerializers,PassengerSerializers,ReservationSerializers
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(departureCity=request.data['departureCity'],arrivalCity=request.data['arrivalCity'],dateOfDeparture=request.data['dateOfDeparture'])
    serializer = FlightSerializers(flights,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])

    passenger =Passenger()
    passenger.firstNmae = request.data['firstNmae']
    passenger.lastNmae = request.data['lastNmae']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    Reservation.save(reservation)

    return Response(status=status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers