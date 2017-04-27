from django.shortcuts import render
from rest_framework import generics
from webm_app import models
from webm_app import serializer
from rest_framework import filters


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

#class PndMachinePointView:

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