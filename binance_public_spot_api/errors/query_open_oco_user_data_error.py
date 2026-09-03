from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryOpenOcoUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryOpenOcoUserDataError:
    def map(self, response: HttpResponse) -> QueryOpenOcoUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_open_oco_user_data_error_mapper: Final[ErrorMapper[QueryOpenOcoUserDataErrorBody]] = _QueryOpenOcoUserDataError()
