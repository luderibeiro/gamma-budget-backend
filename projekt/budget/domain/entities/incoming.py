import datetime


class Incoming:
    """
    Class representing an incoming budget record.

    Attributes:
    ----------
        name (str): The name of the incoming record.
        description (str): The description of the incoming record.
        amount (float): The amount of the incoming record.
        launch_date (datetime.datetime): The launch date of the incoming record.
        category (int): The category of the incoming record.
    """

    def __init__(
        self,
        id: str,
        user_id: int,
        name: str,
        description: str,
        amount: float,
        launch_date: datetime.datetime,
        category: int,
    ) -> None:
        """
        Initialize the incoming record.

        Args:
        ----
            name (str): The name of the incoming record.
            description (str): The description of the incoming record.
            amount (float): The amount of the incoming record.
            launch_date (datetime.datetime): The launch date of the incoming record.
            category (int): The category of the incoming record.
        """
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.amount = amount
        self.launch_date = launch_date
        self.category = category

    def to_dict(self) -> dict:
        """
        Convert the incoming record to a dictionary.

        Returns:
        -------
            dict: A dictionary representation of the incoming record.
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
            "amount": self.amount,
            "launch_date": self.launch_date,
            "category": self.category,
        }
