from django.shortcuts import render
from rest_framework import generics
from webm_app import models
from webm_app import serializer
from rest_framework import filters
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance


class PndMachineView(generics.ListAPIView):
    model = models.PayAndDisplayMachine
    serializer_class = serializer.PayAndDisplayMachineSerializer
    queryset = models.PayAndDisplayMachine.objects.all()

class PndMachineIdView(generics.RetrieveAPIView):
    model = models.PayAndDisplayMachine
    serializer_class = serializer.PayAndDisplayMachineSerializer
    queryset = models.PayAndDisplayMachine.objects.all()

class PndMachineLocationView(generics.ListAPIView):
    queryset = models.PayAndDisplayMachine.objects.all()
    serializer_class = serializer.PayAndDisplayMachineSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('location','furtherloc',)

class PndMachinePointView(generics.ListAPIView):
    serializer_class = serializer.PayAndDisplayMachineSerializer
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = models.PayAndDisplayMachine.objects.all()
        radius = int(self.request.query_params.get('radius', None))
        latitude = float(self.request.query_params.get('latitude', None))
        longitude = float(self.request.query_params.get('longitude', None))
        point = Point(longitude,latitude)
        if latitude and longitude is not None:
            queryset = models.PayAndDisplayMachine.objects.filter(point__distance_lt=(point, Distance(km=radius)))
        return queryset


class PndOutletView(generics.ListAPIView):
    model = models.PayAndDisplayOutlet
    serializer_class = serializer.PayAndDisplayOutletSerializer
    queryset = models.PayAndDisplayOutlet.objects.all()

class PndOutletIdView(generics.RetrieveAPIView):
    model = models.PayAndDisplayOutlet
    serializer_class = serializer.PayAndDisplayOutletSerializer
    queryset = models.PayAndDisplayOutlet.objects.all()

class PndOutletLocationView(generics.ListAPIView):
    queryset = models.PayAndDisplayOutlet.objects.all()
    serializer_class = serializer.PayAndDisplayOutletSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('address1', 'address2',)

#class PndOutletPointView: