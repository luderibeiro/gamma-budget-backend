import uuid

from django.db import models


class Revenue(models.Model):
    """
    Model for revenue transactions.

    Attributes:
    ----------
        id (models.UUIDField): The UUID field for primary key.
        user_id (models.IntegerField): The ID of the user.
        name (models.CharField): The name of the revenue transaction.
        description (models.TextField): The description of the revenue transaction.
        amount (models.DecimalField): The amount of the revenue transaction.
        expiration_date (models.DateField): The expiration date of the revenue transaction.
        paid (models.BooleanField): Flag indicating if the revenue transaction is paid.
        payment_date (models.DateField): The payment date of the revenue transaction.
        category (models.ForeignKey): The category of the revenue transaction.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    expiration_date = models.DateField(blank=False, null=False)
    paid = models.BooleanField(default=False)
    payment_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey("RevenueCategory", on_delete=models.CASCADE, related_name="revenue")

    def __str__(self):
        """
        String representation of the revenue transaction.

        Returns:
        -------
            str: The name of the revenue transaction.
        """
        return self.name
