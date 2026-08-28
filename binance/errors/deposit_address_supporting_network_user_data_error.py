from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DepositAddressSupportingNetworkUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DepositAddressSupportingNetworkUserDataError:
    def map(self, response: HttpResponse) -> DepositAddressSupportingNetworkUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


deposit_address_supporting_network_user_data_error_mapper: Final[
    ErrorMapper[DepositAddressSupportingNetworkUserDataErrorBody]
] = _DepositAddressSupportingNetworkUserDataError()
