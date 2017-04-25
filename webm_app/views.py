from django.shortcuts import render
from rest_framework import generics
from webm_app import models
from webm_app import serializer


class PndMachineView(generics.ListAPIView):
    model = models.PayAndDisplayMachine
    serializer_class = serializer.PayAndDisplayMachineSerializer
    queryset = models.PayAndDisplayMachine.objects.all()

#class PndMachineIdView(generics.RetrieveAPIView):

#class PndMachineLocationView:

#class PndMachinePointView:

class PndOutletView(generics.ListAPIView):
    model = models.PayAndDisplayOutlet
    serializer_class = serializer.PayAndDisplayOutletSerializer
    queryset = models.PayAndDisplayOutlet.objects.all()

#class PndOutletIdView:

#class PndOutletLocationView:

#class PndOutletPointView: