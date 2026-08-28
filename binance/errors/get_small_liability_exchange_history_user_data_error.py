from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetSmallLiabilityExchangeHistoryUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetSmallLiabilityExchangeHistoryUserDataError:
    def map(self, response: HttpResponse) -> GetSmallLiabilityExchangeHistoryUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_small_liability_exchange_history_user_data_error_mapper: Final[
    ErrorMapper[GetSmallLiabilityExchangeHistoryUserDataErrorBody]
] = _GetSmallLiabilityExchangeHistoryUserDataError()
