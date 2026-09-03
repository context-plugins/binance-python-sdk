from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .manager_sub_transfer_history_vo import ManagerSubTransferHistoryVo, ManagerSubTransferHistoryVoDict


class SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse(SdkBaseModel):
    count: int
    manager_sub_transfer_history_vos: list[ManagerSubTransferHistoryVo] = Field(alias="managerSubTransferHistoryVos")


class SapiV1ManagedSubaccountQueryTransLogForTradeParentResponseDict(TypedDict):
    count: int
    manager_sub_transfer_history_vos: list[ManagerSubTransferHistoryVo | ManagerSubTransferHistoryVoDict]
