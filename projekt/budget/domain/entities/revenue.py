import datetime


class Revenue:
    """
    Class representing a revenue record.

    Attributes:
    ----------
        name (str): The name of the revenue record.
        description (str): The description of the revenue record.
        amount (float): The amount of the revenue record.
        expiration_date (datetime.datetime): The expiration date of the revenue record.
        paid (bool): Flag indicating if the revenue has been paid.
        payment_date (datetime.datetime): The payment date of the revenue record.
        category (int): The category of the revenue record.
    """

    def __init__(
        self,
        id: str,
        user_id: int,
        name: str,
        description: str,
        amount: float,
        expiration_date: datetime.datetime,
        paid: bool,
        payment_date: datetime.datetime,
        category: int,
    ) -> None:
        """
        Initialize the revenue record.

        Args:
        ----
            name (str): The name of the revenue record.
            description (str): The description of the revenue record.
            amount (float): The amount of the revenue record.
            expiration_date (datetime.datetime): The expiration date of the revenue record.
            paid (bool): Flag indicating if the revenue has been paid.
            payment_date (datetime.datetime): The payment date of the revenue record.
            category (int): The category of the revenue record.
        """
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.amount = amount
        self.expiration_date = expiration_date
        self.paid = paid
        self.payment_date = payment_date if paid else None
        self.category = category

    def to_dict(self) -> dict:
        """
        Convert the revenue record to a dictionary.

        Returns:
        -------
            dict: A dictionary representation of the revenue record.
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
            "amount": self.amount,
            "expiration_date": self.expiration_date,
            "paid": self.paid,
            "payment_date": self.payment_date if self.paid else None,
            "category": self.category,
        }
