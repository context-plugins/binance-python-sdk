from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SubAccountSStatusOnMarginFuturesForMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SubAccountSStatusOnMarginFuturesForMasterAccountError:
    def map(self, response: HttpResponse) -> SubAccountSStatusOnMarginFuturesForMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


sub_account_s_status_on_margin_futures_for_master_account_error_mapper: Final[
    ErrorMapper[SubAccountSStatusOnMarginFuturesForMasterAccountErrorBody]
] = _SubAccountSStatusOnMarginFuturesForMasterAccountError()
