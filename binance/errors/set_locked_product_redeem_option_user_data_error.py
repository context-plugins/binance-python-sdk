from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SetLockedProductRedeemOptionUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SetLockedProductRedeemOptionUserDataError:
    def map(self, response: HttpResponse) -> SetLockedProductRedeemOptionUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


set_locked_product_redeem_option_user_data_error_mapper: Final[
    ErrorMapper[SetLockedProductRedeemOptionUserDataErrorBody]
] = _SetLockedProductRedeemOptionUserDataError()
