from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CryptoLoanCustomizeMarginCallTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CryptoLoanCustomizeMarginCallTradeError:
    def map(self, response: HttpResponse) -> CryptoLoanCustomizeMarginCallTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


crypto_loan_customize_margin_call_trade_error_mapper: Final[
    ErrorMapper[CryptoLoanCustomizeMarginCallTradeErrorBody]
] = _CryptoLoanCustomizeMarginCallTradeError()
