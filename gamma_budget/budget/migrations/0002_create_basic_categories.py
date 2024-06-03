from budget.models import IncomingCategory, RevenueCategory
from django.db import migrations


def create_categories(apps, schema_editor):
    IncomingCategory.objects.bulk_create(
        [
            IncomingCategory(
                name="Salário", description="Receita referente ao salário"
            ),
            IncomingCategory(
                name="Investimento", description="Receita referente a investimentos"
            ),
            IncomingCategory(name="Outros", description="Outros tipos de receita"),
        ]
    )
    RevenueCategory.objects.bulk_create(
        [
            RevenueCategory(
                name="Alimentação", description="Categoria de despesa de Alimentação"
            ),
            RevenueCategory(
                name="Assinaturas e serviços",
                description="Categoria de despesa de Assinaturas e serviços",
            ),
            RevenueCategory(name="Casa", description="Categoria de despesa de Casa"),
            RevenueCategory(
                name="Compras", description="Categoria de despesa de Compras"
            ),
            RevenueCategory(
                name="Cuidados pessoais",
                description="Categoria de despesa de Cuidados pessoais",
            ),
            RevenueCategory(
                name="Dívidas e empréstimos",
                description="Categoria de despesa de Dívidas e empréstimos",
            ),
            RevenueCategory(
                name="Educação", description="Categoria de despesa de Educação"
            ),
            RevenueCategory(
                name="Família", description="Categoria de despesa de Família"
            ),
            RevenueCategory(
                name="Impostos", description="Categoria de despesa de Impostos"
            ),
            RevenueCategory(
                name="Investimentos",
                description="Categoria de despesa de Investimentos",
            ),
            RevenueCategory(name="Lazer", description="Categoria de despesa de Lazer"),
            RevenueCategory(
                name="Presentes", description="Categoria de despesa de Presentes"
            ),
            RevenueCategory(
                name="Mercado", description="Categoria de despesa de Mercado"
            ),
            RevenueCategory(name="Pets", description="Categoria de despesa de Pets"),
            RevenueCategory(
                name="Restaurantes", description="Categoria de despesa de Restaurantes"
            ),
            RevenueCategory(name="Saúde", description="Categoria de despesa de Saúde"),
            RevenueCategory(
                name="Transporte", description="Categoria de despesa de Transporte"
            ),
            RevenueCategory(
                name="Viagem", description="Categoria de despesa de Viagem"
            ),
            RevenueCategory(
                name="Outros", description="Categoria de despesa de Outros"
            ),
        ]
    )


def reverse_create_categories(apps, schema_editor):
    IncomingCategory.objects.all().delete()
    RevenueCategory.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("budget", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_categories, reverse_create_categories),
    ]
