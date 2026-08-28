from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

HashrateResaleRequestUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _HashrateResaleRequestUserDataError:
    def map(self, response: HttpResponse) -> HashrateResaleRequestUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


hashrate_resale_request_user_data_error_mapper: Final[
    ErrorMapper[HashrateResaleRequestUserDataErrorBody]
] = _HashrateResaleRequestUserDataError()
