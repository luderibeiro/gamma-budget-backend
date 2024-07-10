from unittest.mock import Mock, patch

import pytest
from budget.api.v1.mixins import (
    ExecuteUseCaseOnDestroyMixin,
    ExecuteUseCaseOnGetMixin,
)
from rest_framework import status
from rest_framework.response import Response


@pytest.fixture
def mock_request():
    return Mock()


@pytest.fixture
def execute_use_case_on_get_mixin():
    return ExecuteUseCaseOnGetMixin()


def test_get_method(execute_use_case_on_get_mixin, mock_request):
    with patch.object(
        execute_use_case_on_get_mixin,
        "execute_use_case_retrieve",
        return_value=Mock(get_response=Mock(return_value=Response(data={"test": "data"}, status=status.HTTP_200_OK))),
    ):
        response = execute_use_case_on_get_mixin.get(mock_request)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {"test": "data"}

    # Test exception handling (example: HTTP 400 error)
    with patch.object(
        execute_use_case_on_get_mixin, "execute_use_case_retrieve", side_effect=execute_use_case_on_get_mixin.Http400Error("Bad request")
    ):
        response = execute_use_case_on_get_mixin.get(mock_request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.fixture
def execute_use_case_on_destroy_mixin():
    return ExecuteUseCaseOnDestroyMixin()


def test_delete_method(execute_use_case_on_destroy_mixin, mock_request):
    with patch.object(
        execute_use_case_on_destroy_mixin,
        "execute_use_case_destroy",
        return_value=Mock(get_response=Mock(return_value=Response(data={"test": "data"}, status=status.HTTP_200_OK))),
    ):
        response = execute_use_case_on_destroy_mixin.delete(mock_request)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {"test": "data"}

    # Test exception handling (example: HTTP 400 error)
    with (
        pytest.raises(ExecuteUseCaseOnGetMixin.Http400Error),
        patch.object(execute_use_case_on_destroy_mixin, "execute_use_case_destroy", side_effect=ExecuteUseCaseOnGetMixin.Http400Error("Bad request")),
    ):
        response = execute_use_case_on_destroy_mixin.delete(mock_request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
