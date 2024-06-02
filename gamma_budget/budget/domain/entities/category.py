class Category:
    """
    A class to represent a category.

    Attributes
    ----------
    id : str
        The unique identifier of the category.
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
        Constructs all the necessary attributes for the Category object.

        Parameters
        ----------
        id: str
            The unique identifier of the category.
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
        Converts the Category instance to a dictionary.

        Returns
        -------
        dict
            A dictionary representation of the Category instance.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
