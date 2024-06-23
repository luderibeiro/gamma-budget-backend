import uuid

from django.db import models


class Limit(models.Model):
    """
    Model for revenue limits.

    Attributes:
    ----------
        id (models.UUIDField): The UUID field for primary key.
        user (models.IntegerField): The user associated with the limit.
        limit (models.DecimalField): The limit amount.
        amount (models.DecimalField): The amount of the limit.
        limit_date (models.DateField): The date to associate month and year of limit.
        category (models.ForeignKey): The category associated with the limit.
        is_active (models.BooleanField): Flag indicating if the limit is active.
        created_at (models.DateTimeField): The date and time the limit was created.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.IntegerField()
    limit = models.DecimalField(max_digits=15, decimal_places=2)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    limit_date = models.DateField(null=False, blank=False)
    category = models.ForeignKey("RevenueCategory", on_delete=models.CASCADE, related_name="limits")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the limit transaction.

        Returns:
        -------
            str: The name of the transaction.
        """
        return self.category.name
