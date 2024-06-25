import uuid

from django.db import models


class Alert(models.Model):
    """
    Model for alerts.

    Attributes:
    ----------
        id (models.AutoField): The UUID field for primary key.
        user_id (models.IntegerField): The ID of the user who will receive alert.
        revenue_id (models.IntegerField): The ID of the revenue record.
        message (models.CharField): The message of the alert.
        alert_date (models.DateTimeField): The date and time of the alert.
        created_at (models.DateTimeField): The date and time the alert was created.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user_id = models.IntegerField(blank=False, null=False)
    revenue = models.ForeignKey("Revenue", on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    alert_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the alert.

        Returns:
        -------
            str: The message of the alert.
        """
        return self.message
