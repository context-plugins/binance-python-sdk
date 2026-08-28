from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SubscribeEthStakingV2TradeErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _SubscribeEthStakingV2TradeError:
    def map(self, response: HttpResponse) -> SubscribeEthStakingV2TradeErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


subscribe_eth_staking_v2_trade_error_mapper: Final[
    ErrorMapper[SubscribeEthStakingV2TradeErrorBody]
] = _SubscribeEthStakingV2TradeError()
