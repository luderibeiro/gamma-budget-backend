import datetime


class Alert:
    """
    Class representing an alert budget record.

    Attributes:
    ----------
        id (str): The ID of the alert record.
        user_id (int): The ID of the user.
        revenue_id (str): The ID of the revenue record.
        message (str): The message of the alert.
        alert_date (datetime.datetime): The date and time of the alert.
    """

    def __init__(
        self,
        id: str,
        user_id: int,
        user_email: str,
        revenue_id: str,
        message: str,
        alert_date: datetime.datetime,
    ) -> None:
        """
        Initialize the alert record.

        Args:
        ----
            id (str): The ID of the alert record.
            user_id (int): The ID of the user.
            revenue_id (str): The ID of the revenue record.
            message (str): The message of the alert.
            alert_date (datetime.datetime): The date and time of the alert.
        """
        self.id = id
        self.user_id = user_id
        self.user_email = user_email
        self.revenue_id = revenue_id
        self.message = message
        self.alert_date = alert_date

    def to_dict(self) -> dict:
        """
        Convert the alert record to a dictionary.

        Returns:
        -------
            dict: A dictionary representation of the alert record.
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user_email": self.user_email,
            "revenue_id": self.revenue_id,
            "message": self.message,
            "alert_date": self.alert_date,
        }
