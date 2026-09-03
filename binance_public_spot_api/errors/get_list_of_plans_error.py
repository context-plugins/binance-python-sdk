from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetListOfPlansErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetListOfPlansError:
    def map(self, response: HttpResponse) -> GetListOfPlansErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_list_of_plans_error_mapper: Final[ErrorMapper[GetListOfPlansErrorBody]] = _GetListOfPlansError()
