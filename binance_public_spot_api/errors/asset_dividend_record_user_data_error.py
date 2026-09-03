from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AssetDividendRecordUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AssetDividendRecordUserDataError:
    def map(self, response: HttpResponse) -> AssetDividendRecordUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


asset_dividend_record_user_data_error_mapper: Final[
    ErrorMapper[AssetDividendRecordUserDataErrorBody]
] = _AssetDividendRecordUserDataError()
