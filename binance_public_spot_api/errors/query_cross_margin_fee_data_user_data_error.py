from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryCrossMarginFeeDataUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryCrossMarginFeeDataUserDataError:
    def map(self, response: HttpResponse) -> QueryCrossMarginFeeDataUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_cross_margin_fee_data_user_data_error_mapper: Final[
    ErrorMapper[QueryCrossMarginFeeDataUserDataErrorBody]
] = _QueryCrossMarginFeeDataUserDataError()
