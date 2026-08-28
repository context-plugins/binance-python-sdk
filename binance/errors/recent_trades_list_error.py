from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

RecentTradesListErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RecentTradesListError:
    def map(self, response: HttpResponse) -> RecentTradesListErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


recent_trades_list_error_mapper: Final[ErrorMapper[RecentTradesListErrorBody]] = _RecentTradesListError()
