from django.shortcuts import render


# Create your views here.
def hod_index(request):
    return render(request, 'hod_index.html')


def add_staff(request):
    return render(request, 'add_staff.html')
