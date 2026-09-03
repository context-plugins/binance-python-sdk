from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CancelAlgoOrderTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CancelAlgoOrderTradeError:
    def map(self, response: HttpResponse) -> CancelAlgoOrderTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


cancel_algo_order_trade_error_mapper: Final[ErrorMapper[CancelAlgoOrderTradeErrorBody]] = _CancelAlgoOrderTradeError()
