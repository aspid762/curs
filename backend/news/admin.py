from django.contrib import admin

# Register your models here.

#from .models import 
from django.contrib import admin
from .models import News

admin.site.register(News)