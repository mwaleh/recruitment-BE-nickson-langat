from django.contrib import admin

from core.models import Building, HalfHourData, MeterData

# Register your models here.

admin.site.register(Building)
admin.site.register(MeterData)
admin.site.register(HalfHourData)