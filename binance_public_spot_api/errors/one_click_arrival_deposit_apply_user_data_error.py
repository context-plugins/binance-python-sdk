from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

OneClickArrivalDepositApplyUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _OneClickArrivalDepositApplyUserDataError:
    def map(self, response: HttpResponse) -> OneClickArrivalDepositApplyUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


one_click_arrival_deposit_apply_user_data_error_mapper: Final[
    ErrorMapper[OneClickArrivalDepositApplyUserDataErrorBody]
] = _OneClickArrivalDepositApplyUserDataError()
