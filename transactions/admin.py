from django.contrib import admin
from .models import TransactionModel


@admin.register(TransactionModel)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "category", "type", "amount", "date", "created_at")
    list_filter = ("type", "category", "date")
    search_fields = ("user__username", "note")
    ordering = ("-date", "-id")
    readonly_fields = ("created_at",)