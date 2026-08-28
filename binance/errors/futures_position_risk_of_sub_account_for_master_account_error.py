from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

FuturesPositionRiskOfSubAccountForMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _FuturesPositionRiskOfSubAccountForMasterAccountError:
    def map(self, response: HttpResponse) -> FuturesPositionRiskOfSubAccountForMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


futures_position_risk_of_sub_account_for_master_account_error_mapper: Final[
    ErrorMapper[FuturesPositionRiskOfSubAccountForMasterAccountErrorBody]
] = _FuturesPositionRiskOfSubAccountForMasterAccountError()
