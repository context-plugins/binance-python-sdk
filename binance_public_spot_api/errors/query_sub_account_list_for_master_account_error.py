from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QuerySubAccountListForMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QuerySubAccountListForMasterAccountError:
    def map(self, response: HttpResponse) -> QuerySubAccountListForMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_sub_account_list_for_master_account_error_mapper: Final[
    ErrorMapper[QuerySubAccountListForMasterAccountErrorBody]
] = _QuerySubAccountListForMasterAccountError()
