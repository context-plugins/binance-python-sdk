from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

WithdrawlAssetsFromTheManagedSubAccountForInvestorMasterAccountErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _WithdrawlAssetsFromTheManagedSubAccountForInvestorMasterAccountError:
    def map(self, response: HttpResponse) -> WithdrawlAssetsFromTheManagedSubAccountForInvestorMasterAccountErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


withdrawl_assets_from_the_managed_sub_account_for_investor_master_account_error_mapper: Final[
    ErrorMapper[WithdrawlAssetsFromTheManagedSubAccountForInvestorMasterAccountErrorBody]
] = _WithdrawlAssetsFromTheManagedSubAccountForInvestorMasterAccountError()
