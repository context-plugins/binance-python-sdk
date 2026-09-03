from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

NewOrderListOtocoTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _NewOrderListOtocoTradeError:
    def map(self, response: HttpResponse) -> NewOrderListOtocoTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


new_order_list_otoco_trade_error_mapper: Final[
    ErrorMapper[NewOrderListOtocoTradeErrorBody]
] = _NewOrderListOtocoTradeError()
