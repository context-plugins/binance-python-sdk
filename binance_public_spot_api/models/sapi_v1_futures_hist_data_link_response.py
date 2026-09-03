from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data20 import Data20, Data20Dict


class SapiV1FuturesHistDataLinkResponse(SdkBaseModel):
    data: list[Data20]


class SapiV1FuturesHistDataLinkResponseDict(TypedDict):
    data: list[Data20 | Data20Dict]
