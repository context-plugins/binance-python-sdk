from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CancelHashrateResaleConfigurationUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CancelHashrateResaleConfigurationUserDataError:
    def map(self, response: HttpResponse) -> CancelHashrateResaleConfigurationUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


cancel_hashrate_resale_configuration_user_data_error_mapper: Final[
    ErrorMapper[CancelHashrateResaleConfigurationUserDataErrorBody]
] = _CancelHashrateResaleConfigurationUserDataError()
