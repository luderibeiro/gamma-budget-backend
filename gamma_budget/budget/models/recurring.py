import uuid

from django.db import models


class Recurring(models.Model):
    """
    Model for recurring revenues.

    Attributes:
    ----------
        id (models.UUIDField): The UUID field for primary key.
        revenue (models.ForeignKey): The revenue associated with the recurring payment.
        amount (models.DecimalField): The amount of the recurring payment.
        payment_method (models.CharField): The payment method for the recurring payment.
        payment_date (models.DateField): The date of the recurring payment.
        period (models.PositiveBigIntegerField): The period of the recurring payment.
        period_unit (models.CharField): The unit of the period.
        active (models.BooleanField): Flag indicating if the recurring payment is active.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    revenue = models.ForeignKey(
        "Revenue", on_delete=models.CASCADE, related_name="recurring"
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    period = models.PositiveBigIntegerField()
    period_unit = models.CharField(max_length=10, default="months")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
