from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

StatisticListUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _StatisticListUserDataError:
    def map(self, response: HttpResponse) -> StatisticListUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


statistic_list_user_data_error_mapper: Final[
    ErrorMapper[StatisticListUserDataErrorBody]
] = _StatisticListUserDataError()
