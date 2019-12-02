from django.contrib import admin
from .models import User,Hood,Profile

# Register your models here.
admin.site.register(User)
admin.site.register(Hood)
admin.site.register(Profile)
