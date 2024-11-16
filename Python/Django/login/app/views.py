from django.shortcuts import render, redirect, HttpResponse
from .models import User
import bcrypt
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        password = request.POST['password']
        re_password = request.POST['re_password']
        if password != re_password:
            messages.error(request, "Passwords do not match.", extra_tags='register')
            return redirect('/register')
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='register')
            return redirect('/register')
        else:
            User.objects.add_user(request.POST)
            messages.success(request, "Registration successful! You can now log in.", extra_tags='success')
            return redirect('/')

    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'])

        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['email'] = logged_user.email
                request.session['fname' ] = logged_user.fname
                return redirect('/profile')
            else:
                messages.error(request, "Invalid email or password", extra_tags='login')
        else:
            messages.error(request, "Invalid email or password", extra_tags='login')

        return redirect('/login')
    return render(request, 'index.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def profile(request):
    if not 'email' in request.session:
        messages.error(request, 'You must first login.', extra_tags='login')
        return redirect('/')
    return render(request, 'profile.html')
