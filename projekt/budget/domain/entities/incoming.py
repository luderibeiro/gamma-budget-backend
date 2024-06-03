import datetime


class Incoming:
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
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.amount = amount
        self.launch_date = launch_date
        self.category = category

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
            "amount": self.amount,
            "launch_date": self.launch_date,
            "category": self.category,
        }
