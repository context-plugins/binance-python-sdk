from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CheckLockedValueOfVipCollateralAccountUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CheckLockedValueOfVipCollateralAccountUserDataError:
    def map(self, response: HttpResponse) -> CheckLockedValueOfVipCollateralAccountUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


check_locked_value_of_vip_collateral_account_user_data_error_mapper: Final[
    ErrorMapper[CheckLockedValueOfVipCollateralAccountUserDataErrorBody]
] = _CheckLockedValueOfVipCollateralAccountUserDataError()
