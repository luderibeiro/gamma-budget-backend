import uuid

from django.db import models


class Installment(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    revenue = models.ForeignKey("Revenue", on_delete=models.CASCADE, related_name="installment")
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    due_date = models.DateField()
    period = models.PositiveBigIntegerField()
    period_unit = models.CharField(max_length=10, default="months")
    paid = models.BooleanField(default=False)
    periods_paid = models.PositiveBigIntegerField(default=0)
    payment_method = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
