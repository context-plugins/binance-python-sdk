from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .exchange_rates import ExchangeRates, ExchangeRatesDict


class SapiV1CapitalContractConvertibleCoinsResponse(SdkBaseModel):
    convert_enabled: bool = Field(alias="convertEnabled")
    coins: list[str]
    exchange_rates: ExchangeRates = Field(alias="exchangeRates")


class SapiV1CapitalContractConvertibleCoinsResponseDict(TypedDict):
    convert_enabled: bool
    coins: list[str]
    exchange_rates: ExchangeRates | ExchangeRatesDict
