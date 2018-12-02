from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def landing_view(request):
    xx = ['Good_1', 'Good_2', 'Good_3']
    return render(request, 'landing/index.html', context={'names': xx})
