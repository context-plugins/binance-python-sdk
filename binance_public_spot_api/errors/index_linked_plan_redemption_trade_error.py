from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

IndexLinkedPlanRedemptionTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _IndexLinkedPlanRedemptionTradeError:
    def map(self, response: HttpResponse) -> IndexLinkedPlanRedemptionTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


index_linked_plan_redemption_trade_error_mapper: Final[
    ErrorMapper[IndexLinkedPlanRedemptionTradeErrorBody]
] = _IndexLinkedPlanRedemptionTradeError()
