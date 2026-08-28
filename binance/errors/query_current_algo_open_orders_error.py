from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryCurrentAlgoOpenOrdersErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryCurrentAlgoOpenOrdersError:
    def map(self, response: HttpResponse) -> QueryCurrentAlgoOpenOrdersErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_current_algo_open_orders_error_mapper: Final[
    ErrorMapper[QueryCurrentAlgoOpenOrdersErrorBody]
] = _QueryCurrentAlgoOpenOrdersError()
