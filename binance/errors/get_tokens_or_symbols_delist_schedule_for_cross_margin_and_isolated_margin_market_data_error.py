from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetTokensOrSymbolsDelistScheduleForCrossMarginAndIsolatedMarginMarketDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetTokensOrSymbolsDelistScheduleForCrossMarginAndIsolatedMarginMarketDataError:
    def map(
        self, response: HttpResponse
    ) -> GetTokensOrSymbolsDelistScheduleForCrossMarginAndIsolatedMarginMarketDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data_error_mapper: Final[
    ErrorMapper[GetTokensOrSymbolsDelistScheduleForCrossMarginAndIsolatedMarginMarketDataErrorBody]
] = _GetTokensOrSymbolsDelistScheduleForCrossMarginAndIsolatedMarginMarketDataError()
