from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CloseAListenKeyUserStream3ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CloseAListenKeyUserStream3Error:
    def map(self, response: HttpResponse) -> CloseAListenKeyUserStream3ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


close_a_listen_key_user_stream3_error_mapper: Final[
    ErrorMapper[CloseAListenKeyUserStream3ErrorBody]
] = _CloseAListenKeyUserStream3Error()
