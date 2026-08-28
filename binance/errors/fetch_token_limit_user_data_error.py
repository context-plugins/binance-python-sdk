from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

FetchTokenLimitUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _FetchTokenLimitUserDataError:
    def map(self, response: HttpResponse) -> FetchTokenLimitUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


fetch_token_limit_user_data_error_mapper: Final[
    ErrorMapper[FetchTokenLimitUserDataErrorBody]
] = _FetchTokenLimitUserDataError()
