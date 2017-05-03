from django.contrib.gis import admin
from .models import WorldBorder
from .models import PayAndDisplayMachine
from .models import PayAndDisplayOutlet

admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(PayAndDisplayMachine, admin.GeoModelAdmin)
admin.site.register(PayAndDisplayOutlet, admin.GeoModelAdmin)