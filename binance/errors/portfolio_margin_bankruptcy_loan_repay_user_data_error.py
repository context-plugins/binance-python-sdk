from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

PortfolioMarginBankruptcyLoanRepayUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _PortfolioMarginBankruptcyLoanRepayUserDataError:
    def map(self, response: HttpResponse) -> PortfolioMarginBankruptcyLoanRepayUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


portfolio_margin_bankruptcy_loan_repay_user_data_error_mapper: Final[
    ErrorMapper[PortfolioMarginBankruptcyLoanRepayUserDataErrorBody]
] = _PortfolioMarginBankruptcyLoanRepayUserDataError()
