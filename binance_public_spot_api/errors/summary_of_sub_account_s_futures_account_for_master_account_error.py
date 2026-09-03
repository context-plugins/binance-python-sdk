from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SummaryOfSubAccountSFuturesAccountForMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SummaryOfSubAccountSFuturesAccountForMasterAccountError:
    def map(self, response: HttpResponse) -> SummaryOfSubAccountSFuturesAccountForMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


summary_of_sub_account_s_futures_account_for_master_account_error_mapper: Final[
    ErrorMapper[SummaryOfSubAccountSFuturesAccountForMasterAccountErrorBody]
] = _SummaryOfSubAccountSFuturesAccountForMasterAccountError()
