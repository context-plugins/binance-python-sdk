from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CancelAlgoOrderErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CancelAlgoOrderError:
    def map(self, response: HttpResponse) -> CancelAlgoOrderErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


cancel_algo_order_error_mapper: Final[ErrorMapper[CancelAlgoOrderErrorBody]] = _CancelAlgoOrderError()
