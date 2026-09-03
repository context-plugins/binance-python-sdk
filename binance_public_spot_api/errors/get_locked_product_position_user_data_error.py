from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetLockedProductPositionUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetLockedProductPositionUserDataError:
    def map(self, response: HttpResponse) -> GetLockedProductPositionUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_locked_product_position_user_data_error_mapper: Final[
    ErrorMapper[GetLockedProductPositionUserDataErrorBody]
] = _GetLockedProductPositionUserDataError()
