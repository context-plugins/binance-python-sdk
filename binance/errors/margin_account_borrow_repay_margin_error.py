from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

MarginAccountBorrowRepayMarginErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _MarginAccountBorrowRepayMarginError:
    def map(self, response: HttpResponse) -> MarginAccountBorrowRepayMarginErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


margin_account_borrow_repay_margin_error_mapper: Final[
    ErrorMapper[MarginAccountBorrowRepayMarginErrorBody]
] = _MarginAccountBorrowRepayMarginError()
