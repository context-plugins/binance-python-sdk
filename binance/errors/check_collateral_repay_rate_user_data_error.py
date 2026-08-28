from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CheckCollateralRepayRateUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CheckCollateralRepayRateUserDataError:
    def map(self, response: HttpResponse) -> CheckCollateralRepayRateUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


check_collateral_repay_rate_user_data_error_mapper: Final[
    ErrorMapper[CheckCollateralRepayRateUserDataErrorBody]
] = _CheckCollateralRepayRateUserDataError()
