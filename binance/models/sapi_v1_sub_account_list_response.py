from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sub_account import SubAccount, SubAccountDict


class SapiV1SubAccountListResponse(SdkBaseModel):
    sub_accounts: list[SubAccount] = Field(alias="subAccounts")


class SapiV1SubAccountListResponseDict(TypedDict):
    sub_accounts: list[SubAccount | SubAccountDict]
