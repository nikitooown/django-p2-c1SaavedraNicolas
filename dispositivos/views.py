from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def inicio(request):
    return HttpResponse(
        "<h1>EcoEnergy</h1>"
        "<p>Back End en funcionamiento</p>"
)
