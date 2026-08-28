from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AcquiringAlgorithmMarketDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AcquiringAlgorithmMarketDataError:
    def map(self, response: HttpResponse) -> AcquiringAlgorithmMarketDataErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


acquiring_algorithm_market_data_error_mapper: Final[
    ErrorMapper[AcquiringAlgorithmMarketDataErrorBody]
] = _AcquiringAlgorithmMarketDataError()
