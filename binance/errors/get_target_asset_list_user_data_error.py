from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetTargetAssetListUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetTargetAssetListUserDataError:
    def map(self, response: HttpResponse) -> GetTargetAssetListUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_target_asset_list_user_data_error_mapper: Final[
    ErrorMapper[GetTargetAssetListUserDataErrorBody]
] = _GetTargetAssetListUserDataError()
