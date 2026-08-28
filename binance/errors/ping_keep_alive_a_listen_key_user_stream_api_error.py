from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

PingKeepAliveAListenKeyUserStreamApiErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _PingKeepAliveAListenKeyUserStreamApiError:
    def map(self, response: HttpResponse) -> PingKeepAliveAListenKeyUserStreamApiErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


ping_keep_alive_a_listen_key_user_stream_api_error_mapper: Final[
    ErrorMapper[PingKeepAliveAListenKeyUserStreamApiErrorBody]
] = _PingKeepAliveAListenKeyUserStreamApiError()
