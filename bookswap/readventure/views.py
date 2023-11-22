from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['login_success'] = True
            return redirect('home')  # Redirect to the congratulations page
        # else:
        #     # Handle invalid login credentials
        #     return render(request, 'readventure/index.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'readventure/index.html')

def home(request):
    if request.session.get('login_success'):
        del request.session['login_success']  # Remove the session variable to avoid showing the message on page refresh
        return render(request, 'readventure/home.html')
    else:
        # Redirect to the login page if there's no successful login session
        return redirect('index')  # Update 'user_login' with the actual name of your login view