from typing import Generic, TypeVar

DataAccessT = TypeVar("DataAccessT")
GatewayT = TypeVar("GatewayT")


class GetDataAccessUseCaseMixin(Generic[DataAccessT]):
    """Mixin class to provide a method for getting data access.

    Attributes:
    ----------
        data_access (type[DataAccessT] | None): The data access class or None.
    """

    data_access: type[DataAccessT] | None

    def __init__(self, *args, **kwargs):
        """Initialize the GetDataAccessUseCaseMixin.

        Args:
        ----
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

    def get_data_access(self) -> DataAccessT | None:
        """Get an instance of the data access class.

        Returns:
        -------
            DataAccessT | None: An instance of the data access class, or None if not set.
        """
        if self.data_access:
            return self.data_access()
        return None


class ValidateDataAccessUseCaseMixin:
    """Mixin class to provide validation for data access."""

    def __init__(self, *args, **kwargs):
        """Initialize the ValidateDataAccessUseCaseMixin and validate data access.

        Args:
        ----
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.validate()

    def _validate_isnull(self, _property):
        """Validate that a property is not null.

        Args:
        ----
            _property (str): The name of the property to validate.

        Returns:
        -------
            Any: The value of the property if it is set.

        Raises:
        ------
            Exception: If the property is not set.
        """
        property_value = getattr(self, _property)
        if not property_value:
            raise Exception(f"{_property} is not set")

        return property_value

    def validate(self):
        """Validate the data access."""
        self._validate_isnull("data_access")


class GetOutputResponseUseCaseMixin:
    """Mixin class to provide a method for getting and setting the output response."""

    def __init__(self, *args, **kwargs):
        """Initialize the GetOutputResponseUseCaseMixin.

        Args:
        ----
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

        self._output_response = self.output_response
        self.output_response = self.get_new_output_response()

    def get_output_response(self):
        """Get the current output response.

        Returns:
        -------
            Any: The current output response.
        """
        return self.output_response

    def get_new_output_response(self):
        """Get a new output response.

        Returns:
        -------
            Any: A new output response instance.
        """
        return self._output_response()


class ValidateOutputResponseUseCaseMixin:
    """Mixin class to provide validation for the output response."""

    def __init__(self, *args, **kwargs):
        """Initialize the ValidateOutputResponseUseCaseMixin and validate output response.

        Args:
        ----
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.validate()

    def _validate_isnull(self, _property):
        """Validate that a property is not null.

        Args:
        ----
            _property (str): The name of the property to validate.

        Returns:
        -------
            Any: The value of the property if it is set.

        Raises:
        ------
            Exception: If the property is not set.
        """
        property_value = getattr(self, _property)
        if not property_value:
            raise Exception(f"{_property} is not set")

        return property_value

    def validate(self):
        """Validate the output response."""
        self._validate_isnull("output_response")
