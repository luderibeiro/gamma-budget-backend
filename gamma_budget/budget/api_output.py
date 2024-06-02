from rest_framework import status
from rest_framework.response import Response

from budget.domain.use_cases.base.base import AbstractBaseOutput


class DjangoApiOutput(AbstractBaseOutput):
    """Class responsible for API output."""

    def __init__(self, *args, **kwargs):
        self._data = None

    @property
    def data(self) -> dict:
        return self._data

    @data.setter
    def data(self, value: dict):
        self._data = value

    def get_response(self):
        return Response(self.data, status=status.HTTP_200_OK)
