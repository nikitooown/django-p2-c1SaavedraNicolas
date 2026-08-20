from django.shortcuts import render

# Create your views here.
def inicio(request):
    return HttpResponse(
        "<h1>EcoEnergy</h1>"
        "<p>Back End en funcionamiento</p>"
    )
