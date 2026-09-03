from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

BlvtInfoMarketDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _BlvtInfoMarketDataError:
    def map(self, response: HttpResponse) -> BlvtInfoMarketDataErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


blvt_info_market_data_error_mapper: Final[ErrorMapper[BlvtInfoMarketDataErrorBody]] = _BlvtInfoMarketDataError()
