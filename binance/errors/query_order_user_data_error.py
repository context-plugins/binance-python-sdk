from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryOrderUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryOrderUserDataError:
    def map(self, response: HttpResponse) -> QueryOrderUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_order_user_data_error_mapper: Final[ErrorMapper[QueryOrderUserDataErrorBody]] = _QueryOrderUserDataError()
