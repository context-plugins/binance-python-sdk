from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetTargetAssetRoiDataUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetTargetAssetRoiDataUserDataError:
    def map(self, response: HttpResponse) -> GetTargetAssetRoiDataUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_target_asset_roi_data_user_data_error_mapper: Final[
    ErrorMapper[GetTargetAssetRoiDataUserDataErrorBody]
] = _GetTargetAssetRoiDataUserDataError()
