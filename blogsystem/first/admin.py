from django.contrib import admin

# Register your models here.
from .models import Login, reg
admin.site.register(reg)
admin.site.register(Login)