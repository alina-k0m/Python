from django.contrib import admin

# Register your models here.
from .models import Option, Riddle

admin.site.register(Riddle)
admin.site.register(Option)
