from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('upload/buldings', views.upload_building, name='upload-buildings'),
    path('upload/meters', views.upload_meters, name='upload-meters'),
    path('upload/hours', views.upload_hours, name='upload-hours'),
    path('consumption/chart/', views.consumption_chart, name='chart'),
]