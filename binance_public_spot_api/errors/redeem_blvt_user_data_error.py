from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

RedeemBlvtUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RedeemBlvtUserDataError:
    def map(self, response: HttpResponse) -> RedeemBlvtUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


redeem_blvt_user_data_error_mapper: Final[ErrorMapper[RedeemBlvtUserDataErrorBody]] = _RedeemBlvtUserDataError()
