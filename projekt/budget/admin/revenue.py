from budget.models import Installment, Recurring, Revenue
from django.contrib import admin


class RevenueAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "name",
        "amount",
        "category",
    ]
    list_filter = [
        "category",
    ]
    search_fields = [
        "id",
        "name",
        "description",
    ]
    ordering = [
        "user_id",
        "expiration_date",
        "category",
        "name",
    ]


class InstallmentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
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
        "id",
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
