from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetInterestHistoryUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetInterestHistoryUserDataError:
    def map(self, response: HttpResponse) -> GetInterestHistoryUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_interest_history_user_data_error_mapper: Final[
    ErrorMapper[GetInterestHistoryUserDataErrorBody]
] = _GetInterestHistoryUserDataError()
