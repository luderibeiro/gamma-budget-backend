from typing import ClassVar

from budget.models import Limit
from rest_framework import serializers


class LimitSerializer(serializers.ModelSerializer):
    """Serializer default for Limit model.

    Attributes:
    ----------
        user_id (IntegerField): The ID of the user.
        limit (DecimalField): The limit amount.
        amount (DecimalField): The amount of the incoming item.
        category (UUIDField): The category of the incoming item.
    """

    user_id = serializers.IntegerField()
    limit = serializers.DecimalField(max_digits=15, decimal_places=2)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    limit_date = serializers.DateField()
    category = serializers.UUIDField()

    class Meta:
        """Meta class for LimitCreateSerializer."""

        model = Limit
        fields: ClassVar[list[str]] = [
            "user_id",
            "limit",
            "amount",
            "limit_date",
            "category",
        ]


class LimitUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating a limit record.

    Attributes:
    ----------
        limit (DecimalField): The limit amount.
        amount (DecimalField): The amount of the limit record.
    """

    limit = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)

    class Meta:
        """Meta class for LimitUpdateSerializer."""

        model = Limit
        fields: ClassVar[list[str]] = [
            "limit",
            "amount",
        ]
