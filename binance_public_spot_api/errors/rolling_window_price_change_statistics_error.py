from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

RollingWindowPriceChangeStatisticsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RollingWindowPriceChangeStatisticsError:
    def map(self, response: HttpResponse) -> RollingWindowPriceChangeStatisticsErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


rolling_window_price_change_statistics_error_mapper: Final[
    ErrorMapper[RollingWindowPriceChangeStatisticsErrorBody]
] = _RollingWindowPriceChangeStatisticsError()
