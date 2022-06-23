from typing import List
from venv import create
from django.urls import path
from .views import ListEvents, EventView, deleteEvent, createEvent

urlpatterns = [
    path('', ListEvents),
    path('<int:pk>', EventView),
    path('delete/<int:pk>', deleteEvent),
    path('create/', createEvent),
]