from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

QueryManagedSubAccountMarginAssetDetailsForInvestorMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _QueryManagedSubAccountMarginAssetDetailsForInvestorMasterAccountError:
    def map(self, response: HttpResponse) -> QueryManagedSubAccountMarginAssetDetailsForInvestorMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


query_managed_sub_account_margin_asset_details_for_investor_master_account_error_mapper: Final[
    ErrorMapper[QueryManagedSubAccountMarginAssetDetailsForInvestorMasterAccountErrorBody]
] = _QueryManagedSubAccountMarginAssetDetailsForInvestorMasterAccountError()
