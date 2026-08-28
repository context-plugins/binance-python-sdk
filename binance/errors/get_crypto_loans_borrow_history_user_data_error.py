from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetCryptoLoansBorrowHistoryUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetCryptoLoansBorrowHistoryUserDataError:
    def map(self, response: HttpResponse) -> GetCryptoLoansBorrowHistoryUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_crypto_loans_borrow_history_user_data_error_mapper: Final[
    ErrorMapper[GetCryptoLoansBorrowHistoryUserDataErrorBody]
] = _GetCryptoLoansBorrowHistoryUserDataError()
