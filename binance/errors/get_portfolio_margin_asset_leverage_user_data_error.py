from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetPortfolioMarginAssetLeverageUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetPortfolioMarginAssetLeverageUserDataError:
    def map(self, response: HttpResponse) -> GetPortfolioMarginAssetLeverageUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_portfolio_margin_asset_leverage_user_data_error_mapper: Final[
    ErrorMapper[GetPortfolioMarginAssetLeverageUserDataErrorBody]
] = _GetPortfolioMarginAssetLeverageUserDataError()
