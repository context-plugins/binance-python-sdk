from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

IndexLinkedPlanRebalanceDetailsUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _IndexLinkedPlanRebalanceDetailsUserDataError:
    def map(self, response: HttpResponse) -> IndexLinkedPlanRebalanceDetailsUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


index_linked_plan_rebalance_details_user_data_error_mapper: Final[
    ErrorMapper[IndexLinkedPlanRebalanceDetailsUserDataErrorBody]
] = _IndexLinkedPlanRebalanceDetailsUserDataError()
