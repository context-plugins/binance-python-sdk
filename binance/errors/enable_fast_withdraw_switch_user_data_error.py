from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

EnableFastWithdrawSwitchUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EnableFastWithdrawSwitchUserDataError:
    def map(self, response: HttpResponse) -> EnableFastWithdrawSwitchUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


enable_fast_withdraw_switch_user_data_error_mapper: Final[
    ErrorMapper[EnableFastWithdrawSwitchUserDataErrorBody]
] = _EnableFastWithdrawSwitchUserDataError()
