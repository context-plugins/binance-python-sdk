from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

OrderBookErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _OrderBookError:
    def map(self, response: HttpResponse) -> OrderBookErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


order_book_error_mapper: Final[ErrorMapper[OrderBookErrorBody]] = _OrderBookError()
