from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SubscribeLockedProductTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SubscribeLockedProductTradeError:
    def map(self, response: HttpResponse) -> SubscribeLockedProductTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


subscribe_locked_product_trade_error_mapper: Final[
    ErrorMapper[SubscribeLockedProductTradeErrorBody]
] = _SubscribeLockedProductTradeError()
