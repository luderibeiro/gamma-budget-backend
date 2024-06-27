import datetime
from typing import Any


class Limit:
    """
    Class representing an limit budget record.

    Attributes:
    ----------
        id (str): The ID of the limit record.
        user_id (int): The ID of the user.
        limit (float): The limit amount.
        amount (float): The amount of the limit record.
        launch_date (datetime.datetime): The launch date of the limit record.
        category (int): The category of the limit record.
    """

    def __init__(
        self,
        id: str,
        user_id: int,
        limit: float,
        amount: float,
        limit_date: datetime.datetime,
        category: dict[str, Any],
    ) -> None:
        """
        Initialize the limit record.

        Args:
        ----
            id (str): The ID of the limit record.
            user_id (int): The ID of the user.
            limit (float): The limit amount.
            amount (float): The amount of the limit record.
            launch_date (datetime.datetime): The launch date of the limit record.
            category (int): The category of the limit record.
        """
        self.id = id
        self.user_id = user_id
        self.limit = limit
        self.amount = amount
        self.limit_date = limit_date
        self.category = category

    def to_dict(self) -> dict:
        """
        Convert the limit record to a dictionary.

        Returns:
        -------
            dict: A dictionary representation of the limit record.
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "limit": self.limit,
            "amount": self.amount,
            "limit_date": self.limit_date,
            "category": self.category,
        }
