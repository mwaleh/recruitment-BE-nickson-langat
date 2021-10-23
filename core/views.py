import csv, io
from django.shortcuts import redirect, render
from django.db.models import Count, F, Sum, Avg
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay
from django.http import JsonResponse
from django.contrib import messages
from .models import Building, HalfHourData, MeterData

# Create your views here.
def index(request):
    buldings=Building.objects.all()
    context={
        'buildings':buldings
    }
    return render(request, 'home.html', context)

def upload_building(request):
    template = "upload_buildings.html"
    context = {
        'order': 'Order of the CSV should be id,name',
              }

    if request.method == "GET":
        return render(request, template, context)
    csv_file = request.FILES['file']
    print(csv_file.name)
    if not csv_file.name.endswith('.csv'):
        messages.success(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',',):
        try:
            _, created=Building.objects.update_or_create(
                id=column[0],
                name=column[1],
            )
        except ValueError:
            pass    
    return render(request, template, context)


def upload_meters(request):
    template = "upload_meters.html"

    context = {
        'order': 'Order of the CSV should be building_id,id,fuel,unit',
              }

    if request.method == "GET":
        return render(request, template, context)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.success(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',',):
        try:
            _, created=MeterData.objects.update_or_create(
                bulding_id_id=column[0],
                id=column[1],
                fuel=column[2],
                unit=column[3]
            )
        except ValueError:
            pass    
    return render(request, template, context)


def upload_hours(request):
    template = "upload_hours.html"
    context = {
        'order': 'Order of the CSV should be consumption,meter_id,reading_date_time'
    }

    if request.method == "GET":
        return render(request, template, context)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.success(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',',):
        try:
            _, created=HalfHourData.objects.update_or_create(
                consumption=column[0],
                meter_id_id=column[1],
                reading_date_time=column[2],
            )
        except ValueError:
            pass    
    return render(request, template, context)


def pie_chart(request):
    labels = []
    data = []
    # queryset=HalfHourData.objects.all()[:9]
    
    qs = HalfHourData.objects.values('meter_id__bulding_id__name').annotate(sum_consumption=Sum('consumption')).order_by('meter_id__bulding_id__name')[:25]
    
    # qs=queryset.annotate(day=ExtractDay('reading_date_time'))\
    #      .values('day').annotate(total=Sum('consumption')).values('day', 'total').order_by('day')
   
    # for x in qs:
    #     labels.append(x['day'])
    #     data.append(float(x['total']))

    for x in qs:
        labels.append(x['meter_id__bulding_id__name'])
        data.append(float(x['sum_consumption']))
        
    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })

def stats(request):
    return render(request, 'statistics.html')

colorPalette = ['#00ccff ', '#ff33cc', '#ff0066', '#00ffcc', '#290066', '#ff3300', '#ffff00']
colorPrimary, colorSuccess, colorDanger = '#79aec8', colorPalette[0], colorPalette[5]

def generate_color_palette(amount):
    palette = []

    i = 0
    while i < len(colorPalette) and len(palette) < amount:
        palette.append(colorPalette[i])
        i += 1
        if i == len(colorPalette) and len(palette) < amount:
            i = 0

    return palette