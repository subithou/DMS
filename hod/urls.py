from django.urls import path, include
from hod.views import hod_index, add_staff

urlpatterns = [
    path('', hod_index, name='hod_index'),
    path('add_staff/', add_staff, name='add_staff'),


]