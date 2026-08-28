from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

RepayGetFlexibleLoanRepaymentHistoryUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RepayGetFlexibleLoanRepaymentHistoryUserDataError:
    def map(self, response: HttpResponse) -> RepayGetFlexibleLoanRepaymentHistoryUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


repay_get_flexible_loan_repayment_history_user_data_error_mapper: Final[
    ErrorMapper[RepayGetFlexibleLoanRepaymentHistoryUserDataErrorBody]
] = _RepayGetFlexibleLoanRepaymentHistoryUserDataError()
