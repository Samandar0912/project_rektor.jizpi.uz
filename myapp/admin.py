from django.contrib import admin
from .models import ApplicationType, Gender, Post, Region

# Register your models here.

admin.site.register(ApplicationType)
admin.site.register(Gender)
admin.site.register(Post)
admin.site.register(Region)
