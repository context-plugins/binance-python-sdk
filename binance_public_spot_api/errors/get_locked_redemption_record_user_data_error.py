from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLockedRedemptionRecordUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLockedRedemptionRecordUserDataError:
    def map(self, response: HttpResponse) -> GetLockedRedemptionRecordUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_locked_redemption_record_user_data_error_mapper: Final[
    ErrorMapper[GetLockedRedemptionRecordUserDataErrorBody]
] = _GetLockedRedemptionRecordUserDataError()
