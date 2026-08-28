from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryIndexLinkedPlanPositionDetailsUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryIndexLinkedPlanPositionDetailsUserDataError:
    def map(self, response: HttpResponse) -> QueryIndexLinkedPlanPositionDetailsUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_index_linked_plan_position_details_user_data_error_mapper: Final[
    ErrorMapper[QueryIndexLinkedPlanPositionDetailsUserDataErrorBody]
] = _QueryIndexLinkedPlanPositionDetailsUserDataError()
