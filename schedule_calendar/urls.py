from django.contrib import admin
from django.urls import path

from schedule_calendar import views

urlpatterns = [
    path('', views.home_view),
]
