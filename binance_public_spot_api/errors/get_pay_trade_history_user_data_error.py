from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetPayTradeHistoryUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetPayTradeHistoryUserDataError:
    def map(self, response: HttpResponse) -> GetPayTradeHistoryUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_pay_trade_history_user_data_error_mapper: Final[
    ErrorMapper[GetPayTradeHistoryUserDataErrorBody]
] = _GetPayTradeHistoryUserDataError()
