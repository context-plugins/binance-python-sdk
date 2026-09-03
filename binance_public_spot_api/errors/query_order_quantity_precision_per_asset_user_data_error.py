from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryOrderQuantityPrecisionPerAssetUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryOrderQuantityPrecisionPerAssetUserDataError:
    def map(self, response: HttpResponse) -> QueryOrderQuantityPrecisionPerAssetUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_order_quantity_precision_per_asset_user_data_error_mapper: Final[
    ErrorMapper[QueryOrderQuantityPrecisionPerAssetUserDataErrorBody]
] = _QueryOrderQuantityPrecisionPerAssetUserDataError()
