from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SetFlexibleAutoSubscribeUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SetFlexibleAutoSubscribeUserDataError:
    def map(self, response: HttpResponse) -> SetFlexibleAutoSubscribeUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


set_flexible_auto_subscribe_user_data_error_mapper: Final[
    ErrorMapper[SetFlexibleAutoSubscribeUserDataErrorBody]
] = _SetFlexibleAutoSubscribeUserDataError()
