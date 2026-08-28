from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryMarginAvailableInventoryUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryMarginAvailableInventoryUserDataError:
    def map(self, response: HttpResponse) -> QueryMarginAvailableInventoryUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_margin_available_inventory_user_data_error_mapper: Final[
    ErrorMapper[QueryMarginAvailableInventoryUserDataErrorBody]
] = _QueryMarginAvailableInventoryUserDataError()
