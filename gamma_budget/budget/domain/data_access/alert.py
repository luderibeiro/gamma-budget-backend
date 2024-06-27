from abc import ABCMeta, abstractmethod

from budget.domain.entities.alert import Alert


class AbstractBaseAlertCreateDataAccess(metaclass=ABCMeta):
    """Base class for alert create data access."""

    @abstractmethod
    def create_alert(self, data: dict, user_id: int) -> Alert | None:
        pass


class AbstractBaseAlertListDataAccess(metaclass=ABCMeta):
    """Base class for alert list data access."""

    @abstractmethod
    def get_alerts(self, user_id: int) -> list[Alert] | None:
        pass


class AbstractBaseAlertUpdateDataAccess(metaclass=ABCMeta):
    """Base class for alert update data access."""

    @abstractmethod
    def get_alert(self, alert_id: int, user_id: int) -> Alert | None:
        pass

    @abstractmethod
    def update_alert(self, user_id: int, alert_id: str, data: dict) -> Alert | None:
        pass


class AbstractBaseAlertDeleteDataAccess(metaclass=ABCMeta):
    """Base class for alert delete data access."""

    @abstractmethod
    def get_alert(self, alert_id: int, user_id: int) -> Alert | None:
        pass

    @abstractmethod
    def delete_alert(self, user_id: int, alert_id: str) -> bool:
        pass
