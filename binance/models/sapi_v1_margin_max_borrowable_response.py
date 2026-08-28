from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginMaxBorrowableResponse(SdkBaseModel):
    amount: str
    """account's currently max borrowable amount with sufficient system availability"""

    borrow_limit: str = Field(alias="borrowLimit")
    """max borrowable amount limited by the account level"""


class SapiV1MarginMaxBorrowableResponseDict(TypedDict):
    amount: str
    borrow_limit: str
