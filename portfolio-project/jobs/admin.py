from django.contrib import admin
from .models import Job   #	 Showing error in importing the module

# Register your models here.

admin.site.register(Job)  # add a job in admin page