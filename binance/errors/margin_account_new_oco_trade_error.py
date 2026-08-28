from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

MarginAccountNewOcoTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _MarginAccountNewOcoTradeError:
    def map(self, response: HttpResponse) -> MarginAccountNewOcoTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


margin_account_new_oco_trade_error_mapper: Final[
    ErrorMapper[MarginAccountNewOcoTradeErrorBody]
] = _MarginAccountNewOcoTradeError()
