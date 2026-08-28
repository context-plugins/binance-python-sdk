from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

RedeemLockedProductTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RedeemLockedProductTradeError:
    def map(self, response: HttpResponse) -> RedeemLockedProductTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


redeem_locked_product_trade_error_mapper: Final[
    ErrorMapper[RedeemLockedProductTradeErrorBody]
] = _RedeemLockedProductTradeError()
