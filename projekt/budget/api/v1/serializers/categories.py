from budget.models.categories import IncomingCategory, RevenueCategory
from rest_framework import serializers


class IncomingCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomingCategory
        fields = "__all__"


class RevenueCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueCategory
        fields = "__all__"
