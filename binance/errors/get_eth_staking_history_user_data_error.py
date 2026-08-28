from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetEthStakingHistoryUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetEthStakingHistoryUserDataError:
    def map(self, response: HttpResponse) -> GetEthStakingHistoryUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_eth_staking_history_user_data_error_mapper: Final[
    ErrorMapper[GetEthStakingHistoryUserDataErrorBody]
] = _GetEthStakingHistoryUserDataError()
