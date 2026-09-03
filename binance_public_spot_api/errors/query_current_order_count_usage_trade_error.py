from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryCurrentOrderCountUsageTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryCurrentOrderCountUsageTradeError:
    def map(self, response: HttpResponse) -> QueryCurrentOrderCountUsageTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_current_order_count_usage_trade_error_mapper: Final[
    ErrorMapper[QueryCurrentOrderCountUsageTradeErrorBody]
] = _QueryCurrentOrderCountUsageTradeError()
