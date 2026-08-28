from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CrossMarginCollateralRatioMarketDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CrossMarginCollateralRatioMarketDataError:
    def map(self, response: HttpResponse) -> CrossMarginCollateralRatioMarketDataErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


cross_margin_collateral_ratio_market_data_error_mapper: Final[
    ErrorMapper[CrossMarginCollateralRatioMarketDataErrorBody]
] = _CrossMarginCollateralRatioMarketDataError()
