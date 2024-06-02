class Category:
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
    ) -> None:
        self.id = id
        self.name = name
        self.description = description

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
