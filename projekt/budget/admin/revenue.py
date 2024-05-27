from budget.models import Installment, Recurring, Revenue
from django.contrib import admin


class RevenueAdmin(admin.ModelAdmin):

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
        "expiration_date",
        "name",
    ]


class InstallmentAdmin(admin.ModelAdmin):
    list_display = [
        "revenue",
        "amount",
        "due_date",
    ]
    list_filter = []
    search_fields = [
        "description",
    ]
    ordering = [
        "revenue",
    ]


class RecurringAdmin(admin.ModelAdmin):
    list_display = [
        "active",
        "revenue",
        "amount",
    ]
    list_filter = [
        "revenue",
        "payment_date",
        "active",
    ]
    search_fields = [
        "description",
    ]
    ordering = [
        "revenue",
    ]


admin.site.register(Revenue, RevenueAdmin)
admin.site.register(Installment, InstallmentAdmin)
admin.site.register(Recurring, RecurringAdmin)
