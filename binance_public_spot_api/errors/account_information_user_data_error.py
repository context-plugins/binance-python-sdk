from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AccountInformationUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AccountInformationUserDataError:
    def map(self, response: HttpResponse) -> AccountInformationUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


account_information_user_data_error_mapper: Final[
    ErrorMapper[AccountInformationUserDataErrorBody]
] = _AccountInformationUserDataError()
