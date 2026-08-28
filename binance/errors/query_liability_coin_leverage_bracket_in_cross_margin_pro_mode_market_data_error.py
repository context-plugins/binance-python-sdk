from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryLiabilityCoinLeverageBracketInCrossMarginProModeMarketDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryLiabilityCoinLeverageBracketInCrossMarginProModeMarketDataError:
    def map(self, response: HttpResponse) -> QueryLiabilityCoinLeverageBracketInCrossMarginProModeMarketDataErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data_error_mapper: Final[
    ErrorMapper[QueryLiabilityCoinLeverageBracketInCrossMarginProModeMarketDataErrorBody]
] = _QueryLiabilityCoinLeverageBracketInCrossMarginProModeMarketDataError()
