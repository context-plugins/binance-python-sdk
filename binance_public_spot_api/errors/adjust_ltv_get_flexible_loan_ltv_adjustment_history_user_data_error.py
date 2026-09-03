from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AdjustLtvGetFlexibleLoanLtvAdjustmentHistoryUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AdjustLtvGetFlexibleLoanLtvAdjustmentHistoryUserDataError:
    def map(self, response: HttpResponse) -> AdjustLtvGetFlexibleLoanLtvAdjustmentHistoryUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data_error_mapper: Final[
    ErrorMapper[AdjustLtvGetFlexibleLoanLtvAdjustmentHistoryUserDataErrorBody]
] = _AdjustLtvGetFlexibleLoanLtvAdjustmentHistoryUserDataError()
