

# Create your views here.from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, HttpResponse

from .forms import CustomUserCreationForm

# Create your views here.



from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Create and save User object
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        # Additional processing or redirection after successful registration

    # Render registration template
        return redirect('login')
    else:
        return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        # Process login form data and authenticate user
        # Use Django's authentication mechanisms
        # For example:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create_blog_post')
        else:
            # Handle invalid login credentials
            return HttpResponse('Incorrect User-Id or Password')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

        
        

