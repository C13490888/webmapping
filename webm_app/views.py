from django.shortcuts import render
from rest_framework import generics
from webm_app import models
from webm_app import serializer


class PndMachineView(generics.ListAPIView):
    model = models.PayAndDisplayMachine
    serializer_class = serializer.PayAndDisplayMachineSerializer
    queryset = models.PayAndDisplayMachine.objects.all()

class PndMachineIdView(generics.RetrieveAPIView):
    model = models.PayAndDisplayMachine
    serializer_class = serializer.PayAndDisplayMachineSerializer
    queryset = models.PayAndDisplayMachine.objects.all()

class PndMachineLocationView(generics.ListAPIView):
    model = models.PayAndDisplayMachine
    serializer_class = serializer.PayAndDisplayMachineSerializer

    def get_queryset(self):
        location = self.kwargs('location')
        return models.PayAndDisplayMachine.objects.filter(location__contains=location)

#class PndMachinePointView:

class PndOutletView(generics.ListAPIView):
    model = models.PayAndDisplayOutlet
    serializer_class = serializer.PayAndDisplayOutletSerializer
    queryset = models.PayAndDisplayOutlet.objects.all()

class PndOutletIdView(generics.RetrieveAPIView):
    model = models.PayAndDisplayOutlet
    serializer_class = serializer.PayAndDisplayOutletSerializer
    queryset = models.PayAndDisplayOutlet.objects.all()

'''class PndOutletLocationView(generics.ListAPIView):
    model = models.PayAndDisplayOutlet
    serializer_class = serializer.PayAndDisplayOutletSerializer

    def get_queryset(self):
        location = self.kwargs('location')
        return models.PayAndDisplayOutlet.objects.filter(location__contains=location)
'''
#class PndOutletPointView: