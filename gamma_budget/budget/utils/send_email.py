import os
import time
from datetime import date

from budget.models.alert import Alert
from budget.models.revenue import Revenue
from django.core.mail import send_mail


class SendEmail:
    def _send_alert_email(
        self,
        subject,
        from_email,
        recipient_list,
        revenue: dict,
        fail_silently=False,
        message=None,
        auth_user=None,
        auth_password=None,
        connection=None,
    ):
        return send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently,
            auth_user,
            auth_password,
            connection,
            html_message=self._get_html_message_alert_email(revenue),
        )

    def _get_html_message_alert_email(self, revenue: dict):
        return (
            '<html lang="pt-br">'
            "<header>"
            '<meta charset="utf-8"/>'
            "</header>"
            "<body>"
            "<p><strong>Alerta de despesa GammaBudget</strong></p>"
            "<p>Despesa: " + revenue["name"] + "</p>"
            "<p>Data de vencimento: " + str(revenue["expiration_date"]) + "</p>"
            "<p><strong>Valor da despesa: {}</strong></p>".format(str(revenue["amount"]) + "</body>" "</html>")
        )

    def _get_alerts_to_send_email_today(self):
        alerts = Alert.objects.filter(alert_date=date.today())
        if not alerts:
            print("No alerts to send email today.")
            return None
        alerts_data = []
        for alert in alerts:
            alert_data = {
                "user_email": alert.user.email,
                "revenue_id": alert.revenue.id,
            }
            alerts_data.append(alert_data)
        return alerts_data

    def _get_revenue(self, revenue_id):
        revenue = Revenue.objects.get(id=revenue_id)
        if not revenue:
            print("Revenue was not found.")
            return None
        data = {
            "name": revenue.name,
            "expiration_date": revenue.expiration_date,
            "amount": revenue.amount,
        }
        return data

    def _send_email(self, alert: dict):
        revenue = {}
        revenue = self._get_revenue(alert.get("revenue_id"))
        self._send_alert_email(
            subject=f"Alerta de despesa `{revenue.get("name")} - GammaBudget",
            from_email=os.getenv("EMAIL_HOST_USER"),
            recipient_list=[alert.get("user_email")],
            revenue=revenue,
        )

    def send_today_alerts(self):
        print("Checking for alerts to send email...")
        alerts = self._get_alerts_to_send_email_today()
        for alert in alerts:
            email_sent = self._send_email(alert)
            if email_sent:
                print("Email sent successfully to {}".format(alert.get("user_email")))
            else:
                print("Failed to send email to {}".format(alert.get("user_email")))
