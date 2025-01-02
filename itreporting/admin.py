from django.contrib import admin
from .models import Issue, Module
# from .models import Profile
# admin.site.register(Profile)
# Register your models here.
admin.site.register(Issue)
admin.site.register(Module)