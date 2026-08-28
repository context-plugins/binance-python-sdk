from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetCurrentEthStakingQuotaUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetCurrentEthStakingQuotaUserDataError:
    def map(self, response: HttpResponse) -> GetCurrentEthStakingQuotaUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_current_eth_staking_quota_user_data_error_mapper: Final[
    ErrorMapper[GetCurrentEthStakingQuotaUserDataErrorBody]
] = _GetCurrentEthStakingQuotaUserDataError()
