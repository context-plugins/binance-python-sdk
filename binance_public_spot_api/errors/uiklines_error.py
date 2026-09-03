from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

UiklinesErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _UiklinesError:
    def map(self, response: HttpResponse) -> UiklinesErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error](response)
            case _:
                return RawError(response)


uiklines_error_mapper: Final[ErrorMapper[UiklinesErrorBody]] = _UiklinesError()
