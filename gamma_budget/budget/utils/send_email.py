from django.core.mail import send_mail


class SendEmail:
    def send_alert_email(
        self,
        subject,
        from_email,
        recipient_list,
        message,
        revenue,
        fail_silently=False,
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
            html_message=self._get_html_message_alert_email(message, revenue),
        )

    def _get_html_message_alert_email(self, message, revenue):
        return (
            '<html lang="pt-br">'
            "<header>"
            '<meta charset="utf-8"/>'
            "</header>"
            "<body>"
            "<p><strong>Alerta de despesa GammaBudget</strong></p>"
            "<p>Despesa: " + revenue["name"] + "</p>"
            "<p>Data de vencimento: " + str(revenue["expiration_date"]) + "</p>"
            "<p><strong>Valor da despesa: {}</strong></p>".format(revenue["amount"] + "</body>" "</html>")
        )
