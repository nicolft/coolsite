from django.contrib import admin

# Register your models here.
from .models import CommType, CommReq

admin.site.register(CommType)
admin.site.register(CommReq)