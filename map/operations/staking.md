<!-- Generated file — do not edit; regenerated with the SDK. -->

# Staking — operations

Accessor: `client.staking` · Source: `binance/apis/staking.py` · 12 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.staking.eth_staking_account_v2_user_data

- **Route**: `GET /sapi/v2/eth-staking/account`
- **Signature**: `def eth_staking_account_v2_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2EthStakingAccountResponse`
- **Returns (raw)**: `ApiResult[SapiV2EthStakingAccountResponse, EthStakingAccountV2UserDataErrorBody]`
- **Error**: `EthStakingAccountV2UserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2EthStakingAccountResponse` | `binance/models/sapi_v2_eth_staking_account_response.py` |
| `EthStakingAccountV2UserDataErrorBody` | `binance/errors/eth_staking_account_v2_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.staking.get_beth_rewards_distribution_history_user_data

- **Route**: `GET /sapi/v1/eth-staking/eth/history/rewardsHistory`
- **Signature**: `def get_beth_rewards_distribution_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1EthStakingEthHistoryRewardsHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1EthStakingEthHistoryRewardsHistoryResponse, GetBethRewardsDistributionHistoryUserDataErrorBody]`
- **Error**: `GetBethRewardsDistributionHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1EthStakingEthHistoryRewardsHistoryResponse` | `binance/models/sapi_v1_eth_staking_eth_history_rewards_history_response.py` |
| `GetBethRewardsDistributionHistoryUserDataErrorBody` | `binance/errors/get_beth_rewards_distribution_history_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.staking.get_eth_redemption_history_user_data

- **Route**: `GET /sapi/v1/eth-staking/eth/history/redemptionHistory`
- **Signature**: `def get_eth_redemption_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1EthStakingEthHistoryRedemptionHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1EthStakingEthHistoryRedemptionHistoryResponse, GetEthRedemptionHistoryUserDataErrorBody]`
- **Error**: `GetEthRedemptionHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1EthStakingEthHistoryRedemptionHistoryResponse` | `binance/models/sapi_v1_eth_staking_eth_history_redemption_history_response.py` |
| `GetEthRedemptionHistoryUserDataErrorBody` | `binance/errors/get_eth_redemption_history_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.staking.get_eth_staking_history_user_data

- **Route**: `GET /sapi/v1/eth-staking/eth/history/stakingHistory`
- **Signature**: `def get_eth_staking_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1EthStakingEthHistoryStakingHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1EthStakingEthHistoryStakingHistoryResponse, GetEthStakingHistoryUserDataErrorBody]`
- **Error**: `GetEthStakingHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1EthStakingEthHistoryStakingHistoryResponse` | `binance/models/sapi_v1_eth_staking_eth_history_staking_history_response.py` |
| `GetEthStakingHistoryUserDataErrorBody` | `binance/errors/get_eth_staking_history_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.staking.get_wbeth_rate_history_user_data

- **Route**: `GET /sapi/v1/eth-staking/eth/history/rateHistory`
- **Signature**: `def get_wbeth_rate_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1EthStakingEthHistoryRateHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1EthStakingEthHistoryRateHistoryResponse, GetWbethRateHistoryUserDataErrorBody]`
- **Error**: `GetWbethRateHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1EthStakingEthHistoryRateHistoryResponse` | `binance/models/sapi_v1_eth_staking_eth_history_rate_history_response.py` |
| `GetWbethRateHistoryUserDataErrorBody` | `binance/errors/get_wbeth_rate_history_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.staking.get_wbeth_rewards_history_user_data

- **Route**: `GET /sapi/v1/eth-staking/eth/history/wbethRewardsHistory`
- **Signature**: `def get_wbeth_rewards_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse, GetWbethRewardsHistoryUserDataErrorBody]`
- **Error**: `GetWbethRewardsHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse` | `binance/models/sapi_v1_eth_staking_eth_history_wbeth_rewards_history_response.py` |
| `GetWbethRewardsHistoryUserDataErrorBody` | `binance/errors/get_wbeth_rewards_history_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.staking.get_wbeth_unwrap_history_user_data

- **Route**: `GET /sapi/v1/eth-staking/wbeth/history/unwrapHistory`
- **Signature**: `def get_wbeth_unwrap_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1EthStakingWbethHistoryUnwrapHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1EthStakingWbethHistoryUnwrapHistoryResponse, GetWbethUnwrapHistoryUserDataErrorBody]`
- **Error**: `GetWbethUnwrapHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1EthStakingWbethHistoryUnwrapHistoryResponse` | `binance/models/sapi_v1_eth_staking_wbeth_history_unwrap_history_response.py` |
| `GetWbethUnwrapHistoryUserDataErrorBody` | `binance/errors/get_wbeth_unwrap_history_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.staking.get_wbeth_wrap_history_user_data

- **Route**: `GET /sapi/v1/eth-staking/wbeth/history/wrapHistory`
- **Signature**: `def get_wbeth_wrap_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1EthStakingWbethHistoryWrapHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1EthStakingWbethHistoryWrapHistoryResponse, GetWbethWrapHistoryUserDataErrorBody]`
- **Error**: `GetWbethWrapHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1EthStakingWbethHistoryWrapHistoryResponse` | `binance/models/sapi_v1_eth_staking_wbeth_history_wrap_history_response.py` |
| `GetWbethWrapHistoryUserDataErrorBody` | `binance/errors/get_wbeth_wrap_history_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.staking.get_current_eth_staking_quota_user_data

- **Route**: `GET /sapi/v1/eth-staking/eth/quota`
- **Signature**: `def get_current_eth_staking_quota_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1EthStakingEthQuotaResponse`
- **Returns (raw)**: `ApiResult[SapiV1EthStakingEthQuotaResponse, GetCurrentEthStakingQuotaUserDataErrorBody]`
- **Error**: `GetCurrentEthStakingQuotaUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1EthStakingEthQuotaResponse` | `binance/models/sapi_v1_eth_staking_eth_quota_response.py` |
| `GetCurrentEthStakingQuotaUserDataErrorBody` | `binance/errors/get_current_eth_staking_quota_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.staking.redeem_eth_trade

- **Route**: `POST /sapi/v1/eth-staking/eth/redeem`
- **Signature**: `def redeem_eth_trade(amount: float, timestamp: int, signature: str, *, asset: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `amount`, `timestamp`, `signature`
- **Params**: `amount` — query · `timestamp` — query · `signature` — query · `asset` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1EthStakingEthRedeemResponse`
- **Returns (raw)**: `ApiResult[SapiV1EthStakingEthRedeemResponse, RedeemEthTradeErrorBody]`
- **Error**: `RedeemEthTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1EthStakingEthRedeemResponse` | `binance/models/sapi_v1_eth_staking_eth_redeem_response.py` |
| `RedeemEthTradeErrorBody` | `binance/errors/redeem_eth_trade_error.py` |
| `Error` | `binance/models/error.py` |

### client.staking.subscribe_eth_staking_v2_trade

- **Route**: `POST /sapi/v2/eth-staking/eth/stake`
- **Signature**: `def subscribe_eth_staking_v2_trade(amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `amount`, `timestamp`, `signature`
- **Params**: `amount` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV2EthStakingEthStakeResponse`
- **Returns (raw)**: `ApiResult[SapiV2EthStakingEthStakeResponse, SubscribeEthStakingV2TradeErrorBody]`
- **Error**: `SubscribeEthStakingV2TradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV2EthStakingEthStakeResponse` | `binance/models/sapi_v2_eth_staking_eth_stake_response.py` |
| `SubscribeEthStakingV2TradeErrorBody` | `binance/errors/subscribe_eth_staking_v2_trade_error.py` |
| `Error` | `binance/models/error.py` |

### client.staking.wrap_beth_trade

- **Route**: `POST /sapi/v1/eth-staking/wbeth/wrap`
- **Signature**: `def wrap_beth_trade(amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `amount`, `timestamp`, `signature`
- **Params**: `amount` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1EthStakingWbethWrapResponse`
- **Returns (raw)**: `ApiResult[SapiV1EthStakingWbethWrapResponse, WrapBethTradeErrorBody]`
- **Error**: `WrapBethTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1EthStakingWbethWrapResponse` | `binance/models/sapi_v1_eth_staking_wbeth_wrap_response.py` |
| `WrapBethTradeErrorBody` | `binance/errors/wrap_beth_trade_error.py` |
| `Error` | `binance/models/error.py` |

