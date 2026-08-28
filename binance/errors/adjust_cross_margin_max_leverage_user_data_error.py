from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AdjustCrossMarginMaxLeverageUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AdjustCrossMarginMaxLeverageUserDataError:
    def map(self, response: HttpResponse) -> AdjustCrossMarginMaxLeverageUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


adjust_cross_margin_max_leverage_user_data_error_mapper: Final[
    ErrorMapper[AdjustCrossMarginMaxLeverageUserDataErrorBody]
] = _AdjustCrossMarginMaxLeverageUserDataError()
