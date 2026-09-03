from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CancelAnExistingOrderAndSendANewOrderTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CancelAnExistingOrderAndSendANewOrderTradeError:
    def map(self, response: HttpResponse) -> CancelAnExistingOrderAndSendANewOrderTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


cancel_an_existing_order_and_send_a_new_order_trade_error_mapper: Final[
    ErrorMapper[CancelAnExistingOrderAndSendANewOrderTradeErrorBody]
] = _CancelAnExistingOrderAndSendANewOrderTradeError()
