from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SubAccountFuturesAssetTransferForMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SubAccountFuturesAssetTransferForMasterAccountError:
    def map(self, response: HttpResponse) -> SubAccountFuturesAssetTransferForMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


sub_account_futures_asset_transfer_for_master_account_error_mapper: Final[
    ErrorMapper[SubAccountFuturesAssetTransferForMasterAccountErrorBody]
] = _SubAccountFuturesAssetTransferForMasterAccountError()
