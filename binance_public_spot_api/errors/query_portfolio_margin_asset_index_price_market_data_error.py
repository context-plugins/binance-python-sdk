from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryPortfolioMarginAssetIndexPriceMarketDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryPortfolioMarginAssetIndexPriceMarketDataError:
    def map(self, response: HttpResponse) -> QueryPortfolioMarginAssetIndexPriceMarketDataErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_portfolio_margin_asset_index_price_market_data_error_mapper: Final[
    ErrorMapper[QueryPortfolioMarginAssetIndexPriceMarketDataErrorBody]
] = _QueryPortfolioMarginAssetIndexPriceMarketDataError()
