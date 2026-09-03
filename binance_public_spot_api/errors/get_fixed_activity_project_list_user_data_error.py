from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetFixedActivityProjectListUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetFixedActivityProjectListUserDataError:
    def map(self, response: HttpResponse) -> GetFixedActivityProjectListUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_fixed_activity_project_list_user_data_error_mapper: Final[
    ErrorMapper[GetFixedActivityProjectListUserDataErrorBody]
] = _GetFixedActivityProjectListUserDataError()
