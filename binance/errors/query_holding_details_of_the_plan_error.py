from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryHoldingDetailsOfThePlanErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryHoldingDetailsOfThePlanError:
    def map(self, response: HttpResponse) -> QueryHoldingDetailsOfThePlanErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_holding_details_of_the_plan_error_mapper: Final[
    ErrorMapper[QueryHoldingDetailsOfThePlanErrorBody]
] = _QueryHoldingDetailsOfThePlanError()
