from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

PortfolioMarginBankruptcyLoanAmountUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _PortfolioMarginBankruptcyLoanAmountUserDataError:
    def map(self, response: HttpResponse) -> PortfolioMarginBankruptcyLoanAmountUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


portfolio_margin_bankruptcy_loan_amount_user_data_error_mapper: Final[
    ErrorMapper[PortfolioMarginBankruptcyLoanAmountUserDataErrorBody]
] = _PortfolioMarginBankruptcyLoanAmountUserDataError()
