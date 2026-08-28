from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryUserWalletBalanceUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryUserWalletBalanceUserDataError:
    def map(self, response: HttpResponse) -> QueryUserWalletBalanceUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_user_wallet_balance_user_data_error_mapper: Final[
    ErrorMapper[QueryUserWalletBalanceUserDataErrorBody]
] = _QueryUserWalletBalanceUserDataError()
