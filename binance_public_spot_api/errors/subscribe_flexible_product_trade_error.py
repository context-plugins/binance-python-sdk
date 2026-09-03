from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SubscribeFlexibleProductTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SubscribeFlexibleProductTradeError:
    def map(self, response: HttpResponse) -> SubscribeFlexibleProductTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


subscribe_flexible_product_trade_error_mapper: Final[
    ErrorMapper[SubscribeFlexibleProductTradeErrorBody]
] = _SubscribeFlexibleProductTradeError()
