from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Error(SdkBaseModel):
    code: int
    """Error code"""

    msg: str
    """Error message"""


class ErrorDict(TypedDict):
    code: int
    msg: str
