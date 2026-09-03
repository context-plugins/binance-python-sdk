from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

FuturesPositionRiskOfSubAccountV2ForMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _FuturesPositionRiskOfSubAccountV2ForMasterAccountError:
    def map(self, response: HttpResponse) -> FuturesPositionRiskOfSubAccountV2ForMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


futures_position_risk_of_sub_account_v2_for_master_account_error_mapper: Final[
    ErrorMapper[FuturesPositionRiskOfSubAccountV2ForMasterAccountErrorBody]
] = _FuturesPositionRiskOfSubAccountV2ForMasterAccountError()
