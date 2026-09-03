from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DailyAccountSnapshotUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DailyAccountSnapshotUserDataError:
    def map(self, response: HttpResponse) -> DailyAccountSnapshotUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


daily_account_snapshot_user_data_error_mapper: Final[
    ErrorMapper[DailyAccountSnapshotUserDataErrorBody]
] = _DailyAccountSnapshotUserDataError()
