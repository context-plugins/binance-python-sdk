from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

TimeWeightedAveragePriceTwapNewOrderErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _TimeWeightedAveragePriceTwapNewOrderError:
    def map(self, response: HttpResponse) -> TimeWeightedAveragePriceTwapNewOrderErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


time_weighted_average_price_twap_new_order_error_mapper: Final[
    ErrorMapper[TimeWeightedAveragePriceTwapNewOrderErrorBody]
] = _TimeWeightedAveragePriceTwapNewOrderError()
