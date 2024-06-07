from typing import ClassVar

from budget.models import Incoming
from django.contrib import admin


class IncomingAdmin(admin.ModelAdmin):
    """Admin interface for the Incoming model.

    Attributes:
    ----------
        list_display (list[str]): Fields to display in the list view.
        list_filter (list[str]): Fields to filter by in the list view.
        search_fields (list[str]): Fields to search by in the list view.
        ordering (list[str]): Default ordering for the list view.
    """

    list_display: ClassVar[list[str]] = [
        "id",
        "user_id",
        "name",
        "amount",
        "category",
        "launch_date",
    ]
    list_filter: ClassVar[list[str]] = [
        "user_id",
        "category",
    ]
    search_fields: ClassVar[list[str]] = [
        "id",
        "user_id",
        "name",
        "description",
    ]
    ordering: ClassVar[list[str]] = [
        "user_id",
        "launch_date",
    ]
    readonly_fields: ClassVar[list[str]] = [
        "id",
        # "launch_date",
    ]
    fields: ClassVar[list[str]] = [
        "id",
        "user_id",
        "name",
        "description",
        "amount",
        "launch_date",
        # "incoming_date",
        "category",
    ]


admin.site.register(Incoming, IncomingAdmin)
