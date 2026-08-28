from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetNftTransactionHistoryUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetNftTransactionHistoryUserDataError:
    def map(self, response: HttpResponse) -> GetNftTransactionHistoryUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_nft_transaction_history_user_data_error_mapper: Final[
    ErrorMapper[GetNftTransactionHistoryUserDataErrorBody]
] = _GetNftTransactionHistoryUserDataError()
