from budget.domain.entities import Alert
from budget.models import Alert as AlertModel


def parse_alert_model_to_entity(alert: AlertModel) -> Alert:
    return Alert(
        id=alert.id,
        user_id=alert.user_id,
        revenue_id=alert.revenue.id,
        message=alert.message,
        alert_date=alert.alert_date,
    )
