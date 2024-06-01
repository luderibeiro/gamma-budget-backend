import datetime


class Incoming:
    def __init__(
        self,
        name: str,
        description: str,
        amount: float,
        launch_date: datetime.datetime,
        category: int,
    ) -> None:
        self.name = name
        self.description = description
        self.amount = amount
        self.launch_date = launch_date
        self.category = category

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "amount": self.amount,
            "launch_date": self.launch_date,
            "category": self.category,
        }
