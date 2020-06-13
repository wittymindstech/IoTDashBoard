from django.shortcuts import render
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm

@login_required
def index(request):
    return render(request, 'index.html')

def register(request):
    form_class = UserRegistrationForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']

            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/wtdash/login')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
        else:
            form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
