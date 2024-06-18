from typing import ClassVar

from budget.models import Revenue
from django.contrib import admin


class RevenueAdmin(admin.ModelAdmin):
    """Admin interface for the Revenue model.

    Attributes:
    ----------
        readonly_fields (list[str]): Fields that are read-only in the admin interface.
        list_display (list[str]): Fields to display in the list view.
        list_filter (list[str]): Fields to filter by in the list view.
        search_fields (list[str]): Fields to search by in the list view.
        ordering (list[str]): Default ordering for the list view.
    """

    readonly_fields: ClassVar[list[str]] = [
        "id",
        "user_id",
    ]
    list_display: ClassVar[list[str]] = [
        "id",
        "user_id",
        "name",
        "amount",
        "category",
        "expiration_date",
    ]
    list_filter: ClassVar[list[str]] = [
        "user_id",
        "category",
    ]
    search_fields: ClassVar[list[str]] = [
        "id",
        "name",
        "amount",
    ]
    ordering: ClassVar[list[str]] = [
        "user_id",
        "expiration_date",
        "category",
        "name",
    ]
    fields: ClassVar[list[str]] = [
        "id",
        "user_id",
        "name",
        "description",
        "amount",
        "expiration_date",
        "paid",
        "payment_date",
        "category",
    ]

    class Meta:
        """Meta class for RevenueAdmin."""

        model = Revenue
        fields = "__all__"


admin.site.register(Revenue, RevenueAdmin)
