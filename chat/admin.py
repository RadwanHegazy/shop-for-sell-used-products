from django.contrib import admin
from .models import Ask, Messages
# Register your models here.

admin.site.register(Messages)
admin.site.register(Ask)