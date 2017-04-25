import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder
from .models import PayAndDisplayMachine
from .models import PayAndDisplayOutlet
import json
from django.contrib.gis.geos import Point
world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'TM_WORLD_BORDERS-0.3.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        WorldBorder, world_shp, world_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)

def load_machines():
    machines = open('webm_app/data/dccrdpandd.geojson')
    machines_clearway = open('webm_app/data/dccrdpanddclway.geojson')

    data1 = json.load(machines)
    data2 = json.load(machines_clearway)

    for machine in data1['features']:
        longitude = float(machine['properties']['Longitude'])
        latitude = float(machine['properties']['Latitude'])
        tariff = machine['properties']['Tariff']
        hours = machine['properties']['Hours_of_Operation']
        zone = machine['properties']['Zone']
        location = machine['properties']['Location']
        furtherloc = machine['properties']['Exact_Location']
        nospaces = machine['properties']['No_Spaces']
        furtherinfo = machine['properties']['Further_Information']
        clearway = machine['properties']['Clr_Way']
        point = Point(longitude,latitude)
        print(longitude)
        print(latitude)
        print(location)
        PayAndDisplayMachine.objects.create(longitude=longitude,latitude=latitude,tariff=tariff,hours=hours,zone=zone,location=location,furtherloc=furtherloc,nospaces=nospaces,furtherinfo=furtherinfo,clearway=clearway,point=point)


    for machine in data2['features']:
        longitude = float(machine['properties']['Longitude'])
        latitude = float(machine['properties']['Latitude'])
        tariff = machine['properties']['Tariff']
        hours = machine['properties']['Hours_of_Operation']
        zone = machine['properties']['Zone']
        location = machine['properties']['Location']
        furtherloc = machine['properties']['Exact_Location']
        nospaces = machine['properties']['No_Spaces']
        furtherinfo = machine['properties']['Further_Information']
        clearway = machine['properties']['Clr_Way']
        point = Point(longitude,latitude)
        print(longitude)
        print(latitude)
        print(location)
        PayAndDisplayMachine.objects.create(longitude=longitude,latitude=latitude,tariff=tariff,hours=hours,zone=zone,location=location,furtherloc=furtherloc,nospaces=nospaces,furtherinfo=furtherinfo,clearway=clearway,point=point)


def load_outlets():
    outlets = open('webm_app/data/dccrdpanddoutlets.geojson')
    data = json.load(outlets)

    for outlet in data['features']:
        longitude = float(outlet['properties']['Longitude'])
        latitude = float(outlet['properties']['Latitude'])
        name = outlet['properties']['Name']
        address1 = outlet['properties']['Address_1']
        address2 = outlet['properties']['Address_2']
        county = outlet['properties']['County']
        point = Point(longitude,latitude)
        PayAndDisplayOutlet.objects.create(latitude=latitude,longitude=longitude,name=name,address1=address1,address2=address2,county=county,point=point)

