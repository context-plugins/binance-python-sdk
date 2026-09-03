from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetFlexibleProductPositionUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetFlexibleProductPositionUserDataError:
    def map(self, response: HttpResponse) -> GetFlexibleProductPositionUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_flexible_product_position_user_data_error_mapper: Final[
    ErrorMapper[GetFlexibleProductPositionUserDataErrorBody]
] = _GetFlexibleProductPositionUserDataError()
