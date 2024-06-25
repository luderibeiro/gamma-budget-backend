from budget.models.alert import Alert
from rest_framework import serializers


class AlertSerializer(serializers.ModelSerializer):
    """
    Serializer for the Alert model.

    Attributes:
    ----------
        user_id (serializers.IntegerField): The ID of the user who will receive alert.
        revenue_id (serializers.UUIDField): The ID of the revenue record.
        message (serializers.CharField): The message of the alert.
        alert_date (serializers.DateTimeField): The date and time of the alert.
        Meta (serializers.ModelSerializer): The metadata class for the serializer.
    """

    user_id = serializers.IntegerField(required=True)
    revenue_id = serializers.UUIDField(required=True)
    message = serializers.CharField(max_length=255)
    alert_date = serializers.DateTimeField()

    class Meta:
        model = Alert
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class AlertUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for the Alert model.

    Attributes:
    ----------
        user_id (serializers.IntegerField): The ID of the user who will receive alert.
        revenue_id (serializers.UUIDField): The ID of the revenue record.
        message (serializers.CharField): The message of the alert.
        alert_date (serializers.DateTimeField): The date and time of the alert.
        Meta (serializers.ModelSerializer): The metadata class for the serializer.
    """

    revenue_id = serializers.UUIDField(required=True)
    message = serializers.CharField(max_length=255)
    alert_date = serializers.DateTimeField()

    class Meta:
        model = Alert
        fields = [
            "revenue_id",
            "message",
            "alert_date",
        ]
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
