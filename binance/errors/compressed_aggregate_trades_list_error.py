from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CompressedAggregateTradesListErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CompressedAggregateTradesListError:
    def map(self, response: HttpResponse) -> CompressedAggregateTradesListErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


compressed_aggregate_trades_list_error_mapper: Final[
    ErrorMapper[CompressedAggregateTradesListErrorBody]
] = _CompressedAggregateTradesListError()
