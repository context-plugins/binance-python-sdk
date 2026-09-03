from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

PurchaseFixedActivityProjectUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _PurchaseFixedActivityProjectUserDataError:
    def map(self, response: HttpResponse) -> PurchaseFixedActivityProjectUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


purchase_fixed_activity_project_user_data_error_mapper: Final[
    ErrorMapper[PurchaseFixedActivityProjectUserDataErrorBody]
] = _PurchaseFixedActivityProjectUserDataError()
