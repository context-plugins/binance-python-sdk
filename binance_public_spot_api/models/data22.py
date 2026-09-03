from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .funds_detail import FundsDetail, FundsDetailDict
from .payer_info import PayerInfo, PayerInfoDict
from .receiver_info import ReceiverInfo, ReceiverInfoDict


class Data22(SdkBaseModel):
    order_type: str = Field(alias="orderType")
    """Enum：PAY(C2B Merchant Acquiring Payment), PAY_REFUND(C2B Merchant Acquiring Payment,refund), C2C(C2C Transfer
    Payment),CRYPTO_BOX(Crypto box), CRYPTO_BOX_RF(Crypto Box, refund), C2C_HOLDING(Transfer to new Binance user),
    C2C_HOLDING_RF(Transfer to new Binance user,refund), PAYOUT(B2C Disbursement Payment)"""

    transaction_id: str = Field(alias="transactionId")
    transaction_time: int = Field(alias="transactionTime")
    amount: str
    """order amount(up to 8 decimal places), positive is income, negative is expenditure"""

    currency: str
    wallet_type: int = Field(alias="walletType")
    wallet_types: list[int] = Field(alias="walletTypes")
    funds_detail: list[FundsDetail] = Field(alias="fundsDetail")
    payer_info: PayerInfo = Field(alias="payerInfo")
    receiver_info: ReceiverInfo = Field(alias="receiverInfo")


class Data22Dict(TypedDict):
    order_type: str
    transaction_id: str
    transaction_time: int
    amount: str
    currency: str
    wallet_type: int
    wallet_types: list[int]
    funds_detail: list[FundsDetail | FundsDetailDict]
    payer_info: PayerInfo | PayerInfoDict
    receiver_info: ReceiverInfo | ReceiverInfoDict
