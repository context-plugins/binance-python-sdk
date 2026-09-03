from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

EnableOptionsForSubAccountForMasterAccountUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EnableOptionsForSubAccountForMasterAccountUserDataError:
    def map(self, response: HttpResponse) -> EnableOptionsForSubAccountForMasterAccountUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


enable_options_for_sub_account_for_master_account_user_data_error_mapper: Final[
    ErrorMapper[EnableOptionsForSubAccountForMasterAccountUserDataErrorBody]
] = _EnableOptionsForSubAccountForMasterAccountUserDataError()
