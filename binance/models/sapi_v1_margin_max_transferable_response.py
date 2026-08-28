from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginMaxTransferableResponse(SdkBaseModel):
    amount: str
    """Account's currently max borrowable amount with sufficient system availability"""

    borrow_limit: str = Field(alias="borrowLimit")
    """Max borrowable amount limited by the account level"""


class SapiV1MarginMaxTransferableResponseDict(TypedDict):
    amount: str
    borrow_limit: str
