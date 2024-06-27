
import pytest
from budget.api.v1.serializers.incoming import (
    IncomingCreateSerializer,
)
from budget.models.categories import IncomingCategory


@pytest.mark.django_db
def test_incoming_create_serializer():
    category = IncomingCategory(name="Teste")
    data = {"name": "Test Incoming", "description": "Test description", "amount": "100.00", "category": category.id}
    serializer = IncomingCreateSerializer(data=data)

    assert serializer.is_valid(), serializer.errors
    assert serializer.data["name"] == data["name"]
    assert serializer.data["description"] == data["description"]
    assert serializer.data["amount"] == data["amount"]
    assert serializer.data["category"] == str(data["category"])


# @pytest.mark.django_db
# def test_incoming_list_serializer():
#     incoming_category = IncomingCategory(name="Teste_incoming")
#     incoming_category.save()
#     incoming = Incoming.objects.create(
#         name="Test Incoming",
#         description="Test description",
#         amount=Decimal("100.00"),
#         launch_date=datetime.today(),
#         incoming_date=datetime.today(),
#         category=incoming_category,
#     )
#     serializer = IncomingListSerializer(incoming)
#     data = serializer.data
#     assert data["name"] == incoming.name
#     assert data["description"] == incoming.description
#     assert data["amount"] == str(incoming.amount)
#     assert data["launch_date"] == incoming.launch_date.strftime("%Y-%m-%d %H:%M:%S.%f:%z")
#     assert data["incoming_date"] == incoming.incoming_date.strftime("%Y-%m-%d %H:%M:%S.%f:%z")
#     assert data["category"] == str(incoming.category)


# @pytest.mark.django_db
# def test_incoming_detail_serializer():
#     incoming = Incoming.objects.create(
#         name="Test Incoming",
#         description="Test description",
#         amount=Decimal("100.00"),
#         launch_date=date.today(),
#         incoming_date=date.today(),
#         category=uuid4(),
#     )
#     serializer = IncomingDetailSerializer(incoming)
#     data = serializer.data
#     assert data["name"] == incoming.name
#     assert data["description"] == incoming.description
#     assert data["amount"] == str(incoming.amount)
#     assert data["launch_date"] == str(incoming.launch_date)
#     assert data["incoming_date"] == str(incoming.incoming_date)
#     assert data["category"] == str(incoming.category)


# @pytest.mark.django_db
# def test_incoming_update_serializer():
#     incoming = Incoming.objects.create(name="Test Incoming", description="Test description", amount=Decimal("100.00"), category=uuid4())
#     data = {"name": "Updated Incoming", "description": "Updated description", "amount": "200.00", "category": uuid4()}
#     serializer = IncomingUpdateSerializer(incoming, data=data)
#     assert serializer.is_valid(), serializer.errors
#     instance = serializer.save()
#     assert instance.name == data["name"]
#     assert instance.description == data["description"]
#     assert instance.amount == Decimal(data["amount"])
#     assert instance.category == data["category"]


# @pytest.mark.django_db
# def test_incoming_delete_serializer():
#     incoming = Incoming.objects.create(name="Test Incoming", description="Test description", amount=Decimal("100.00"), category=uuid4())
#     serializer = IncomingDeleteSerializer(incoming)
#     data = serializer.data
#     assert data["name"] == incoming.name
#     assert data["description"] == incoming.description
#     assert data["amount"] == str(incoming.amount)
#     assert data["category"] == str(incoming.category)


# @pytest.mark.django_db
# def test_incoming_category_list_serializer():
#     incoming = Incoming.objects.create(name="Test Incoming", description="Test description", amount=Decimal("100.00"), category=uuid4())
#     serializer = IncomingCategoryListSerializer(incoming)
#     data = serializer.data
#     assert data["name"] == incoming.name
#     assert data["description"] == incoming.description
#     assert data["amount"] == str(incoming.amount)
#     assert data["category"] == str(incoming.category)
