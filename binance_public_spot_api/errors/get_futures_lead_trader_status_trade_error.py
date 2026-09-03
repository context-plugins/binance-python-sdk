from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetFuturesLeadTraderStatusTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetFuturesLeadTraderStatusTradeError:
    def map(self, response: HttpResponse) -> GetFuturesLeadTraderStatusTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_futures_lead_trader_status_trade_error_mapper: Final[
    ErrorMapper[GetFuturesLeadTraderStatusTradeErrorBody]
] = _GetFuturesLeadTraderStatusTradeError()
