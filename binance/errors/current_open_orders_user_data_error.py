from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CurrentOpenOrdersUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CurrentOpenOrdersUserDataError:
    def map(self, response: HttpResponse) -> CurrentOpenOrdersUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


current_open_orders_user_data_error_mapper: Final[
    ErrorMapper[CurrentOpenOrdersUserDataErrorBody]
] = _CurrentOpenOrdersUserDataError()
