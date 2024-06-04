from budget.models import Revenue
from rest_framework import serializers


class RevenueCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating Revenue instances.

    Attributes:
    ----------
        name (CharField): The name of the revenue.
        description (CharField): The description of the revenue.
        amount (DecimalField): The amount of the revenue.
        expiration_date (DateField): The expiration date of the revenue.
        paid (BooleanField): Whether the revenue is paid.
        payment_date (DateField): The payment date of the revenue.
        category (UUIDField): The category of the revenue.
    """

    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    expiration_date = serializers.DateField()
    paid = serializers.BooleanField()
    payment_date = serializers.DateField(allow_null=True)
    category = serializers.UUIDField()

    class Meta:
        """Meta class for RevenueCreateSerializer."""

        model = Revenue
        fields = (
            "name",
            "description",
            "amount",
            "expiration_date",
            "paid",
            "payment_date",
            "category",
        )


class RevenueListSerializer(serializers.ModelSerializer):
    """Serializer for listing Revenue instances.

    Attributes:
    ----------
        name (CharField): The name of the revenue.
        description (CharField): The description of the revenue.
        amount (DecimalField): The amount of the revenue.
        expiration_date (DateField): The expiration date of the revenue.
        paid (BooleanField): Whether the revenue is paid.
        payment_date (DateField): The payment date of the revenue.
        category (UUIDField): The category of the revenue.
    """

    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    expiration_date = serializers.DateField()
    paid = serializers.BooleanField()
    payment_date = serializers.DateField(allow_null=True)
    category = serializers.UUIDField()

    class Meta:
        """Meta class for RevenueListSerializer."""

        model = Revenue
        fields = "__all__"


class RevenueDetailSerializer(serializers.ModelSerializer):
    """Serializer for detailing Revenue instances."""

    class Meta:
        """Meta class for RevenueDetailSerializer."""

        model = Revenue
        fields = "__all__"


class RevenueUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating Revenue instances.

    Attributes:
    ----------
        name (CharField): The name of the revenue.
        description (CharField): The description of the revenue.
        amount (DecimalField): The amount of the revenue.
        expiration_date (DateField): The expiration date of the revenue.
        paid (BooleanField): Whether the revenue is paid.
        payment_date (DateField): The payment date of the revenue.
        category (UUIDField): The category of the revenue.
    """

    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    expiration_date = serializers.DateField()
    paid = serializers.BooleanField()
    payment_date = serializers.DateField(allow_null=True)
    category = serializers.UUIDField()

    class Meta:
        """Meta class for RevenueUpdateSerializer."""

        model = Revenue
        fields = (
            "name",
            "description",
            "amount",
            "expiration_date",
            "paid",
            "payment_date",
            "category",
        )


class RevenueDeleteSerializer(serializers.ModelSerializer):
    """Serializer for deleting Revenue instances."""

    class Meta:
        """Meta class for RevenueDeleteSerializer."""

        model = Revenue
        fields = "__all__"


class RevenueCategoryListSerializer(serializers.ModelSerializer):
    """Serializer for listing categories of Revenue instances."""

    class Meta:
        """Meta class for RevenueCategoryListSerializer."""

        model = Revenue
        fields = "__all__"
