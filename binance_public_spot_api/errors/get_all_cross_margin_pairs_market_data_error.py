from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetAllCrossMarginPairsMarketDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAllCrossMarginPairsMarketDataError:
    def map(self, response: HttpResponse) -> GetAllCrossMarginPairsMarketDataErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_all_cross_margin_pairs_market_data_error_mapper: Final[
    ErrorMapper[GetAllCrossMarginPairsMarketDataErrorBody]
] = _GetAllCrossMarginPairsMarketDataError()
