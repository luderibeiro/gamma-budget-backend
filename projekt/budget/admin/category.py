from budget.models import IncomingCategory, RevenueCategory
from django.contrib import admin


class IncomingCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
    ]
    search_fields = [
        "name",
        "description",
    ]
    ordering = [
        "name",
    ]


class RevenueCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
    ]
    search_fields = [
        "name",
        "description",
    ]
    ordering = [
        "name",
    ]


admin.site.register(IncomingCategory, IncomingCategoryAdmin)
admin.site.register(RevenueCategory, RevenueCategoryAdmin)
