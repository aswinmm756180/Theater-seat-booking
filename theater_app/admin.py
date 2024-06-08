from django.contrib import admin
from .models import *  # Import your models here

# Register your models here
admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Theater)
