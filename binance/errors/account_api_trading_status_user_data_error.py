from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AccountApiTradingStatusUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AccountApiTradingStatusUserDataError:
    def map(self, response: HttpResponse) -> AccountApiTradingStatusUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


account_api_trading_status_user_data_error_mapper: Final[
    ErrorMapper[AccountApiTradingStatusUserDataErrorBody]
] = _AccountApiTradingStatusUserDataError()
