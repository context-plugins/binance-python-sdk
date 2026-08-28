from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryIsolatedMarginAccountInfoUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryIsolatedMarginAccountInfoUserDataError:
    def map(self, response: HttpResponse) -> QueryIsolatedMarginAccountInfoUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_isolated_margin_account_info_user_data_error_mapper: Final[
    ErrorMapper[QueryIsolatedMarginAccountInfoUserDataErrorBody]
] = _QueryIsolatedMarginAccountInfoUserDataError()
