from django.shortcuts import render
from polls.models import My_car


def prediction2(request):
    last_brake = My_car.objects.last()
    return render(request, 'polls/last.html', {'last_brake': last_brake})
