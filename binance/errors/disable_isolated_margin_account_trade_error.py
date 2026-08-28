from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DisableIsolatedMarginAccountTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DisableIsolatedMarginAccountTradeError:
    def map(self, response: HttpResponse) -> DisableIsolatedMarginAccountTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


disable_isolated_margin_account_trade_error_mapper: Final[
    ErrorMapper[DisableIsolatedMarginAccountTradeErrorBody]
] = _DisableIsolatedMarginAccountTradeError()
