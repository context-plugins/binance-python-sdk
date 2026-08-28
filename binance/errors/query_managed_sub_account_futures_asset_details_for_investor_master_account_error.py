from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryManagedSubAccountFuturesAssetDetailsForInvestorMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryManagedSubAccountFuturesAssetDetailsForInvestorMasterAccountError:
    def map(self, response: HttpResponse) -> QueryManagedSubAccountFuturesAssetDetailsForInvestorMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_managed_sub_account_futures_asset_details_for_investor_master_account_error_mapper: Final[
    ErrorMapper[QueryManagedSubAccountFuturesAssetDetailsForInvestorMasterAccountErrorBody]
] = _QueryManagedSubAccountFuturesAssetDetailsForInvestorMasterAccountError()
