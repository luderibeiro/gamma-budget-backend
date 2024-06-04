from django.apps import AppConfig


class BudgetConfig(AppConfig):
    """
    AppConfig for the budget app.

    Attributes:
    ----------
        default_auto_field (str): The default auto field for models.
        name (str): The name of the app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "budget"

    def ready(self):
        """
        Method to perform app initialization.

        Imports the configure function from budget.main and calls it.
        """
        from budget.main import configure

        configure()
