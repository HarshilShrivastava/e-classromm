from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from courses.models import courseName
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import userlogin,UserCreationForm
from django.contrib import messages


def index(request):
    return render(request, 'sample/home.html')


def Signup(request):
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'sample/signup.html', {'form': form})


def loginView(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/accounts/profile/')
        else:
            messages.error(request,'username or password not correct')
            return redirect('/accounts/login')

    return render(request, 'sample/signin.html')

@login_required
def profile(request):
    qs = courseName.objects.all().filter(created_by=request.user)
    qs1 = courseName.objects.all().filter(joined_by=request.user)
    context = {"qs": qs,
               "qs1": qs1}
    return render(request, 'sample/profile.html', context)
