from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

RepayFuturesNegativeBalanceUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RepayFuturesNegativeBalanceUserDataError:
    def map(self, response: HttpResponse) -> RepayFuturesNegativeBalanceUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


repay_futures_negative_balance_user_data_error_mapper: Final[
    ErrorMapper[RepayFuturesNegativeBalanceUserDataErrorBody]
] = _RepayFuturesNegativeBalanceUserDataError()
