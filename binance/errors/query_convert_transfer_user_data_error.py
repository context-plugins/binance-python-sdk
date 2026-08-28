from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryConvertTransferUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryConvertTransferUserDataError:
    def map(self, response: HttpResponse) -> QueryConvertTransferUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_convert_transfer_user_data_error_mapper: Final[
    ErrorMapper[QueryConvertTransferUserDataErrorBody]
] = _QueryConvertTransferUserDataError()
