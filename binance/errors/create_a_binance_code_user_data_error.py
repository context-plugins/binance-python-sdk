from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CreateABinanceCodeUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateABinanceCodeUserDataError:
    def map(self, response: HttpResponse) -> CreateABinanceCodeUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


create_a_binance_code_user_data_error_mapper: Final[
    ErrorMapper[CreateABinanceCodeUserDataErrorBody]
] = _CreateABinanceCodeUserDataError()
