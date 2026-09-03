from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

NewOrderListOtoTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _NewOrderListOtoTradeError:
    def map(self, response: HttpResponse) -> NewOrderListOtoTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


new_order_list_oto_trade_error_mapper: Final[ErrorMapper[NewOrderListOtoTradeErrorBody]] = _NewOrderListOtoTradeError()
