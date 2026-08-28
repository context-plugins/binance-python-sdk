from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryIsolatedMarginFeeDataUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryIsolatedMarginFeeDataUserDataError:
    def map(self, response: HttpResponse) -> QueryIsolatedMarginFeeDataUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_isolated_margin_fee_data_user_data_error_mapper: Final[
    ErrorMapper[QueryIsolatedMarginFeeDataUserDataErrorBody]
] = _QueryIsolatedMarginFeeDataUserDataError()
