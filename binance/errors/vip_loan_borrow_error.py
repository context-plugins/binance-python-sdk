from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

VipLoanBorrowErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _VipLoanBorrowError:
    def map(self, response: HttpResponse) -> VipLoanBorrowErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


vip_loan_borrow_error_mapper: Final[ErrorMapper[VipLoanBorrowErrorBody]] = _VipLoanBorrowError()
