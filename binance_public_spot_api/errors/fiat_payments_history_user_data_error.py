from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

FiatPaymentsHistoryUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _FiatPaymentsHistoryUserDataError:
    def map(self, response: HttpResponse) -> FiatPaymentsHistoryUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


fiat_payments_history_user_data_error_mapper: Final[
    ErrorMapper[FiatPaymentsHistoryUserDataErrorBody]
] = _FiatPaymentsHistoryUserDataError()
