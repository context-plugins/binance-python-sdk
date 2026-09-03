from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

MarginAccountCancelOrderTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _MarginAccountCancelOrderTradeError:
    def map(self, response: HttpResponse) -> MarginAccountCancelOrderTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


margin_account_cancel_order_trade_error_mapper: Final[
    ErrorMapper[MarginAccountCancelOrderTradeErrorBody]
] = _MarginAccountCancelOrderTradeError()
