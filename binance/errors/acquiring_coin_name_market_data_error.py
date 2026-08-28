from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AcquiringCoinNameMarketDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AcquiringCoinNameMarketDataError:
    def map(self, response: HttpResponse) -> AcquiringCoinNameMarketDataErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


acquiring_coin_name_market_data_error_mapper: Final[
    ErrorMapper[AcquiringCoinNameMarketDataErrorBody]
] = _AcquiringCoinNameMarketDataError()
