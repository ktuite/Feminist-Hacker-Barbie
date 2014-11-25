from django.contrib import admin
from .models import *

@admin.register(BarbiePage)

class BarbiePageAdmin(admin.ModelAdmin):
    pass

@admin.register(Adaptation)

class AdaptationAdmin(admin.ModelAdmin):
    pass