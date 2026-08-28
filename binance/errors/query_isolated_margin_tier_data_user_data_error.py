from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryIsolatedMarginTierDataUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryIsolatedMarginTierDataUserDataError:
    def map(self, response: HttpResponse) -> QueryIsolatedMarginTierDataUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_isolated_margin_tier_data_user_data_error_mapper: Final[
    ErrorMapper[QueryIsolatedMarginTierDataUserDataErrorBody]
] = _QueryIsolatedMarginTierDataUserDataError()
