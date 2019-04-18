from django.urls import path
from django.contrib.auth import views as adminviews

from . import views

urlpatterns = [
    path('', views.task1, name='task1'),
    path('task2', views.task2, name='task2'),
    path('task3', views.task3, name='task3'),
    path('last5games', views.last5games, name='last5games'),
    path('todaysgames', views.todaysgames, name='todaysgames'),
]

