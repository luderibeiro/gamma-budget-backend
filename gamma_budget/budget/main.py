from budget.domain.use_cases import (
    IncomingCategoryListUseCase,
    IncomingCreateUseCase,
    IncomingDeleteUseCase,
    IncomingListUseCase,
    IncomingRetrieveUseCase,
    IncomingUpdateUseCase,
    LimitCreateUseCase,
    LimitDeleteUseCase,
    LimitListUseCase,
    LimitUpdateUseCase,
    RevenueCategoryListUseCase,
    RevenueCreateUseCase,
    RevenueDeleteUseCase,
    RevenueListUseCase,
    RevenueRetrieveUseCase,
    RevenueUpdateUseCase,
)
from budget.repositories import (
    IncomingCategoryListRepository,
    IncomingCreateRepository,
    IncomingDeleteRepository,
    IncomingListRepository,
    IncomingRetrieveRepository,
    IncomingUpdateRepository,
    LimitCreateRepository,
    LimitDeleteRepository,
    LimitListRepository,
    LimitUpdateRepository,
    RevenueCategoryListRepository,
    RevenueCreateRepository,
    RevenueDeleteRepository,
    RevenueListRepository,
    RevenueRetrieveRepository,
    RevenueUpdateRepository,
)


def configure():
    IncomingListUseCase.data_access = IncomingListRepository
    IncomingCreateUseCase.data_access = IncomingCreateRepository
    IncomingRetrieveUseCase.data_access = IncomingRetrieveRepository
    IncomingUpdateUseCase.data_access = IncomingUpdateRepository
    IncomingDeleteUseCase.data_access = IncomingDeleteRepository

    RevenueListUseCase.data_access = RevenueListRepository
    RevenueCreateUseCase.data_access = RevenueCreateRepository
    RevenueRetrieveUseCase.data_access = RevenueRetrieveRepository
    RevenueUpdateUseCase.data_access = RevenueUpdateRepository
    RevenueDeleteUseCase.data_access = RevenueDeleteRepository

    IncomingCategoryListUseCase.data_access = IncomingCategoryListRepository
    RevenueCategoryListUseCase.data_access = RevenueCategoryListRepository

    LimitListUseCase.data_access = LimitListRepository
    LimitCreateUseCase.data_access = LimitCreateRepository
    LimitUpdateUseCase.data_access = LimitUpdateRepository
    LimitDeleteUseCase.data_access = LimitDeleteRepository
