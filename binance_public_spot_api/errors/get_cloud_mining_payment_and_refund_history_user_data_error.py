from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetCloudMiningPaymentAndRefundHistoryUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetCloudMiningPaymentAndRefundHistoryUserDataError:
    def map(self, response: HttpResponse) -> GetCloudMiningPaymentAndRefundHistoryUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_cloud_mining_payment_and_refund_history_user_data_error_mapper: Final[
    ErrorMapper[GetCloudMiningPaymentAndRefundHistoryUserDataErrorBody]
] = _GetCloudMiningPaymentAndRefundHistoryUserDataError()
