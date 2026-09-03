from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

TransferToSubAccountOfSameMasterForSubAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _TransferToSubAccountOfSameMasterForSubAccountError:
    def map(self, response: HttpResponse) -> TransferToSubAccountOfSameMasterForSubAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


transfer_to_sub_account_of_same_master_for_sub_account_error_mapper: Final[
    ErrorMapper[TransferToSubAccountOfSameMasterForSubAccountErrorBody]
] = _TransferToSubAccountOfSameMasterForSubAccountError()
