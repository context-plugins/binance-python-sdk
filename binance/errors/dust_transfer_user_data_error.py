from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DustTransferUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DustTransferUserDataError:
    def map(self, response: HttpResponse) -> DustTransferUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


dust_transfer_user_data_error_mapper: Final[ErrorMapper[DustTransferUserDataErrorBody]] = _DustTransferUserDataError()
