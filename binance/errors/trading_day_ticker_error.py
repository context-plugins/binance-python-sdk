from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

TradingDayTickerErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _TradingDayTickerError:
    def map(self, response: HttpResponse) -> TradingDayTickerErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


trading_day_ticker_error_mapper: Final[ErrorMapper[TradingDayTickerErrorBody]] = _TradingDayTickerError()
