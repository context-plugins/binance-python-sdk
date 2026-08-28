from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

FundCollectionByAssetUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _FundCollectionByAssetUserDataError:
    def map(self, response: HttpResponse) -> FundCollectionByAssetUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


fund_collection_by_asset_user_data_error_mapper: Final[
    ErrorMapper[FundCollectionByAssetUserDataErrorBody]
] = _FundCollectionByAssetUserDataError()
