from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

RepayFlexibleLoanRepayTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RepayFlexibleLoanRepayTradeError:
    def map(self, response: HttpResponse) -> RepayFlexibleLoanRepayTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


repay_flexible_loan_repay_trade_error_mapper: Final[
    ErrorMapper[RepayFlexibleLoanRepayTradeErrorBody]
] = _RepayFlexibleLoanRepayTradeError()
