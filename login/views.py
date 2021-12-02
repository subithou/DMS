from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

import hod.views
import home_page.views
import staff.views
import student.views
from login.form import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from login.models import login_table


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user1 = login_table.objects.filter(username=username, password=password, category='student', status=1)
        user2 = login_table.objects.filter(username=username, password=password, category='staff', status=1)
        user3 = login_table.objects.filter(username=username, password=password, category='hod', status=1)

        if user1:
            return redirect(student.views.student_index)
        elif user2:
            return redirect(staff.views.staff_index)
        elif user3:
            return redirect(hod.views.hod_index)
        else:
            messages.error(request, 'username or password not correct')
            return redirect('login')


        # if user.is_active:
        # return redirect(student.views.student_index)

    return render(request, 'login.html')
