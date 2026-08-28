from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

EthStakingAccountV2UserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _EthStakingAccountV2UserDataError:
    def map(self, response: HttpResponse) -> EthStakingAccountV2UserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


eth_staking_account_v2_user_data_error_mapper: Final[
    ErrorMapper[EthStakingAccountV2UserDataErrorBody]
] = _EthStakingAccountV2UserDataError()
