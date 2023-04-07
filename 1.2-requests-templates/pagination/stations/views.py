from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

# from .models import BusStantions


def index(request):
    return redirect(reverse('bus_stations'))

# class BusStantion(ListView):
#     model = BusStantions

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open('data-398-2018-08-30.csv', newline='', encoding='utf8') as f:
        stantions = []
        f_reader = csv.DictReader(f)
        stantion = []
        for row in f_reader:
            stantions.append(row.items())
        for lst in stantions:
            stantion = list(lst)

        page_number = int(request.GET.get("page", 1))
        paginator = Paginator(stantion, 10)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': paginator,
            'page': page,
        }
    return render(request, 'stations/index.html', context)

    bus_stationstions('bus_stations/')