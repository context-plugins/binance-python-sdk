from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

KlineCandlestickDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _KlineCandlestickDataError:
    def map(self, response: HttpResponse) -> KlineCandlestickDataErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


kline_candlestick_data_error_mapper: Final[ErrorMapper[KlineCandlestickDataErrorBody]] = _KlineCandlestickDataError()
