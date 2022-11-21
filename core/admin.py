from django.contrib import admin

from core.models import Image, Project

# Register your models here.
admin.site.register(Project)
admin.site.register(Image)