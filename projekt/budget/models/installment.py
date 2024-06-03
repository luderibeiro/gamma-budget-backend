import uuid

from django.db import models


class Installment(models.Model):
    """
    Model for revenue installments.

    Attributes:
    ----------
        id (models.UUIDField): The UUID field for primary key.
        revenue (models.ForeignKey): The revenue associated with the installment.
        amount (models.DecimalField): The amount of the installment.
        due_date (models.DateField): The due date of the installment.
        period (models.PositiveBigIntegerField): The period of the installment.
        period_unit (models.CharField): The unit of the period.
        paid (models.BooleanField): Flag indicating if the installment is paid.
        periods_paid (models.PositiveBigIntegerField): The number of periods paid.
        payment_method (models.CharField): The payment method for the installment.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    revenue = models.ForeignKey(
        "Revenue", on_delete=models.CASCADE, related_name="installment"
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    due_date = models.DateField()
    period = models.PositiveBigIntegerField()
    period_unit = models.CharField(max_length=10, default="months")
    paid = models.BooleanField(default=False)
    periods_paid = models.PositiveBigIntegerField(default=0)
    payment_method = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        """
        String representation of the installment.

        Returns:
        -------
            str: A string representation of the installment.
        """
        return self.name
