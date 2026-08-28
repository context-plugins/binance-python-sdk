from __future__ import annotations

from typing import TypeAlias

from ..sub_account_coinfutures_details import SubAccountCoinfuturesDetails, SubAccountCoinfuturesDetailsDict
from ..sub_account_usdtfutures_details import SubAccountUsdtfuturesDetails, SubAccountUsdtfuturesDetailsDict

SapiV2SubAccountFuturesAccountResponse: TypeAlias = SubAccountUsdtfuturesDetails | SubAccountCoinfuturesDetails

SapiV2SubAccountFuturesAccountResponseDict: TypeAlias = (
    SubAccountUsdtfuturesDetailsDict | SubAccountCoinfuturesDetailsDict
)
