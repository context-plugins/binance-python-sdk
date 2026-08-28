from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryCrossMarginAccountDetailsUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryCrossMarginAccountDetailsUserDataError:
    def map(self, response: HttpResponse) -> QueryCrossMarginAccountDetailsUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_cross_margin_account_details_user_data_error_mapper: Final[
    ErrorMapper[QueryCrossMarginAccountDetailsUserDataErrorBody]
] = _QueryCrossMarginAccountDetailsUserDataError()
