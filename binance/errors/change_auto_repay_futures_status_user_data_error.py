from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ChangeAutoRepayFuturesStatusUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ChangeAutoRepayFuturesStatusUserDataError:
    def map(self, response: HttpResponse) -> ChangeAutoRepayFuturesStatusUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


change_auto_repay_futures_status_user_data_error_mapper: Final[
    ErrorMapper[ChangeAutoRepayFuturesStatusUserDataErrorBody]
] = _ChangeAutoRepayFuturesStatusUserDataError()
