from __future__ import annotations

from typing import TypeAlias

from ..repayment_info import RepaymentInfo, RepaymentInfoDict
from ..repayment_info2 import RepaymentInfo2, RepaymentInfo2Dict

SapiV1LoanRepayResponse: TypeAlias = RepaymentInfo | RepaymentInfo2

SapiV1LoanRepayResponseDict: TypeAlias = RepaymentInfoDict | RepaymentInfo2Dict
