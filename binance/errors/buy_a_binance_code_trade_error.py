from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

BuyABinanceCodeTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _BuyABinanceCodeTradeError:
    def map(self, response: HttpResponse) -> BuyABinanceCodeTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


buy_a_binance_code_trade_error_mapper: Final[ErrorMapper[BuyABinanceCodeTradeErrorBody]] = _BuyABinanceCodeTradeError()
