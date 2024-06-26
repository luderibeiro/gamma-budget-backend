# Generated by Django 5.0 on 2024-05-28 19:53

import uuid
from typing import Any, ClassVar

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies: ClassVar[list[tuple[str, str]]] = []

    operations: ClassVar[Any] = [
        migrations.CreateModel(
            name="IncomingCategory",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Revenue",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("user_id", models.IntegerField(default=0)),
                ("name", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=15)),
                ("expiration_date", models.DateField(auto_now_add=True)),
                ("paid", models.BooleanField(default=False)),
                ("payment_date", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="RevenueCategory",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Incoming",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("user_id", models.IntegerField(default=0)),
                ("name", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=15)),
                ("launch_date", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="incoming",
                        to="budget.incomingcategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recurring",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=15)),
                (
                    "payment_method",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("payment_date", models.DateField(blank=True, null=True)),
                ("period", models.PositiveBigIntegerField()),
                ("period_unit", models.CharField(default="months", max_length=10)),
                ("active", models.BooleanField(default=True)),
                (
                    "revenue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recurring",
                        to="budget.revenue",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Installment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=15)),
                ("due_date", models.DateField()),
                ("period", models.PositiveBigIntegerField()),
                ("period_unit", models.CharField(default="months", max_length=10)),
                ("paid", models.BooleanField(default=False)),
                ("periods_paid", models.PositiveBigIntegerField(default=0)),
                (
                    "payment_method",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "revenue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="installment",
                        to="budget.revenue",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="revenue",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="revenue",
                to="budget.revenuecategory",
            ),
        ),
    ]
