from django.contrib import admin

from .models import CategoryModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("icon", "name", "type", "color", "user", "is_system")
    list_filter = ("type", "color")
    search_fields = ("name", "description", "user__username")
    list_select_related = ("user",)
    ordering = ("type", "name")
    autocomplete_fields = ("user",)

    @admin.display(boolean=True, description="سیستمی")
    def is_system(self, obj):
        return obj.user_id is None