from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DepositHistorySupportingNetworkUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DepositHistorySupportingNetworkUserDataError:
    def map(self, response: HttpResponse) -> DepositHistorySupportingNetworkUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


deposit_history_supporting_network_user_data_error_mapper: Final[
    ErrorMapper[DepositHistorySupportingNetworkUserDataErrorBody]
] = _DepositHistorySupportingNetworkUserDataError()
