from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ToggleBnbBurnOnSpotTradeAndMarginInterestUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ToggleBnbBurnOnSpotTradeAndMarginInterestUserDataError:
    def map(self, response: HttpResponse) -> ToggleBnbBurnOnSpotTradeAndMarginInterestUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data_error_mapper: Final[
    ErrorMapper[ToggleBnbBurnOnSpotTradeAndMarginInterestUserDataErrorBody]
] = _ToggleBnbBurnOnSpotTradeAndMarginInterestUserDataError()
