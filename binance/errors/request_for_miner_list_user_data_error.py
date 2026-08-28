from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

RequestForMinerListUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RequestForMinerListUserDataError:
    def map(self, response: HttpResponse) -> RequestForMinerListUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


request_for_miner_list_user_data_error_mapper: Final[
    ErrorMapper[RequestForMinerListUserDataErrorBody]
] = _RequestForMinerListUserDataError()
