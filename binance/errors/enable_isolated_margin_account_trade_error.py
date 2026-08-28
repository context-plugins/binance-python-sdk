from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

EnableIsolatedMarginAccountTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EnableIsolatedMarginAccountTradeError:
    def map(self, response: HttpResponse) -> EnableIsolatedMarginAccountTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


enable_isolated_margin_account_trade_error_mapper: Final[
    ErrorMapper[EnableIsolatedMarginAccountTradeErrorBody]
] = _EnableIsolatedMarginAccountTradeError()
