from django.contrib.gis.db import models

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # Auto-generated `LayerMapping` dictionary for WorldBorder model
    worldborder_mapping = {
        'fips': 'FIPS',
        'iso2': 'ISO2',
        'iso3': 'ISO3',
        'un': 'UN',
        'name': 'NAME',
        'area': 'AREA',
        'pop2005': 'POP2005',
        'region': 'REGION',
        'subregion': 'SUBREGION',
        'lon': 'LON',
        'lat': 'LAT',
        'geom': 'MULTIPOLYGON',
    }

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class PayAndDisplayMachine(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    tariff = models.FloatField(null=True)
    hours = models.TextField(null=True)
    zone = models.TextField(null=True)
    location = models.TextField(null=True)
    furtherloc = models.TextField(null=True)
    nospaces = models.TextField(null=True)
    furtherinfo = models.TextField(null=True)
    clearway = models.TextField(null=True)
    point = models.PointField(null=True)

    def __str__(self):              # __unicode__ on Python 2
        return "Co-ordinates: " + str(self.latitude) + " " + str(self.longitude) + "\n" + "Location: " + str(self.location)

class PayAndDisplayOutlet(models.Model):
    #Outlets that do Payzone/P&D Vouchers
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.TextField(null=True)
    address1 = models.TextField(null=True)
    address2 = models.TextField(null=True)
    county = models.TextField(null=True)
    point = models.PointField(null=True)

    def __str__(self):              # __unicode__ on Python 2
        return "Co-ordinates: " + str(self.latitude) + " " + str(self.longitude) + "\n" + "Location: " + str(self.name)
