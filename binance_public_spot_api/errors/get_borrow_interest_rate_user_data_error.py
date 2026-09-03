from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetBorrowInterestRateUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetBorrowInterestRateUserDataError:
    def map(self, response: HttpResponse) -> GetBorrowInterestRateUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_borrow_interest_rate_user_data_error_mapper: Final[
    ErrorMapper[GetBorrowInterestRateUserDataErrorBody]
] = _GetBorrowInterestRateUserDataError()
