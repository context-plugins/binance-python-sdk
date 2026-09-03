from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

FetchDepositAddressListWithNetworkUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _FetchDepositAddressListWithNetworkUserDataError:
    def map(self, response: HttpResponse) -> FetchDepositAddressListWithNetworkUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


fetch_deposit_address_list_with_network_user_data_error_mapper: Final[
    ErrorMapper[FetchDepositAddressListWithNetworkUserDataErrorBody]
] = _FetchDepositAddressListWithNetworkUserDataError()
