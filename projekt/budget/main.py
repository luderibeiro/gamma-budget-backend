from budget.domain.use_cases import (
    IncomingCreateUseCase,
    IncomingDeleteUseCase,
    IncomingListUseCase,
    IncomingRetrieveUseCase,
    IncomingUpdateUseCase,
)
from budget.repositories import (
    IncomingCreateRepository,
    IncomingDeleteRepository,
    IncomingListRepository,
    IncomingRetrieveRepository,
    IncomingUpdateRepository,
)


def configure():
    IncomingListUseCase.data_access = IncomingListRepository
    IncomingCreateUseCase.data_access = IncomingCreateRepository
    IncomingRetrieveUseCase.data_access = IncomingRetrieveRepository
    IncomingUpdateUseCase.data_access = IncomingUpdateRepository
    IncomingDeleteUseCase.data_access = IncomingDeleteRepository
