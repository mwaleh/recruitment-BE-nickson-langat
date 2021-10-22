from django.db import models

# Create your models here.

class Building(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self) -> str:
        return str(self.id)
    @property
    def meters(self):
        results=MeterData.objects.filter(bulding_id=self.id)
        return results

class MeterData(models.Model):
    bulding_id=models.ForeignKey(Building, on_delete=models.CASCADE)
    fuel=models.CharField(max_length=250)
    unit=models.CharField(max_length=250)

    def __str__(self) -> str:
        return str(self.id)

class HalfHourData(models.Model):
    consumption=models.DecimalField(decimal_places=2, max_digits=9)
    meter_id=models.ForeignKey(MeterData, on_delete=models.CASCADE)
    reading_date_time=models.DateTimeField()

    def __str__(self) -> str:
        return str(self.id)