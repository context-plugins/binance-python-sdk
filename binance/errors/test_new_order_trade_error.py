from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

TestNewOrderTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _TestNewOrderTradeError:
    def map(self, response: HttpResponse) -> TestNewOrderTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


test_new_order_trade_error_mapper: Final[ErrorMapper[TestNewOrderTradeErrorBody]] = _TestNewOrderTradeError()
