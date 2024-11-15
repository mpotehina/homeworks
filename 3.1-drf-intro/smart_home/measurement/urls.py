from django.contrib.redirects import admin
from django.urls import path

from .views import SensorsView, SensorUpdate, MeasurementsUpdate

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementsUpdate.as_view()),
]
