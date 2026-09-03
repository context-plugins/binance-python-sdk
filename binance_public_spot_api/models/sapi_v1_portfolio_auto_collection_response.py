from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1PortfolioAutoCollectionResponse(SdkBaseModel):
    msg: str


class SapiV1PortfolioAutoCollectionResponseDict(TypedDict):
    msg: str
