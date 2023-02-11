from django.contrib import admin
from .models import Ngos

# Register your models here.

class NgosAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ngos,NgosAdmin)