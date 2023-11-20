from django.shortcuts import render

from django.contrib.auth import authenticate, login
#from . import 

def index(request):
    return render(request,'base.html')
def dash(request):
    return render(request,'index.html')
def content(request):
    return render(request,'content.html')

def about(request):
    return render(request,'about.html')
def contacts(request):
    print(request)
    return render(request,'contacts.html')

def login_news(request):
    for key, value in request.POST.items():
        print(f'Key: {key}')
        print(f'Value: {value}')
    # username = request.POST["username"]
    # password = request.POST["password"]
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     # Redirect to a success page.
    #     return render(request,'news.html')
    # else:
    #     # Return an 'invalid login' error message.    
    return render(request,'login.html')

def news(request):
    print(request)
    return render(request,'news.html')

def register(request):
    return render(request,'register.html')
def reset(request):
    return render(request,'reset.html')
def profile(request):
    return render(request,'profile.html')