from django.contrib import admin

from django.contrib import admin
from .models import *


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    pass
