from django.shortcuts import render

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
def login(request):
    print(request)
    return render(request,'login.html')
def news(request):
    print(request)
    return render(request,'news.html')
