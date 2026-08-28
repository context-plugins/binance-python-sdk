from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1SystemStatusResponse(SdkBaseModel):
    status: int
    """0: normal, 1：system maintenance"""

    msg: str
    """"normal", "system_maintenance"
    """


class SapiV1SystemStatusResponseDict(TypedDict):
    status: int
    msg: str
