from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QuerySubAccountAssetsForMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QuerySubAccountAssetsForMasterAccountError:
    def map(self, response: HttpResponse) -> QuerySubAccountAssetsForMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_sub_account_assets_for_master_account_error_mapper: Final[
    ErrorMapper[QuerySubAccountAssetsForMasterAccountErrorBody]
] = _QuerySubAccountAssetsForMasterAccountError()
