import uuid

from django.db import models


class Incoming(models.Model):
    """
    Model for incoming transactions.

    Attributes:
    ----------
        id (models.UUIDField): The UUID field for primary key.
        user_id (models.IntegerField): The ID of the user.
        name (models.CharField): The name of the transaction.
        description (models.TextField): The description of the transaction.
        amount (models.DecimalField): The amount of the transaction.
        launch_date (models.DateTimeField): The date and time when the transaction was created.
        category (models.ForeignKey): The category of the transaction.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    launch_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        "IncomingCategory", on_delete=models.CASCADE, related_name="incoming"
    )

    def __str__(self):
        """
        String representation of the incoming transaction.

        Returns:
        -------
            str: The name of the transaction.
        """
        return self.name
