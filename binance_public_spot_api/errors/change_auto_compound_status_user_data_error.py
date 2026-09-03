from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ChangeAutoCompoundStatusUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ChangeAutoCompoundStatusUserDataError:
    def map(self, response: HttpResponse) -> ChangeAutoCompoundStatusUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


change_auto_compound_status_user_data_error_mapper: Final[
    ErrorMapper[ChangeAutoCompoundStatusUserDataErrorBody]
] = _ChangeAutoCompoundStatusUserDataError()
