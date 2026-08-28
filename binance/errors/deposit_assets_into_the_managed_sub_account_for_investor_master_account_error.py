from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DepositAssetsIntoTheManagedSubAccountForInvestorMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DepositAssetsIntoTheManagedSubAccountForInvestorMasterAccountError:
    def map(self, response: HttpResponse) -> DepositAssetsIntoTheManagedSubAccountForInvestorMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


deposit_assets_into_the_managed_sub_account_for_investor_master_account_error_mapper: Final[
    ErrorMapper[DepositAssetsIntoTheManagedSubAccountForInvestorMasterAccountErrorBody]
] = _DepositAssetsIntoTheManagedSubAccountForInvestorMasterAccountError()
