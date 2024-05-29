from budget.models import Revenue
from rest_framework import serializers


class RevenueCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    expiration_date = serializers.DateField()
    paid = serializers.BooleanField()
    payment_date = serializers.DateField()
    category = serializers.UUIDField()

    class Meta:
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
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    expiration_date = serializers.DateField()
    paid = serializers.BooleanField()
    payment_date = serializers.DateField()
    category = serializers.UUIDField()

    class Meta:
        model = Revenue
        fields = "__all__"


class RevenueDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = "__all__"


class RevenueUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    expiration_date = serializers.DateField()
    paid = serializers.BooleanField()
    payment_date = serializers.DateField()
    category = serializers.UUIDField()

    class Meta:
        model = Revenue
        fields = (
            "name",
            "description",
            "amount",
            "category",
            "expiration_date",
            "paid",
            "payment_date",
            "category",
        )


class RevenueDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = "__all__"


class RevenueCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = "__all__"
