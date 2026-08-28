from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetFutureTickLevelOrderbookHistoricalDataDownloadLinkUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetFutureTickLevelOrderbookHistoricalDataDownloadLinkUserDataError:
    def map(self, response: HttpResponse) -> GetFutureTickLevelOrderbookHistoricalDataDownloadLinkUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_future_tick_level_orderbook_historical_data_download_link_user_data_error_mapper: Final[
    ErrorMapper[GetFutureTickLevelOrderbookHistoricalDataDownloadLinkUserDataErrorBody]
] = _GetFutureTickLevelOrderbookHistoricalDataDownloadLinkUserDataError()
