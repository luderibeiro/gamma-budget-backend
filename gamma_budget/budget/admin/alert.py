from typing import ClassVar

from budget.models.alert import Alert
from django.contrib import admin


class AlertAdmin(admin.ModelAdmin):
    """
    Alert admin class.
    """

    list_display: ClassVar[list[str]] = [
        "user_id",
        "revenue",
        "message",
        "alert_date",
        "created_at",
    ]
    list_filter: ClassVar[list[str]] = [
        "user_id",
        "revenue",
    ]
    search_fields: ClassVar[list[str]] = [
        "user_id",
        "revenue",
        "message",
        "alert_date",
        "created_at",
    ]
    ordering: ClassVar[list[str]] = [
        "user_id",
        "alert_date",
    ]
    readonly_fields: ClassVar[list[str]] = [
        "id",
        "created_at",
    ]
    fields: ClassVar[list[str]] = [
        "id",
        "user_id",
        "revenue",
        "message",
        "alert_date",
        "created_at",
    ]


admin.site.register(Alert, AlertAdmin)
