from budget.models.limit import Limit
from django.contrib import admin


class LimitAdmin(admin.ModelAdmin):
    """
    Limit admin class.
    """

    list_display = ("user", "limit", "amount", "limit_date", "category", "created_at")
    search_fields = ("user", "limit", "amount", "limit_date", "category", "created_at")
    readonly_fields = ("created_at",)
    list_filter = ("user", "limit_date", "category", "created_at")


admin.site.register(Limit, LimitAdmin)
