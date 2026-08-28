from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

MarginAccountCancelAllOpenOrdersOnASymbolTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _MarginAccountCancelAllOpenOrdersOnASymbolTradeError:
    def map(self, response: HttpResponse) -> MarginAccountCancelAllOpenOrdersOnASymbolTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


margin_account_cancel_all_open_orders_on_a_symbol_trade_error_mapper: Final[
    ErrorMapper[MarginAccountCancelAllOpenOrdersOnASymbolTradeErrorBody]
] = _MarginAccountCancelAllOpenOrdersOnASymbolTradeError()
