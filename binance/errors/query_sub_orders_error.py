from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QuerySubOrdersErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QuerySubOrdersError:
    def map(self, response: HttpResponse) -> QuerySubOrdersErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_sub_orders_error_mapper: Final[ErrorMapper[QuerySubOrdersErrorBody]] = _QuerySubOrdersError()
