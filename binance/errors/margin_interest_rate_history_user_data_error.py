from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

MarginInterestRateHistoryUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _MarginInterestRateHistoryUserDataError:
    def map(self, response: HttpResponse) -> MarginInterestRateHistoryUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


margin_interest_rate_history_user_data_error_mapper: Final[
    ErrorMapper[MarginInterestRateHistoryUserDataErrorBody]
] = _MarginInterestRateHistoryUserDataError()
