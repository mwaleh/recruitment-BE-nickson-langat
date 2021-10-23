from datetime import date
from django.test import TestCase
from django.urls import reverse
from core.models import Building, HalfHourData, MeterData

# Create your tests here.
class CoreTest(TestCase):
    def setUp(self):
        self.building = Building(name='AfricanHut')
        self.building.save()
        self.timestamp = date.today()
        self.meter = MeterData(building=self.building,fuel='Water', unit='m3')
        self.meter.save()
        self.consumption=HalfHourData(meter=self.meter, consumption=56.50, uploaded_at=self.timestamp)

    def test_building_creation(self):
        building = self.building
        self.assertTrue(isinstance(building, Building))
        self.assertEqual(building.__str__(), str(building.id))
    
    def test_meter_creation(self):
        meter = self.meter
        self.assertTrue(isinstance(meter, MeterData))
        self.assertEqual(meter.__str__(), str(meter.id))

    def test_consumption_creation(self):
        consumption = self.consumption
        self.assertTrue(isinstance(consumption, HalfHourData))
        self.assertEqual(consumption.__str__(), str(consumption.id))

    def test_building_list_view(self):
        response = self.client.get(reverse('buildings'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'AfricanHut')
        self.assertTemplateUsed(response, 'home.html')

    def test_filter_options(self):
        response = self.client.get('/chart/filter-options/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'days': []}
        )
    
    def test_consumption_per_house(self):
        response = self.client.get('/chart/consumption/per/house/10/')
        self.assertEqual(response.status_code, 200)
        
