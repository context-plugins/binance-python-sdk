from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

OneTimeTransactionTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _OneTimeTransactionTradeError:
    def map(self, response: HttpResponse) -> OneTimeTransactionTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


one_time_transaction_trade_error_mapper: Final[
    ErrorMapper[OneTimeTransactionTradeErrorBody]
] = _OneTimeTransactionTradeError()
