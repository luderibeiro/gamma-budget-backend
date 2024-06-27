import pytest
from datetime import date
from decimal import Decimal
from budget.models import Revenue, RevenueCategory
import uuid

@pytest.mark.django_db
def test_revenue_creation():
    category = RevenueCategory.objects.create(name="Test Category")
    revenue = Revenue.objects.create(
        user_id=1,
        name="Test Revenue",
        description="Test description",
        amount=Decimal("100.00"),
        expiration_date=date.today(),
        paid=False,
        payment_date=None,
        category=category
    )
    assert revenue.id is not None
    assert revenue.user_id == 1
    assert revenue.name == "Test Revenue"
    assert revenue.description == "Test description"
    assert revenue.amount == Decimal("100.00")
    assert revenue.expiration_date == date.today()
    assert revenue.paid is False
    assert revenue.payment_date is None
    assert revenue.category == category

@pytest.mark.django_db
def test_revenue_str():
    category = RevenueCategory.objects.create(name="Test Category")
    revenue = Revenue.objects.create(
        user_id=1,
        name="Test Revenue",
        description="Test description",
        amount=Decimal("100.00"),
        expiration_date=date.today(),
        paid=False,
        payment_date=None,
        category=category
    )
    assert str(revenue) == "Test Revenue"

@pytest.mark.django_db
def test_revenue_paid():
    category = RevenueCategory.objects.create(name="Test Category")
    revenue = Revenue.objects.create(
        user_id=1,
        name="Test Revenue",
        description="Test description",
        amount=Decimal("100.00"),
        expiration_date=date.today(),
        paid=True,
        payment_date=date.today(),
        category=category
    )
    assert revenue.paid is True
    assert revenue.payment_date == date.today()
