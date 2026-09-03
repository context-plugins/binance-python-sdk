from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SubAccountTransferHistoryForSubAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SubAccountTransferHistoryForSubAccountError:
    def map(self, response: HttpResponse) -> SubAccountTransferHistoryForSubAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


sub_account_transfer_history_for_sub_account_error_mapper: Final[
    ErrorMapper[SubAccountTransferHistoryForSubAccountErrorBody]
] = _SubAccountTransferHistoryForSubAccountError()
