from django.contrib import admin
from . models import Projects

@admin.register(Projects)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'responsible']
