from __future__ import annotations

from typing import TypeAlias

from ..sub_account_coinfutures_position_risk import (
    SubAccountCoinfuturesPositionRisk,
    SubAccountCoinfuturesPositionRiskDict,
)
from ..sub_account_usdtfutures_position_risk import (
    SubAccountUsdtfuturesPositionRisk,
    SubAccountUsdtfuturesPositionRiskDict,
)

SapiV2SubAccountFuturesPositionRiskResponse: TypeAlias = (
    SubAccountUsdtfuturesPositionRisk | SubAccountCoinfuturesPositionRisk
)

SapiV2SubAccountFuturesPositionRiskResponseDict: TypeAlias = (
    SubAccountUsdtfuturesPositionRiskDict | SubAccountCoinfuturesPositionRiskDict
)
