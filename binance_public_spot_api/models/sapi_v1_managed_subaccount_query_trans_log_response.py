from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .manager_sub_transfer_history_vo2 import ManagerSubTransferHistoryVo2, ManagerSubTransferHistoryVo2Dict


class SapiV1ManagedSubaccountQueryTransLogResponse(SdkBaseModel):
    count: int
    manager_sub_transfer_history_vos: list[ManagerSubTransferHistoryVo2] = Field(alias="managerSubTransferHistoryVos")


class SapiV1ManagedSubaccountQueryTransLogResponseDict(TypedDict):
    count: int
    manager_sub_transfer_history_vos: list[ManagerSubTransferHistoryVo2 | ManagerSubTransferHistoryVo2Dict]
