from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

MarginAccountNewOtocoTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _MarginAccountNewOtocoTradeError:
    def map(self, response: HttpResponse) -> MarginAccountNewOtocoTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


margin_account_new_otoco_trade_error_mapper: Final[
    ErrorMapper[MarginAccountNewOtocoTradeErrorBody]
] = _MarginAccountNewOtocoTradeError()
