from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryManagedSubAccountTransferLogForInvestorMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryManagedSubAccountTransferLogForInvestorMasterAccountError:
    def map(self, response: HttpResponse) -> QueryManagedSubAccountTransferLogForInvestorMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_managed_sub_account_transfer_log_for_investor_master_account_error_mapper: Final[
    ErrorMapper[QueryManagedSubAccountTransferLogForInvestorMasterAccountErrorBody]
] = _QueryManagedSubAccountTransferLogForInvestorMasterAccountError()
