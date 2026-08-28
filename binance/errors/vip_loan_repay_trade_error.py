from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

VipLoanRepayTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _VipLoanRepayTradeError:
    def map(self, response: HttpResponse) -> VipLoanRepayTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


vip_loan_repay_trade_error_mapper: Final[ErrorMapper[VipLoanRepayTradeErrorBody]] = _VipLoanRepayTradeError()
