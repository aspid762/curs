from django.shortcuts import render

#from . import 
def index(request):
    return render(request,'base.html')
def dash(request):
    return render(request,'index.html')