from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from decouple import config
# Create your views here.


def index(request):
    API_KEY = config('WEATHER_API')
    print(type(API_KEY))
    print(API_KEY)
    st = 'api.openweathermap.org/data/2.5/weather?q={city name}&appid='
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('home')
        else:
            messages.info(request, 'Incorrect Username or Password')
            return HttpResponseRedirect('login')

    return render(request,'login.html')

# logout function

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username = username).exists():  #check user already exists in the database.
            messages.info(request, 'Username Already Taken!')
            return HttpResponseRedirect('signup')
        if User.objects.filter(email = email).exists():
            messages.info(request, 'Email Already Taken!')
            return HttpResponseRedirect('signup')
        else:
            user = User.objects.create_user(username = username, password = password, email = email,first_name = first_name, last_name = last_name)
            user.save()
            return HttpResponseRedirect('login')

    return render(request, 'signup.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')