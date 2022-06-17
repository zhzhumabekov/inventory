from django.urls import path, include
from . import views

app_name = 'all_data'

urlpatterns = [
    path('', views.index, name='index'),
]
