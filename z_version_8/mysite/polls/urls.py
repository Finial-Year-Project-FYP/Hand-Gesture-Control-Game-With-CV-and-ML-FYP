from django.urls import path

from polls.Views import statistic, prediction2,  project, home, history, performance

urlpatterns = [
    path('', home.home, name='home'),
    # path('index/', index.index, name='index'),
    path('performance/', performance.performance, name='performance'),
    path('pro/', project.project, name='pro'),
    path('statistic/', statistic.statistic, name='statistic'),
    path('history/', history.history, name='history'),

    # path('pred2/', prediction2.prediction2, name='pred2'),
]
