from rest_framework import serializers

from budget.models import Incoming


class IncomingCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    category = serializers.UUIDField()

    class Meta:
        model = Incoming
        fields = (
            "name",
            "description",
            "amount",
            "category",
        )


class IncomingListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    launch_date = serializers.DateTimeField()
    category = serializers.UUIDField()

    class Meta:
        model = Incoming
        fields = "__all__"


class IncomingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incoming
        fields = "__all__"


class IncomingUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    category = serializers.UUIDField()

    class Meta:
        model = Incoming
        fields = (
            "name",
            "description",
            "amount",
            "category",
        )


class IncomingDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incoming
        fields = "__all__"


class IncomingCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incoming
        fields = "__all__"
