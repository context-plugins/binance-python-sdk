from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetBethRewardsDistributionHistoryUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetBethRewardsDistributionHistoryUserDataError:
    def map(self, response: HttpResponse) -> GetBethRewardsDistributionHistoryUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_beth_rewards_distribution_history_user_data_error_mapper: Final[
    ErrorMapper[GetBethRewardsDistributionHistoryUserDataErrorBody]
] = _GetBethRewardsDistributionHistoryUserDataError()
