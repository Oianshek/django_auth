from django.contrib import admin
from .models import *


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    pass
