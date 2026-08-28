from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

FetchRsaPublicKeyUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _FetchRsaPublicKeyUserDataError:
    def map(self, response: HttpResponse) -> FetchRsaPublicKeyUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


fetch_rsa_public_key_user_data_error_mapper: Final[
    ErrorMapper[FetchRsaPublicKeyUserDataErrorBody]
] = _FetchRsaPublicKeyUserDataError()
