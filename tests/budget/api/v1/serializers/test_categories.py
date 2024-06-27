import pytest
from budget.api.v1.serializers.categories import IncomingCategoryListSerializer, RevenueCategoryListSerializer
from budget.models.categories import IncomingCategory, RevenueCategory


@pytest.mark.django_db
def test_incoming_category_list_serializer():
    # Create an instance of IncomingCategory
    incoming_category = IncomingCategory.objects.create(name="Test Incoming Category")

    # Serialize the instance
    serializer = IncomingCategoryListSerializer(incoming_category)
    data = serializer.data

    # Check if the serialized data matches the instance's data
    assert data["id"] == str(incoming_category.id)
    assert data["name"] == incoming_category.name


@pytest.mark.django_db
def test_revenue_category_list_serializer():
    # Create an instance of RevenueCategory
    revenue_category = RevenueCategory.objects.create(name="Test Revenue Category")

    # Serialize the instance
    serializer = RevenueCategoryListSerializer(revenue_category)
    data = serializer.data

    # Check if the serialized data matches the instance's data
    assert data["id"] == str(revenue_category.id)
    assert data["name"] == revenue_category.name
