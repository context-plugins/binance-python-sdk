from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

UpdateIpRestrictionForSubAccountApiKeyForMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _UpdateIpRestrictionForSubAccountApiKeyForMasterAccountError:
    def map(self, response: HttpResponse) -> UpdateIpRestrictionForSubAccountApiKeyForMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


update_ip_restriction_for_sub_account_api_key_for_master_account_error_mapper: Final[
    ErrorMapper[UpdateIpRestrictionForSubAccountApiKeyForMasterAccountErrorBody]
] = _UpdateIpRestrictionForSubAccountApiKeyForMasterAccountError()
