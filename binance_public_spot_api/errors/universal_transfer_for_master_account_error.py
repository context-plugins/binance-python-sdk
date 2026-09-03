from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

UniversalTransferForMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _UniversalTransferForMasterAccountError:
    def map(self, response: HttpResponse) -> UniversalTransferForMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


universal_transfer_for_master_account_error_mapper: Final[
    ErrorMapper[UniversalTransferForMasterAccountErrorBody]
] = _UniversalTransferForMasterAccountError()
