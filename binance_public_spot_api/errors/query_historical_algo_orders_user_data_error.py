from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryHistoricalAlgoOrdersUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryHistoricalAlgoOrdersUserDataError:
    def map(self, response: HttpResponse) -> QueryHistoricalAlgoOrdersUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_historical_algo_orders_user_data_error_mapper: Final[
    ErrorMapper[QueryHistoricalAlgoOrdersUserDataErrorBody]
] = _QueryHistoricalAlgoOrdersUserDataError()
