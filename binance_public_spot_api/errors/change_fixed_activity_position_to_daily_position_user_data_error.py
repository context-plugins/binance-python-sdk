from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ChangeFixedActivityPositionToDailyPositionUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ChangeFixedActivityPositionToDailyPositionUserDataError:
    def map(self, response: HttpResponse) -> ChangeFixedActivityPositionToDailyPositionUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


change_fixed_activity_position_to_daily_position_user_data_error_mapper: Final[
    ErrorMapper[ChangeFixedActivityPositionToDailyPositionUserDataErrorBody]
] = _ChangeFixedActivityPositionToDailyPositionUserDataError()
