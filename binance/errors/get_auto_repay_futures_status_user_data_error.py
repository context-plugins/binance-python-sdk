from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetAutoRepayFuturesStatusUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAutoRepayFuturesStatusUserDataError:
    def map(self, response: HttpResponse) -> GetAutoRepayFuturesStatusUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_auto_repay_futures_status_user_data_error_mapper: Final[
    ErrorMapper[GetAutoRepayFuturesStatusUserDataErrorBody]
] = _GetAutoRepayFuturesStatusUserDataError()
