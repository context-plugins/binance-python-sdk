from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryAllSourceAssetAndTargetAssetUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryAllSourceAssetAndTargetAssetUserDataError:
    def map(self, response: HttpResponse) -> QueryAllSourceAssetAndTargetAssetUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_all_source_asset_and_target_asset_user_data_error_mapper: Final[
    ErrorMapper[QueryAllSourceAssetAndTargetAssetUserDataErrorBody]
] = _QueryAllSourceAssetAndTargetAssetUserDataError()
