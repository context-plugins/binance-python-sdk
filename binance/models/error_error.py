from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ErrorError(SdkBaseModel):
    code: int
    """Error code"""

    msg: str
    """Error message"""


class ErrorErrorDict(TypedDict):
    code: int
    msg: str
