from budget.models import Incoming
from django.contrib import admin


class IncomingAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "amount",
        "category",
    ]
    list_filter = [
        "category",
    ]
    search_fields = [
        "name",
        "description",
    ]
    ordering = [
        "launch_date",
    ]


admin.site.register(Incoming, IncomingAdmin)
