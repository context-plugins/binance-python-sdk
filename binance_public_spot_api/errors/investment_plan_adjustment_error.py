from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

InvestmentPlanAdjustmentErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _InvestmentPlanAdjustmentError:
    def map(self, response: HttpResponse) -> InvestmentPlanAdjustmentErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


investment_plan_adjustment_error_mapper: Final[
    ErrorMapper[InvestmentPlanAdjustmentErrorBody]
] = _InvestmentPlanAdjustmentError()
