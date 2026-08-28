from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryUserDelegationHistoryForMasterAccountUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryUserDelegationHistoryForMasterAccountUserDataError:
    def map(self, response: HttpResponse) -> QueryUserDelegationHistoryForMasterAccountUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_user_delegation_history_for_master_account_user_data_error_mapper: Final[
    ErrorMapper[QueryUserDelegationHistoryForMasterAccountUserDataErrorBody]
] = _QueryUserDelegationHistoryForMasterAccountUserDataError()
