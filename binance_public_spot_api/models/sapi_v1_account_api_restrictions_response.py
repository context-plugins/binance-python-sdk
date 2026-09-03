from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SapiV1AccountApiRestrictionsResponse(SdkBaseModel):
    ip_restrict: bool = Field(alias="ipRestrict")
    create_time: int = Field(alias="createTime")
    enable_internal_transfer: bool = Field(alias="enableInternalTransfer")
    """This option authorizes this key to transfer funds between your master account and your sub account instantly"""

    enable_futures: bool = Field(alias="enableFutures")
    """API Key created before your futures account opened does not support futures API service"""

    enable_portfolio_margin_trading: Optional[bool] = Field(default=UNSET, alias="enablePortfolioMarginTrading")
    """API Key created before your activate portfolio margin does not support portfolio margin API service"""

    enable_vanilla_options: bool = Field(alias="enableVanillaOptions")
    """Authorizes this key to Vanilla options trading"""

    permits_universal_transfer: bool = Field(alias="permitsUniversalTransfer")
    """Authorizes this key to be used for a dedicated universal transfer API to transfer multiple supported currencies.
    Each business's own transfer API rights are not affected by this authorization"""

    enable_reading: bool = Field(alias="enableReading")
    enable_spot_and_margin_trading: bool = Field(alias="enableSpotAndMarginTrading")
    enable_withdrawals: bool = Field(alias="enableWithdrawals")
    """This option allows you to withdraw via API. You must apply the IP Access Restriction filter in order to enable
    withdrawals"""

    enable_margin: bool = Field(alias="enableMargin")
    """This option can be adjusted after the Cross Margin account transfer is completed"""

    trading_authority_expiration_time: int = Field(alias="tradingAuthorityExpirationTime")
    """Expiration time for spot and margin trading permission"""


class SapiV1AccountApiRestrictionsResponseDict(TypedDict):
    ip_restrict: bool
    create_time: int
    enable_internal_transfer: bool
    enable_futures: bool
    enable_portfolio_margin_trading: NotRequired[bool]
    enable_vanilla_options: bool
    permits_universal_transfer: bool
    enable_reading: bool
    enable_spot_and_margin_trading: bool
    enable_withdrawals: bool
    enable_margin: bool
    trading_authority_expiration_time: int
