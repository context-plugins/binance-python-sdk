from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ListAllConvertPairsErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ListAllConvertPairsError:
    def map(self, response: HttpResponse) -> ListAllConvertPairsErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


list_all_convert_pairs_error_mapper: Final[ErrorMapper[ListAllConvertPairsErrorBody]] = _ListAllConvertPairsError()
