from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

PingKeepAliveAListenKeyUserStream2ErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _PingKeepAliveAListenKeyUserStream2Error:
    def map(self, response: HttpResponse) -> PingKeepAliveAListenKeyUserStream2ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


ping_keep_alive_a_listen_key_user_stream2_error_mapper: Final[
    ErrorMapper[PingKeepAliveAListenKeyUserStream2ErrorBody]
] = _PingKeepAliveAListenKeyUserStream2Error()
