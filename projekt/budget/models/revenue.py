from django.db import models


class Revenue(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    expiration_date = models.DateField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    payment_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey("RevenueCategory", on_delete=models.CASCADE, related_name="revenue")

    def __str__(self):
        return self.name
