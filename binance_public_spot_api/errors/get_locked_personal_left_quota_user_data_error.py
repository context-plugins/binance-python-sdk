from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLockedPersonalLeftQuotaUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLockedPersonalLeftQuotaUserDataError:
    def map(self, response: HttpResponse) -> GetLockedPersonalLeftQuotaUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_locked_personal_left_quota_user_data_error_mapper: Final[
    ErrorMapper[GetLockedPersonalLeftQuotaUserDataErrorBody]
] = _GetLockedPersonalLeftQuotaUserDataError()
