from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.new),
    path("counter",views.counter,name='counter')
]