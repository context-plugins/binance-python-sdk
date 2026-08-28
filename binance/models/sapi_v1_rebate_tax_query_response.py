from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data23 import Data23, Data23Dict


class SapiV1RebateTaxQueryResponse(SdkBaseModel):
    status: str
    type_: str = Field(alias="type")
    code: str
    data: Data23


class SapiV1RebateTaxQueryResponseDict(TypedDict):
    status: str
    type_: str
    code: str
    data: Data23 | Data23Dict
