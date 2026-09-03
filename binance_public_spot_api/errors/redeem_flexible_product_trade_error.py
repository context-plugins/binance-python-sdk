from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

RedeemFlexibleProductTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RedeemFlexibleProductTradeError:
    def map(self, response: HttpResponse) -> RedeemFlexibleProductTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


redeem_flexible_product_trade_error_mapper: Final[
    ErrorMapper[RedeemFlexibleProductTradeErrorBody]
] = _RedeemFlexibleProductTradeError()
