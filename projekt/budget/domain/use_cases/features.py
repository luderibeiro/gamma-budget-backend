from typing import Generic, Type, TypeVar

DataAccessT = TypeVar("DataAccessT")
GatewayT = TypeVar("GatewayT")


class GetDataAccessUseCaseMixin(Generic[DataAccessT]):
    data_access: Type[DataAccessT]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_data_access(self) -> DataAccessT:
        return self.data_access()


class ValidateDataAccessUseCaseMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validate()

    def _validate_isnull(self, _property):
        property_value = getattr(self, _property)
        if not property_value:
            raise Exception("{} is not set".format(_property))

        return property_value

    def validate(self):
        self._validate_isnull("data_access")


class GetOutputResponseUseCaseMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._output_response = self.output_response
        self.output_response = self.get_new_output_response()

    def get_output_response(self):
        return self.output_response

    def get_new_output_response(self):
        return self._output_response()


class ValidateOutputResponseUseCaseMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validate()

    def _validate_isnull(self, _property):
        property_value = getattr(self, _property)
        if not property_value:
            raise Exception("{} is not set".format(_property))

        return property_value

    def validate(self):
        self._validate_isnull("output_response")
        self.validate()

    def _validate_isnull(self, _property):
        property_value = getattr(self, _property)
        if not property_value:
            raise Exception("{} is not set".format(_property))

        return property_value

    def validate(self):
        self._validate_isnull("output_response")
