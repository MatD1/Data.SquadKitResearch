from django.contrib import admin
from .models import British, Post, Insurgent
# Register your models here.
admin.site.register(Post)
admin.site.register(Insurgent)
admin.site.register(British)