import csv, io
from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import ExtractDay
from django.http import JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Building, HalfHourData, MeterData
from .charts import generate_color_palette

# Create your views here.
def index(request):
    bulding_list=Building.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(bulding_list, 10)
    try:
        buildings = paginator.page(page)
    except PageNotAnInteger:
        buildings = paginator.page(1)
    except EmptyPage:
        buildings = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'buildings':buildings})

def statistics_view(request):
    return render(request, 'statistics.html', {})

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
                building_id=column[0],
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
        messages.success('THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',',):
        try:
            _, created=HalfHourData.objects.update_or_create(
                consumption=column[0],
                meter_id=column[1],
                uploaded_at=column[2],
            )
        except ValueError:
            pass    
    return render(request, template, context)

def get_filter_options(request):
    """
    lists all the dates we have half hour records for
    """
    grouped_data = HalfHourData.objects.annotate(day=ExtractDay('uploaded_at')).values('day').order_by('day').distinct()
    options = [data['day'] for data in grouped_data]

    return JsonResponse({
        'days': options,
    })

def consumption_per_house_chart(request, day):
    labels = []
    data = []
    results = HalfHourData.objects.filter(uploaded_at__day=day)
    qs=results.values('meter__building_id__name').annotate(sum_consumption=Sum('consumption')).order_by('meter__building_id__name')
    
    for item in qs:
        labels.append(item['meter__building_id__name'])
        data.append(float(item['sum_consumption']))

    return JsonResponse({
        'title': f'Consumption per household on {day} in DEC 2018',
        'data': {
            'labels': labels,
            'datasets': [{
                'label': 'Consumption (Kwh)',
                'backgroundColor': generate_color_palette(31),
                'borderColor': generate_color_palette(5),
                ' borderWidth':1,
                'fill':False,
                'data': data,
            }]
        },
    })
