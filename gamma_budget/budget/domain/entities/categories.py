class Category:
    """
    Represents a category with an ID, name, and description.

    Attributes:
    ----------
    id : str
        The unique identifier for the category.
    name : str
        The name of the category.
    description : str
        A brief description of the category.
    """

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
    ) -> None:
        """
        Initializes a Category instance.

        Parameters:
        ----------
        id : str
            The unique identifier for the category.
        name : str
            The name of the category.
        description : str
            A brief description of the category.
        """
        self.id = id
        self.name = name
        self.description = description

    def to_dict(self) -> dict:
        """
        Converts the Category instance into a dictionary.

        Returns:
        -------
        dict
            A dictionary representation of the category instance, containing the ID,
            name, and description.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
