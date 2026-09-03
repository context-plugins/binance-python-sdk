from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CloseAListenKeyUserStream2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CloseAListenKeyUserStream2Error:
    def map(self, response: HttpResponse) -> CloseAListenKeyUserStream2ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


close_a_listen_key_user_stream2_error_mapper: Final[
    ErrorMapper[CloseAListenKeyUserStream2ErrorBody]
] = _CloseAListenKeyUserStream2Error()
