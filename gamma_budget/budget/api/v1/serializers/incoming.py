from budget.models import Incoming
from rest_framework import serializers


class IncomingCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating Incoming instances.

    Attributes:
    ----------
        name (CharField): The name of the incoming item.
        description (CharField): The description of the incoming item.
        amount (DecimalField): The amount of the incoming item.
        category (UUIDField): The category of the incoming item.
    """

    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    category = serializers.UUIDField()

    class Meta:
        """Meta class for IncomingCreateSerializer."""

        model = Incoming
        fields = (
            "name",
            "description",
            "amount",
            "category",
        )


class IncomingListSerializer(serializers.ModelSerializer):
    """Serializer for listing Incoming instances.

    Attributes:
    ----------
        name (CharField): The name of the incoming item.
        description (CharField): The description of the incoming item.
        amount (DecimalField): The amount of the incoming item.
        launch_date (DateTimeField): The launch date of the incoming item.
        category (UUIDField): The category of the incoming item.
    """

    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    launch_date = serializers.DateTimeField()
    category = serializers.UUIDField()

    class Meta:
        """Meta class for IncomingListSerializer."""

        model = Incoming
        fields = "__all__"


class IncomingDetailSerializer(serializers.ModelSerializer):
    """Serializer for detailing Incoming instances."""

    class Meta:
        """Meta class for IncomingDetailSerializer."""

        model = Incoming
        fields = "__all__"


class IncomingUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating Incoming instances.

    Attributes:
    ----------
        name (CharField): The name of the incoming item.
        description (CharField): The description of the incoming item.
        amount (DecimalField): The amount of the incoming item.
        category (UUIDField): The category of the incoming item.
    """

    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    category = serializers.UUIDField()

    class Meta:
        """Meta class for IncomingUpdateSerializer."""

        model = Incoming
        fields = (
            "name",
            "description",
            "amount",
            "category",
        )


class IncomingDeleteSerializer(serializers.ModelSerializer):
    """Serializer for deleting Incoming instances."""

    class Meta:
        """Meta class for IncomingDeleteSerializer."""

        model = Incoming
        fields = "__all__"


class IncomingCategoryListSerializer(serializers.ModelSerializer):
    """Serializer for listing categories of Incoming instances."""

    class Meta:
        """Meta class for IncomingCategoryListSerializer."""

        model = Incoming
        fields = "__all__"
