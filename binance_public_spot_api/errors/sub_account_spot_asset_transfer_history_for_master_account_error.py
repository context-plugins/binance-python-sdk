from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SubAccountSpotAssetTransferHistoryForMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SubAccountSpotAssetTransferHistoryForMasterAccountError:
    def map(self, response: HttpResponse) -> SubAccountSpotAssetTransferHistoryForMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


sub_account_spot_asset_transfer_history_for_master_account_error_mapper: Final[
    ErrorMapper[SubAccountSpotAssetTransferHistoryForMasterAccountErrorBody]
] = _SubAccountSpotAssetTransferHistoryForMasterAccountError()
