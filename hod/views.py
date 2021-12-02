from django.shortcuts import render

# Create your views here.
def hod_index(request):
    return render(request, 'hod_index.html')
