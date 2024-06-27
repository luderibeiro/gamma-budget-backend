import pytest
from datetime import date
from decimal import Decimal
from budget.models import Installment, Revenue, RevenueCategory
import uuid

@pytest.mark.django_db
def test_installment_creation():
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
    installment = Installment.objects.create(
        revenue=revenue,
        amount=Decimal("25.00"),
        due_date=date.today(),
        period=1,
        period_unit="months",
        paid=False,
        periods_paid=0,
        payment_method="Credit Card"
    )
    assert installment.id is not None
    assert installment.revenue == revenue
    assert installment.amount == Decimal("25.00")
    assert installment.due_date == date.today()
    assert installment.period == 1
    assert installment.period_unit == "months"
    assert installment.paid is False
    assert installment.periods_paid == 0
    assert installment.payment_method == "Credit Card"

@pytest.mark.django_db
def test_installment_str():
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
    installment = Installment.objects.create(
        revenue=revenue,
        amount=Decimal("25.00"),
        due_date=date.today(),
        period=1,
        period_unit="months",
        paid=False,
        periods_paid=0,
        payment_method="Credit Card"
    )
    assert str(installment) == "Test Revenue"

@pytest.mark.django_db
def test_installment_paid():
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
    installment = Installment.objects.create(
        revenue=revenue,
        amount=Decimal("25.00"),
        due_date=date.today(),
        period=1,
        period_unit="months",
        paid=True,
        periods_paid=1,
        payment_method="Credit Card"
    )
    assert installment.paid is True
    assert installment.periods_paid == 1
    assert installment.payment_method == "Credit Card"
