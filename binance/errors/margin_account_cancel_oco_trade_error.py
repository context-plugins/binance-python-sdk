from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

MarginAccountCancelOcoTradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _MarginAccountCancelOcoTradeError:
    def map(self, response: HttpResponse) -> MarginAccountCancelOcoTradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


margin_account_cancel_oco_trade_error_mapper: Final[
    ErrorMapper[MarginAccountCancelOcoTradeErrorBody]
] = _MarginAccountCancelOcoTradeError()
