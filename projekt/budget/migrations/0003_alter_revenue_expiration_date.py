# Generated by Django 5.0 on 2024-06-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_create_basic_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenue',
            name='expiration_date',
            field=models.DateField(),
        ),
    ]
