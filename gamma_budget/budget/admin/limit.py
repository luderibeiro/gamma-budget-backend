from typing import ClassVar

from budget.models.limit import Limit
from django.contrib import admin


class LimitAdmin(admin.ModelAdmin):
    """Limit admin class."""

    list_display: ClassVar[list[str]] = [
        "id",
        "category",
        "user_id",
        "limit",
        "amount",
    ]
    list_filter: ClassVar[list[str]] = [
        "user_id",
        "category",
    ]
    search_fields: ClassVar[list[str]] = [
        "id",
        "user_id",
    ]
    ordering: ClassVar[list[str]] = [
        "user_id",
        "limit_date",
    ]
    readonly_fields: ClassVar[list[str]] = [
        "id",
    ]
    fields: ClassVar[list[str]] = [
        "id",
        "user_id",
        "limit",
        "amount",
        "limit_date",
        "category",
    ]


admin.site.register(Limit, LimitAdmin)
