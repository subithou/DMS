from django.urls import path, include
from hod.views import hod_index


urlpatterns = [
    path('', hod_index, name='hod_index'),

]