from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SubAccountEoptionsEnableResponse(SdkBaseModel):
    email: str
    is_e_options_enabled: bool = Field(alias="isEOptionsEnabled")


class SapiV1SubAccountEoptionsEnableResponseDict(TypedDict):
    email: str
    is_e_options_enabled: bool
