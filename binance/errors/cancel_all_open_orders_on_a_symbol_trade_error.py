from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CancelAllOpenOrdersOnASymbolTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CancelAllOpenOrdersOnASymbolTradeError:
    def map(self, response: HttpResponse) -> CancelAllOpenOrdersOnASymbolTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


cancel_all_open_orders_on_a_symbol_trade_error_mapper: Final[
    ErrorMapper[CancelAllOpenOrdersOnASymbolTradeErrorBody]
] = _CancelAllOpenOrdersOnASymbolTradeError()
