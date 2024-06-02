import datetime

from budget.domain.entities.category import Category


class Revenue:
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
