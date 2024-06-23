from budget.models.alert import Alert
from django.contrib import admin


class AlertAdmin(admin.ModelAdmin):
    """
    Alert admin class.
    """

    list_display = ("user", "message", "alert_date", "created_at")
    search_fields = ("user", "message", "alert_date", "created_at")
    readonly_fields = ("created_at",)
    list_filter = ("user", "alert_date", "created_at")


admin.site.register(Alert, AlertAdmin)
