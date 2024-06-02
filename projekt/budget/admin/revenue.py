from budget.models import Installment, Recurring, Revenue
from django.contrib import admin


class RevenueAdmin(admin.ModelAdmin):
    readonly_fields = [
        "id",
        "user_id",
    ]
    list_display = [
        "id",
        "user_id",
        "name",
        "amount",
        "category",
        "expiration_date",
    ]
    list_filter = [
        "user_id",
        "category",
    ]
    search_fields = [
        "id",
        "name",
        "amount",
    ]
    ordering = [
        "user_id",
        "expiration_date",
        "category",
        "name",
    ]
    fields = [
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
        model = Revenue
        fields = "__all__"


# class InstallmentAdmin(admin.ModelAdmin):
#     list_display = [
#         "id",
#         "revenue",
#         "amount",
#         "due_date",
#     ]
#     list_filter = []
#     search_fields = [
#         "description",
#     ]
#     ordering = [
#         "revenue",
#     ]


# class RecurringAdmin(admin.ModelAdmin):
#     list_display = [
#         "id",
#         "active",
#         "revenue",
#         "amount",
#     ]
#     list_filter = [
#         "revenue",
#         "payment_date",
#         "active",
#     ]
#     search_fields = [
#         "description",
#     ]
#     ordering = [
#         "revenue",
#     ]


admin.site.register(Revenue, RevenueAdmin)
# admin.site.register(Installment, InstallmentAdmin)
# admin.site.register(Recurring, RecurringAdmin)
