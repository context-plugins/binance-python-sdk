from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetSimpleEarnLockedProductListUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetSimpleEarnLockedProductListUserDataError:
    def map(self, response: HttpResponse) -> GetSimpleEarnLockedProductListUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_simple_earn_locked_product_list_user_data_error_mapper: Final[
    ErrorMapper[GetSimpleEarnLockedProductListUserDataErrorBody]
] = _GetSimpleEarnLockedProductListUserDataError()
