from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

MarginAccountNewOtoTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _MarginAccountNewOtoTradeError:
    def map(self, response: HttpResponse) -> MarginAccountNewOtoTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


margin_account_new_oto_trade_error_mapper: Final[
    ErrorMapper[MarginAccountNewOtoTradeErrorBody]
] = _MarginAccountNewOtoTradeError()
