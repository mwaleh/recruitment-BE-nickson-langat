from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='buildings'),
    path('upload/buldings', views.upload_building, name='upload-buildings'),
    path('upload/meters', views.upload_meters, name='upload-meters'),
    path('upload/hours', views.upload_hours, name='upload-hours'),
    path('chart/filter-options/', views.get_filter_options, name='chart-filter-options'),
    path('chart/consumption/per/house/<int:day>/', views.consumption_per_house_chart, name='chart-consumption-per-house'),
    path('statistics/', views.statistics_view, name='statistics'),
]