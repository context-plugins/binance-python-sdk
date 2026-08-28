from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetFutureAccountTransactionHistoryListUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetFutureAccountTransactionHistoryListUserDataError:
    def map(self, response: HttpResponse) -> GetFutureAccountTransactionHistoryListUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_future_account_transaction_history_list_user_data_error_mapper: Final[
    ErrorMapper[GetFutureAccountTransactionHistoryListUserDataErrorBody]
] = _GetFutureAccountTransactionHistoryListUserDataError()
