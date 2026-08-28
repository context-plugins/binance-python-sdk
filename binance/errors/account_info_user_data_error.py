from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AccountInfoUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AccountInfoUserDataError:
    def map(self, response: HttpResponse) -> AccountInfoUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


account_info_user_data_error_mapper: Final[ErrorMapper[AccountInfoUserDataErrorBody]] = _AccountInfoUserDataError()
