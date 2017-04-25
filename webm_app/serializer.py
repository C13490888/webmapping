from rest_framework import serializers
from webm_app import models


class PayAndDisplayMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PayAndDisplayMachine
        fields = ('id', 'latitude', 'longitude', 'tariff', 'hours', 'zone', 'location', 'furtherloc', 'nospaces', 'furtherinfo', 'clearway', 'point')

class PayAndDisplayOutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PayAndDisplayOutlet
        fields = ('id', 'latitude', 'longitude', 'name', 'address1', 'address2', 'county', 'point')
