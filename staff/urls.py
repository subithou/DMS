from django.urls import path, include
from staff.views import staff_index


urlpatterns = [
    path('', staff_index, name='student_index'),

]