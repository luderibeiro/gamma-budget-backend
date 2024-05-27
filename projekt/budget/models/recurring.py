from django.db import models


class Recurring(models.Model):
    revenue = models.ForeignKey("Revenue", on_delete=models.CASCADE, related_name="recurring")
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    period = models.PositiveBigIntegerField()
    period_unit = models.CharField(max_length=10, default="months")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
