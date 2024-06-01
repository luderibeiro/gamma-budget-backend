from budget.models import Incoming
from django.contrib import admin


class IncomingAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
        "name",
        "amount",
        "category",
        "launch_date",
    ]
    list_filter = [
        "user_id",
        "category",
    ]
    search_fields = [
        "id",
        "user_id",
        "name",
        "description",
    ]
    ordering = [
        "user_id",
        "launch_date",
    ]


admin.site.register(Incoming, IncomingAdmin)
