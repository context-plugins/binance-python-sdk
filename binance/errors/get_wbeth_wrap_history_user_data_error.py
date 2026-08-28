from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetWbethWrapHistoryUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetWbethWrapHistoryUserDataError:
    def map(self, response: HttpResponse) -> GetWbethWrapHistoryUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_wbeth_wrap_history_user_data_error_mapper: Final[
    ErrorMapper[GetWbethWrapHistoryUserDataErrorBody]
] = _GetWbethWrapHistoryUserDataError()
