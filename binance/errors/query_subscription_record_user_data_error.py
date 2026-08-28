from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QuerySubscriptionRecordUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QuerySubscriptionRecordUserDataError:
    def map(self, response: HttpResponse) -> QuerySubscriptionRecordUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_subscription_record_user_data_error_mapper: Final[
    ErrorMapper[QuerySubscriptionRecordUserDataErrorBody]
] = _QuerySubscriptionRecordUserDataError()
