from django.contrib import admin

from .models import CarInsightCache


@admin.register(CarInsightCache)
class CarInsightCacheAdmin(admin.ModelAdmin):
    list_display = ("year", "make", "model", "updated_at")
