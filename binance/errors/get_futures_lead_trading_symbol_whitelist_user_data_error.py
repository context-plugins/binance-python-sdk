from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetFuturesLeadTradingSymbolWhitelistUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetFuturesLeadTradingSymbolWhitelistUserDataError:
    def map(self, response: HttpResponse) -> GetFuturesLeadTradingSymbolWhitelistUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_futures_lead_trading_symbol_whitelist_user_data_error_mapper: Final[
    ErrorMapper[GetFuturesLeadTradingSymbolWhitelistUserDataErrorBody]
] = _GetFuturesLeadTradingSymbolWhitelistUserDataError()
