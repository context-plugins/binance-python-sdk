from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryApplicationStatusUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryApplicationStatusUserDataError:
    def map(self, response: HttpResponse) -> QueryApplicationStatusUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_application_status_user_data_error_mapper: Final[
    ErrorMapper[QueryApplicationStatusUserDataErrorBody]
] = _QueryApplicationStatusUserDataError()
