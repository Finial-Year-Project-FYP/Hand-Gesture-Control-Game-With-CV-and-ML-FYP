from django.shortcuts import render
from polls.models import My_car


def history(request):
    player_data = My_car.objects.all()
    return render(request, 'polls/history.html', {'player_data': player_data})
