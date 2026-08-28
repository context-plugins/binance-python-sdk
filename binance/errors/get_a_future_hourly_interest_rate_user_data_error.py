from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetAFutureHourlyInterestRateUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAFutureHourlyInterestRateUserDataError:
    def map(self, response: HttpResponse) -> GetAFutureHourlyInterestRateUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_a_future_hourly_interest_rate_user_data_error_mapper: Final[
    ErrorMapper[GetAFutureHourlyInterestRateUserDataErrorBody]
] = _GetAFutureHourlyInterestRateUserDataError()
