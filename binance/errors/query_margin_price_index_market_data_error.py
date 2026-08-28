from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryMarginPriceIndexMarketDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryMarginPriceIndexMarketDataError:
    def map(self, response: HttpResponse) -> QueryMarginPriceIndexMarketDataErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_margin_price_index_market_data_error_mapper: Final[
    ErrorMapper[QueryMarginPriceIndexMarketDataErrorBody]
] = _QueryMarginPriceIndexMarketDataError()
