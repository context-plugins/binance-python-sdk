from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data15 import Data15, Data15Dict


class SapiV1MiningHashTransferConfigDetailsListResponse(SdkBaseModel):
    code: int
    msg: str
    data: Data15


class SapiV1MiningHashTransferConfigDetailsListResponseDict(TypedDict):
    code: int
    msg: str
    data: Data15 | Data15Dict
