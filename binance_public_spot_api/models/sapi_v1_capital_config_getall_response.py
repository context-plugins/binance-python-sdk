from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .network_list import NetworkList, NetworkListDict


class SapiV1CapitalConfigGetallResponse(SdkBaseModel):
    coin: str
    deposit_all_enable: bool = Field(alias="depositAllEnable")
    free: str
    freeze: str
    ipoable: str
    ipoing: str
    is_legal_money: bool = Field(alias="isLegalMoney")
    locked: str
    name: str
    network_list: list[NetworkList] = Field(alias="networkList")
    storage: str
    trading: bool
    withdraw_all_enable: bool = Field(alias="withdrawAllEnable")
    withdrawing: str


class SapiV1CapitalConfigGetallResponseDict(TypedDict):
    coin: str
    deposit_all_enable: bool
    free: str
    freeze: str
    ipoable: str
    ipoing: str
    is_legal_money: bool
    locked: str
    name: str
    network_list: list[NetworkList | NetworkListDict]
    storage: str
    trading: bool
    withdraw_all_enable: bool
    withdrawing: str
