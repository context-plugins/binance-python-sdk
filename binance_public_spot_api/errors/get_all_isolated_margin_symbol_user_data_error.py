from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetAllIsolatedMarginSymbolUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAllIsolatedMarginSymbolUserDataError:
    def map(self, response: HttpResponse) -> GetAllIsolatedMarginSymbolUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_all_isolated_margin_symbol_user_data_error_mapper: Final[
    ErrorMapper[GetAllIsolatedMarginSymbolUserDataErrorBody]
] = _GetAllIsolatedMarginSymbolUserDataError()
