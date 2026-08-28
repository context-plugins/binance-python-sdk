from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DetailOnSubAccountSFuturesAccountV2ForMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DetailOnSubAccountSFuturesAccountV2ForMasterAccountError:
    def map(self, response: HttpResponse) -> DetailOnSubAccountSFuturesAccountV2ForMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


detail_on_sub_account_s_futures_account_v2_for_master_account_error_mapper: Final[
    ErrorMapper[DetailOnSubAccountSFuturesAccountV2ForMasterAccountErrorBody]
] = _DetailOnSubAccountSFuturesAccountV2ForMasterAccountError()
