from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

EnableFuturesForSubAccountForMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EnableFuturesForSubAccountForMasterAccountError:
    def map(self, response: HttpResponse) -> EnableFuturesForSubAccountForMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


enable_futures_for_sub_account_for_master_account_error_mapper: Final[
    ErrorMapper[EnableFuturesForSubAccountForMasterAccountErrorBody]
] = _EnableFuturesForSubAccountForMasterAccountError()
