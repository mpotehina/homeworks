import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    list_stations = []
    number = request.GET.get("page")

    with open(BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        list_stations = list(reader)

    p = Paginator(list_stations, 10)

    context = {
         'bus_stations': p.get_page(number),
         'page': p.get_page(number)
    }

    return render(request, 'stations/index.html', context)
