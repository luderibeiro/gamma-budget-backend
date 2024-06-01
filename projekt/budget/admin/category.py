from typing import ClassVar

from django.contrib import admin

from budget.models import IncomingCategory, RevenueCategory


class IncomingCategoryAdmin(admin.ModelAdmin):
    """Admin interface for the IncomingCategory model.

    Attributes:
    ----------
        list_display (ClassVar[list[str]]): Fields to display in the list view.
        search_fields (ClassVar[list[str]]): Fields to include in the search functionality.
        ordering (ClassVar[list[str]]): Fields to use for ordering the list view.
    """

    list_display: ClassVar[list[str]] = [
        "id",
        "name",
        "description",
    ]
    search_fields: ClassVar[list[str]] = [
        "name",
        "description",
    ]
    ordering: ClassVar[list[str]] = [
        "name",
    ]


class RevenueCategoryAdmin(admin.ModelAdmin):
    """Admin interface for the RevenueCategory model.

    Attributes:
    ----------
        list_display (ClassVar[list[str]]): Fields to display in the list view.
        search_fields (ClassVar[list[str]]): Fields to include in the search functionality.
        ordering (ClassVar[list[str]]): Fields to use for ordering the list view.
    """

    list_display: ClassVar[list[str]] = [
        "id",
        "name",
        "description",
    ]
    search_fields: ClassVar[list[str]] = [
        "name",
        "description",
    ]
    ordering: ClassVar[list[str]] = [
        "name",
    ]


admin.site.register(IncomingCategory, IncomingCategoryAdmin)
admin.site.register(RevenueCategory, RevenueCategoryAdmin)
