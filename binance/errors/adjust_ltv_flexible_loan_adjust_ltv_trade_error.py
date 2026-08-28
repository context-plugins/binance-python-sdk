from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AdjustLtvFlexibleLoanAdjustLtvTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AdjustLtvFlexibleLoanAdjustLtvTradeError:
    def map(self, response: HttpResponse) -> AdjustLtvFlexibleLoanAdjustLtvTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


adjust_ltv_flexible_loan_adjust_ltv_trade_error_mapper: Final[
    ErrorMapper[AdjustLtvFlexibleLoanAdjustLtvTradeErrorBody]
] = _AdjustLtvFlexibleLoanAdjustLtvTradeError()
