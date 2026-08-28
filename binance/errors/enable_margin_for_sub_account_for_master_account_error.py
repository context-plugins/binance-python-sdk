from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

EnableMarginForSubAccountForMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EnableMarginForSubAccountForMasterAccountError:
    def map(self, response: HttpResponse) -> EnableMarginForSubAccountForMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


enable_margin_for_sub_account_for_master_account_error_mapper: Final[
    ErrorMapper[EnableMarginForSubAccountForMasterAccountErrorBody]
] = _EnableMarginForSubAccountForMasterAccountError()
