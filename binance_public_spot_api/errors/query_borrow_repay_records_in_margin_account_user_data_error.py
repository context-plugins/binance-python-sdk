from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryBorrowRepayRecordsInMarginAccountUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryBorrowRepayRecordsInMarginAccountUserDataError:
    def map(self, response: HttpResponse) -> QueryBorrowRepayRecordsInMarginAccountUserDataErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_borrow_repay_records_in_margin_account_user_data_error_mapper: Final[
    ErrorMapper[QueryBorrowRepayRecordsInMarginAccountUserDataErrorBody]
] = _QueryBorrowRepayRecordsInMarginAccountUserDataError()
