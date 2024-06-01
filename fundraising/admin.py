from django.contrib import admin

from fundraising.models import Fundraising


@admin.register(Fundraising)
class FundraisingAdmin(admin.ModelAdmin):
    list_display = ("title", "fundraiser", "created_at", "end_at")
    list_filter = ("created_at", "end_at")
    search_fields = ("title", "creator__email")
