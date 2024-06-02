import uuid

from django.db import models


class IncomingCategory(models.Model):
    """
    Model for incoming categories.

    Attributes:
    ----------
        id (models.UUIDField): The UUID field for primary key.
        name (models.CharField): The name of the category.
        description (models.TextField): The description of the category.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        """
        String representation of the category.

        Returns:
        -------
            str: The name of the category.
        """
        return self.name


class RevenueCategory(models.Model):
    """
    Model for revenue categories.

    Attributes:
    ----------
        id (models.UUIDField): The UUID field for primary key.
        name (models.CharField): The name of the category.
        description (models.TextField): The description of the category.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        """
        String representation of the category.

        Returns:
        -------
            str: The name of the category.
        """
        return self.name
