<!-- Generated file — do not edit; regenerated with the SDK. -->

# Margin — operations

Accessor: `client.margin` · Source: `binance_public_spot_api/apis/margin.py` · 48 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.margin.adjust_cross_margin_max_leverage_user_data

- **Route**: `POST /sapi/v1/margin/max-leverage`
- **Auth**: `api_key_auth`
- **Signature**: `def adjust_cross_margin_max_leverage_user_data(max_leverage: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `max_leverage`, `timestamp`, `signature`
- **Params**: `max_leverage` — query `maxLeverage` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginMaxLeverageResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginMaxLeverageResponse, AdjustCrossMarginMaxLeverageUserDataErrorBody]`
- **Error**: `AdjustCrossMarginMaxLeverageUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginMaxLeverageResponse` | `binance_public_spot_api/models/sapi_v1_margin_max_leverage_response.py` |
| `AdjustCrossMarginMaxLeverageUserDataErrorBody` | `binance_public_spot_api/errors/adjust_cross_margin_max_leverage_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.cross_margin_collateral_ratio_market_data

- **Route**: `GET /sapi/v1/margin/crossMarginCollateralRatio`
- **Auth**: `api_key_auth`
- **Signature**: `def cross_margin_collateral_ratio_market_data(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[SapiV1MarginCrossMarginCollateralRatioResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginCrossMarginCollateralRatioResponse], CrossMarginCollateralRatioMarketDataErrorBody]`
- **Error**: `CrossMarginCollateralRatioMarketDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginCrossMarginCollateralRatioResponse` | `binance_public_spot_api/models/sapi_v1_margin_cross_margin_collateral_ratio_response.py` |
| `CrossMarginCollateralRatioMarketDataErrorBody` | `binance_public_spot_api/errors/cross_margin_collateral_ratio_market_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.disable_isolated_margin_account_trade

- **Route**: `DELETE /sapi/v1/margin/isolated/account`
- **Auth**: `api_key_auth`
- **Signature**: `def disable_isolated_margin_account_trade(symbol: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginIsolatedAccountResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginIsolatedAccountResponse, DisableIsolatedMarginAccountTradeErrorBody]`
- **Error**: `DisableIsolatedMarginAccountTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginIsolatedAccountResponse` | `binance_public_spot_api/models/sapi_v1_margin_isolated_account_response.py` |
| `DisableIsolatedMarginAccountTradeErrorBody` | `binance_public_spot_api/errors/disable_isolated_margin_account_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.enable_isolated_margin_account_trade

- **Route**: `POST /sapi/v1/margin/isolated/account`
- **Auth**: `api_key_auth`
- **Signature**: `def enable_isolated_margin_account_trade(symbol: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginIsolatedAccountResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginIsolatedAccountResponse, EnableIsolatedMarginAccountTradeErrorBody]`
- **Error**: `EnableIsolatedMarginAccountTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginIsolatedAccountResponse` | `binance_public_spot_api/models/sapi_v1_margin_isolated_account_response.py` |
| `EnableIsolatedMarginAccountTradeErrorBody` | `binance_public_spot_api/errors/enable_isolated_margin_account_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.get_all_cross_margin_pairs_market_data

- **Route**: `GET /sapi/v1/margin/allPairs`
- **Auth**: `api_key_auth`
- **Signature**: `def get_all_cross_margin_pairs_market_data(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `list[SapiV1MarginAllPairsResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginAllPairsResponse], GetAllCrossMarginPairsMarketDataErrorBody]`
- **Error**: `GetAllCrossMarginPairsMarketDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginAllPairsResponse` | `binance_public_spot_api/models/sapi_v1_margin_all_pairs_response.py` |
| `GetAllCrossMarginPairsMarketDataErrorBody` | `binance_public_spot_api/errors/get_all_cross_margin_pairs_market_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.get_all_isolated_margin_symbol_user_data

- **Route**: `GET /sapi/v1/margin/isolated/allPairs`
- **Auth**: `api_key_auth`
- **Signature**: `def get_all_isolated_margin_symbol_user_data(symbol: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1MarginIsolatedAllPairsResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginIsolatedAllPairsResponse], GetAllIsolatedMarginSymbolUserDataErrorBody]`
- **Error**: `GetAllIsolatedMarginSymbolUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginIsolatedAllPairsResponse` | `binance_public_spot_api/models/sapi_v1_margin_isolated_all_pairs_response.py` |
| `GetAllIsolatedMarginSymbolUserDataErrorBody` | `binance_public_spot_api/errors/get_all_isolated_margin_symbol_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.get_all_margin_assets_market_data

- **Route**: `GET /sapi/v1/margin/allAssets`
- **Auth**: `api_key_auth`
- **Signature**: `def get_all_margin_assets_market_data(asset: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset`
- **Params**: `asset` — query
- **Returns (parsed)**: `list[SapiV1MarginAllAssetsResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginAllAssetsResponse], GetAllMarginAssetsMarketDataErrorBody]`
- **Error**: `GetAllMarginAssetsMarketDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginAllAssetsResponse` | `binance_public_spot_api/models/sapi_v1_margin_all_assets_response.py` |
| `GetAllMarginAssetsMarketDataErrorBody` | `binance_public_spot_api/errors/get_all_margin_assets_market_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.get_bnb_burn_status_user_data

- **Route**: `GET /sapi/v1/bnbBurn`
- **Auth**: `api_key_auth`
- **Signature**: `def get_bnb_burn_status_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `BnbBurnStatus`
- **Returns (raw)**: `ApiResult[BnbBurnStatus, GetBnbBurnStatusUserDataErrorBody]`
- **Error**: `GetBnbBurnStatusUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BnbBurnStatus` | `binance_public_spot_api/models/bnb_burn_status.py` |
| `GetBnbBurnStatusUserDataErrorBody` | `binance_public_spot_api/errors/get_bnb_burn_status_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.get_cross_margin_transfer_history_user_data

- **Route**: `GET /sapi/v1/margin/transfer`
- **Auth**: `api_key_auth`
- **Signature**: `def get_cross_margin_transfer_history_user_data(timestamp: int, signature: str, *, asset: str | None = None, type_: Type2OrStr | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, isolated_symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `asset` — query · `type_` — query `type` · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `isolated_symbol` — query `isolatedSymbol` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginTransferResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginTransferResponse, GetCrossMarginTransferHistoryUserDataErrorBody]`
- **Error**: `GetCrossMarginTransferHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Type2OrStr` | `binance_public_spot_api/models/enums/type2.py` |
| `SapiV1MarginTransferResponse` | `binance_public_spot_api/models/sapi_v1_margin_transfer_response.py` |
| `GetCrossMarginTransferHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_cross_margin_transfer_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.get_force_liquidation_record_user_data

- **Route**: `GET /sapi/v1/margin/forceLiquidationRec`
- **Auth**: `api_key_auth`
- **Signature**: `def get_force_liquidation_record_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, isolated_symbol: str | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `isolated_symbol` — query `isolatedSymbol` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginForceLiquidationRecResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginForceLiquidationRecResponse, GetForceLiquidationRecordUserDataErrorBody]`
- **Error**: `GetForceLiquidationRecordUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginForceLiquidationRecResponse` | `binance_public_spot_api/models/sapi_v1_margin_force_liquidation_rec_response.py` |
| `GetForceLiquidationRecordUserDataErrorBody` | `binance_public_spot_api/errors/get_force_liquidation_record_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.get_interest_history_user_data

- **Route**: `GET /sapi/v1/margin/interestHistory`
- **Auth**: `api_key_auth`
- **Signature**: `def get_interest_history_user_data(timestamp: int, signature: str, *, asset: str | None = None, isolated_symbol: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, archived: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `asset` — query · `isolated_symbol` — query `isolatedSymbol` · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `archived` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginInterestHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginInterestHistoryResponse, GetInterestHistoryUserDataErrorBody]`
- **Error**: `GetInterestHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginInterestHistoryResponse` | `binance_public_spot_api/models/sapi_v1_margin_interest_history_response.py` |
| `GetInterestHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_interest_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.get_small_liability_exchange_coin_list_user_data

- **Route**: `GET /sapi/v1/margin/exchange-small-liability`
- **Auth**: `api_key_auth`
- **Signature**: `def get_small_liability_exchange_coin_list_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1MarginExchangeSmallLiabilityResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginExchangeSmallLiabilityResponse], GetSmallLiabilityExchangeCoinListUserDataErrorBody]`
- **Error**: `GetSmallLiabilityExchangeCoinListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginExchangeSmallLiabilityResponse` | `binance_public_spot_api/models/sapi_v1_margin_exchange_small_liability_response.py` |
| `GetSmallLiabilityExchangeCoinListUserDataErrorBody` | `binance_public_spot_api/errors/get_small_liability_exchange_coin_list_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.get_small_liability_exchange_history_user_data

- **Route**: `GET /sapi/v1/margin/exchange-small-liability-history`
- **Auth**: `api_key_auth`
- **Signature**: `def get_small_liability_exchange_history_user_data(timestamp: int, signature: str, *, current: int | None = None, size: int | None = None, start_time: int | None = None, end_time: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `current` — query · `size` — query · `start_time` — query `startTime` · `end_time` — query `endTime` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginExchangeSmallLiabilityHistoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginExchangeSmallLiabilityHistoryResponse, GetSmallLiabilityExchangeHistoryUserDataErrorBody]`
- **Error**: `GetSmallLiabilityExchangeHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginExchangeSmallLiabilityHistoryResponse` | `binance_public_spot_api/models/sapi_v1_margin_exchange_small_liability_history_response.py` |
| `GetSmallLiabilityExchangeHistoryUserDataErrorBody` | `binance_public_spot_api/errors/get_small_liability_exchange_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.get_summary_of_margin_account_user_data

- **Route**: `GET /sapi/v1/margin/tradeCoeff`
- **Auth**: `api_key_auth`
- **Signature**: `def get_summary_of_margin_account_user_data(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `email`, `timestamp`, `signature`
- **Params**: `email` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginTradeCoeffResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginTradeCoeffResponse, GetSummaryOfMarginAccountUserDataErrorBody]`
- **Error**: `GetSummaryOfMarginAccountUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginTradeCoeffResponse` | `binance_public_spot_api/models/sapi_v1_margin_trade_coeff_response.py` |
| `GetSummaryOfMarginAccountUserDataErrorBody` | `binance_public_spot_api/errors/get_summary_of_margin_account_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.get_a_future_hourly_interest_rate_user_data

- **Route**: `GET /sapi/v1/margin/next-hourly-interest-rate`
- **Auth**: `api_key_auth`
- **Signature**: `def get_a_future_hourly_interest_rate_user_data(timestamp: int, signature: str, *, assets: str | None = None, is_isolated: IsIsolatedOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `assets` — query · `is_isolated` — query `isIsolated` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1MarginNextHourlyInterestRateResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginNextHourlyInterestRateResponse], GetAFutureHourlyInterestRateUserDataErrorBody]`
- **Error**: `GetAFutureHourlyInterestRateUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `SapiV1MarginNextHourlyInterestRateResponse` | `binance_public_spot_api/models/sapi_v1_margin_next_hourly_interest_rate_response.py` |
| `GetAFutureHourlyInterestRateUserDataErrorBody` | `binance_public_spot_api/errors/get_a_future_hourly_interest_rate_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.get_cross_or_isolated_margin_capital_flow_user_data

- **Route**: `GET /sapi/v1/margin/capital-flow`
- **Auth**: `api_key_auth`
- **Signature**: `def get_cross_or_isolated_margin_capital_flow_user_data(timestamp: int, signature: str, *, asset: str | None = None, symbol: str | None = None, type_: Type3OrStr | None = None, start_time: int | None = None, end_time: int | None = None, from_id: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `asset` — query · `symbol` — query · `type_` — query `type` · `start_time` — query `startTime` · `end_time` — query `endTime` · `from_id` — query `fromId` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1MarginCapitalFlowResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginCapitalFlowResponse], GetCrossOrIsolatedMarginCapitalFlowUserDataErrorBody]`
- **Error**: `GetCrossOrIsolatedMarginCapitalFlowUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Type3OrStr` | `binance_public_spot_api/models/enums/type3.py` |
| `SapiV1MarginCapitalFlowResponse` | `binance_public_spot_api/models/sapi_v1_margin_capital_flow_response.py` |
| `GetCrossOrIsolatedMarginCapitalFlowUserDataErrorBody` | `binance_public_spot_api/errors/get_cross_or_isolated_margin_capital_flow_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data

- **Route**: `GET /sapi/v1/margin/delist-schedule`
- **Auth**: `api_key_auth`
- **Signature**: `def get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1MarginDelistScheduleResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginDelistScheduleResponse], GetTokensOrSymbolsDelistScheduleForCrossMarginAndIsolatedMarginMarketDataErrorBody]`
- **Error**: `GetTokensOrSymbolsDelistScheduleForCrossMarginAndIsolatedMarginMarketDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginDelistScheduleResponse` | `binance_public_spot_api/models/sapi_v1_margin_delist_schedule_response.py` |
| `GetTokensOrSymbolsDelistScheduleForCrossMarginAndIsolatedMarginMarketDataErrorBody` | `binance_public_spot_api/errors/get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.margin_account_cancel_oco_trade

- **Route**: `DELETE /sapi/v1/margin/orderList`
- **Auth**: `api_key_auth`
- **Signature**: `def margin_account_cancel_oco_trade(symbol: str, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, order_list_id: int | None = None, list_client_order_id: str | None = None, new_client_order_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `is_isolated` — query `isIsolated` · `order_list_id` — query `orderListId` · `list_client_order_id` — query `listClientOrderId` · `new_client_order_id` — query `newClientOrderId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `MarginOcoOrder`
- **Returns (raw)**: `ApiResult[MarginOcoOrder, MarginAccountCancelOcoTradeErrorBody]`
- **Error**: `MarginAccountCancelOcoTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `MarginOcoOrder` | `binance_public_spot_api/models/margin_oco_order.py` |
| `MarginAccountCancelOcoTradeErrorBody` | `binance_public_spot_api/errors/margin_account_cancel_oco_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.margin_account_cancel_order_trade

- **Route**: `DELETE /sapi/v1/margin/order`
- **Auth**: `api_key_auth`
- **Signature**: `def margin_account_cancel_order_trade(symbol: str, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, order_id: int | None = None, orig_client_order_id: str | None = None, new_client_order_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `is_isolated` — query `isIsolated` · `order_id` — query `orderId` · `orig_client_order_id` — query `origClientOrderId` · `new_client_order_id` — query `newClientOrderId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `MarginOrder`
- **Returns (raw)**: `ApiResult[MarginOrder, MarginAccountCancelOrderTradeErrorBody]`
- **Error**: `MarginAccountCancelOrderTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `MarginOrder` | `binance_public_spot_api/models/margin_order.py` |
| `MarginAccountCancelOrderTradeErrorBody` | `binance_public_spot_api/errors/margin_account_cancel_order_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.margin_account_cancel_all_open_orders_on_a_symbol_trade

- **Route**: `DELETE /sapi/v1/margin/openOrders`
- **Auth**: `api_key_auth`
- **Signature**: `def margin_account_cancel_all_open_orders_on_a_symbol_trade(symbol: str, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `is_isolated` — query `isIsolated` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1MarginOpenOrdersResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginOpenOrdersResponse], MarginAccountCancelAllOpenOrdersOnASymbolTradeErrorBody]`
- **Error**: `MarginAccountCancelAllOpenOrdersOnASymbolTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `SapiV1MarginOpenOrdersResponse` | `binance_public_spot_api/models/unions/sapi_v1_margin_open_orders_response.py` |
| `MarginAccountCancelAllOpenOrdersOnASymbolTradeErrorBody` | `binance_public_spot_api/errors/margin_account_cancel_all_open_orders_on_a_symbol_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.margin_account_new_oco_trade

- **Route**: `POST /sapi/v1/margin/order/oco`
- **Auth**: `api_key_auth`
- **Signature**: `def margin_account_new_oco_trade(symbol: str, side: SideOrStr, quantity: float, price: float, stop_price: float, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, list_client_order_id: str | None = None, limit_client_order_id: str | None = None, limit_iceberg_qty: float | None = None, stop_client_order_id: str | None = None, stop_limit_price: float | None = None, stop_iceberg_qty: float | None = None, stop_limit_time_in_force: StopLimitTimeInForceOrStr | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, side_effect_type: SideEffectTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `side`, `quantity`, `price`, `stop_price`, `timestamp`, `signature`
- **Params**: `symbol` — query · `side` — query · `quantity` — query · `price` — query · `stop_price` — query `stopPrice` · `timestamp` — query · `signature` — query · `is_isolated` — query `isIsolated` · `list_client_order_id` — query `listClientOrderId` · `limit_client_order_id` — query `limitClientOrderId` · `limit_iceberg_qty` — query `limitIcebergQty` · `stop_client_order_id` — query `stopClientOrderId` · `stop_limit_price` — query `stopLimitPrice` · `stop_iceberg_qty` — query `stopIcebergQty` · `stop_limit_time_in_force` — query `stopLimitTimeInForce` · `new_order_resp_type` — query `newOrderRespType` · `side_effect_type` — query `sideEffectType` · `self_trade_prevention_mode` — query `selfTradePreventionMode` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginOrderOcoResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginOrderOcoResponse, MarginAccountNewOcoTradeErrorBody]`
- **Error**: `MarginAccountNewOcoTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SideOrStr` | `binance_public_spot_api/models/enums/side.py` |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `StopLimitTimeInForceOrStr` | `binance_public_spot_api/models/enums/stop_limit_time_in_force.py` |
| `NewOrderRespTypeOrStr` | `binance_public_spot_api/models/enums/new_order_resp_type.py` |
| `SideEffectTypeOrStr` | `binance_public_spot_api/models/enums/side_effect_type.py` |
| `SelfTradePreventionModeOrStr` | `binance_public_spot_api/models/enums/self_trade_prevention_mode.py` |
| `SapiV1MarginOrderOcoResponse` | `binance_public_spot_api/models/sapi_v1_margin_order_oco_response.py` |
| `MarginAccountNewOcoTradeErrorBody` | `binance_public_spot_api/errors/margin_account_new_oco_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.margin_account_new_oto_trade

- **Route**: `POST /sapi/v1/margin/order/oto`
- **Auth**: `api_key_auth`
- **Signature**: `def margin_account_new_oto_trade(symbol: str, working_type: WorkingTypeOrStr, working_side: WorkingSideOrStr, working_price: float, working_quantity: float, working_iceberg_qty: float, pending_type: PendingTypeOrStr, pending_side: PendingSideOrStr, pending_quantity: float, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, list_client_order_id: str | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, side_effect_type: SideEffectType1OrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, auto_repay_at_cancel: bool | None = None, working_client_order_id: str | None = None, working_time_in_force: WorkingTimeInForceOrStr | None = None, pending_client_order_id: str | None = None, pending_price: float | None = None, pending_stop_price: float | None = None, pending_trailing_delta: float | None = None, pending_iceberg_qty: float | None = None, pending_time_in_force: PendingTimeInForceOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `working_type`, `working_side`, `working_price`, `working_quantity`, `working_iceberg_qty`, `pending_type`, `pending_side`, `pending_quantity`, `timestamp`, `signature`
- **Params**: `symbol` — query · `working_type` — query `workingType` · `working_side` — query `workingSide` · `working_price` — query `workingPrice` · `working_quantity` — query `workingQuantity` · `working_iceberg_qty` — query `workingIcebergQty` · `pending_type` — query `pendingType` · `pending_side` — query `pendingSide` · `pending_quantity` — query `pendingQuantity` · `timestamp` — query · `signature` — query · `is_isolated` — query `isIsolated` · `list_client_order_id` — query `listClientOrderId` · `new_order_resp_type` — query `newOrderRespType` · `side_effect_type` — query `sideEffectType` · `self_trade_prevention_mode` — query `selfTradePreventionMode` · `auto_repay_at_cancel` — query `autoRepayAtCancel` · `working_client_order_id` — query `workingClientOrderId` · `working_time_in_force` — query `workingTimeInForce` · `pending_client_order_id` — query `pendingClientOrderId` · `pending_price` — query `pendingPrice` · `pending_stop_price` — query `pendingStopPrice` · `pending_trailing_delta` — query `pendingTrailingDelta` · `pending_iceberg_qty` — query `pendingIcebergQty` · `pending_time_in_force` — query `pendingTimeInForce`
- **Returns (parsed)**: `SapiV1MarginOrderOtoResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginOrderOtoResponse, MarginAccountNewOtoTradeErrorBody]`
- **Error**: `MarginAccountNewOtoTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WorkingTypeOrStr` | `binance_public_spot_api/models/enums/working_type.py` |
| `WorkingSideOrStr` | `binance_public_spot_api/models/enums/working_side.py` |
| `PendingTypeOrStr` | `binance_public_spot_api/models/enums/pending_type.py` |
| `PendingSideOrStr` | `binance_public_spot_api/models/enums/pending_side.py` |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `NewOrderRespTypeOrStr` | `binance_public_spot_api/models/enums/new_order_resp_type.py` |
| `SideEffectType1OrStr` | `binance_public_spot_api/models/enums/side_effect_type1.py` |
| `SelfTradePreventionModeOrStr` | `binance_public_spot_api/models/enums/self_trade_prevention_mode.py` |
| `WorkingTimeInForceOrStr` | `binance_public_spot_api/models/enums/working_time_in_force.py` |
| `PendingTimeInForceOrStr` | `binance_public_spot_api/models/enums/pending_time_in_force.py` |
| `SapiV1MarginOrderOtoResponse` | `binance_public_spot_api/models/sapi_v1_margin_order_oto_response.py` |
| `MarginAccountNewOtoTradeErrorBody` | `binance_public_spot_api/errors/margin_account_new_oto_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.margin_account_new_otoco_trade

- **Route**: `POST /sapi/v1/margin/order/otoco`
- **Auth**: `api_key_auth`
- **Signature**: `def margin_account_new_otoco_trade(symbol: str, working_type: WorkingTypeOrStr, working_side: WorkingSideOrStr, working_price: float, working_quantity: float, working_iceberg_qty: float, pending_side: PendingSideOrStr, pending_quantity: float, pending_above_type: PendingAboveTypeOrStr, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, side_effect_type: SideEffectType1OrStr | None = None, auto_repay_at_cancel: bool | None = None, list_client_order_id: str | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, working_client_order_id: str | None = None, working_time_in_force: WorkingTimeInForceOrStr | None = None, pending_above_client_order_id: str | None = None, pending_above_price: float | None = None, pending_above_stop_price: float | None = None, pending_above_trailing_delta: float | None = None, pending_above_iceberg_qty: float | None = None, pending_above_time_in_force: PendingAboveTimeInForceOrStr | None = None, pending_below_type: PendingBelowTypeOrStr | None = None, pending_below_client_order_id: str | None = None, pending_below_price: float | None = None, pending_below_stop_price: float | None = None, pending_below_trailing_delta: float | None = None, pending_below_iceberg_qty: float | None = None, pending_below_time_in_force: PendingBelowTimeInForceOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `working_type`, `working_side`, `working_price`, `working_quantity`, `working_iceberg_qty`, `pending_side`, `pending_quantity`, `pending_above_type`, `timestamp`, `signature`
- **Params**: `symbol` — query · `working_type` — query `workingType` · `working_side` — query `workingSide` · `working_price` — query `workingPrice` · `working_quantity` — query `workingQuantity` · `working_iceberg_qty` — query `workingIcebergQty` · `pending_side` — query `pendingSide` · `pending_quantity` — query `pendingQuantity` · `pending_above_type` — query `pendingAboveType` · `timestamp` — query · `signature` — query · `is_isolated` — query `isIsolated` · `side_effect_type` — query `sideEffectType` · `auto_repay_at_cancel` — query `autoRepayAtCancel` · `list_client_order_id` — query `listClientOrderId` · `new_order_resp_type` — query `newOrderRespType` · `self_trade_prevention_mode` — query `selfTradePreventionMode` · `working_client_order_id` — query `workingClientOrderId` · `working_time_in_force` — query `workingTimeInForce` · `pending_above_client_order_id` — query `pendingAboveClientOrderId` · `pending_above_price` — query `pendingAbovePrice` · `pending_above_stop_price` — query `pendingAboveStopPrice` · `pending_above_trailing_delta` — query `pendingAboveTrailingDelta` · `pending_above_iceberg_qty` — query `pendingAboveIcebergQty` · `pending_above_time_in_force` — query `pendingAboveTimeInForce` · `pending_below_type` — query `pendingBelowType` · `pending_below_client_order_id` — query `pendingBelowClientOrderId` · `pending_below_price` — query `pendingBelowPrice` · `pending_below_stop_price` — query `pendingBelowStopPrice` · `pending_below_trailing_delta` — query `pendingBelowTrailingDelta` · `pending_below_iceberg_qty` — query `pendingBelowIcebergQty` · `pending_below_time_in_force` — query `pendingBelowTimeInForce`
- **Returns (parsed)**: `SapiV1MarginOrderOtocoResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginOrderOtocoResponse, MarginAccountNewOtocoTradeErrorBody]`
- **Error**: `MarginAccountNewOtocoTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WorkingTypeOrStr` | `binance_public_spot_api/models/enums/working_type.py` |
| `WorkingSideOrStr` | `binance_public_spot_api/models/enums/working_side.py` |
| `PendingSideOrStr` | `binance_public_spot_api/models/enums/pending_side.py` |
| `PendingAboveTypeOrStr` | `binance_public_spot_api/models/enums/pending_above_type.py` |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `SideEffectType1OrStr` | `binance_public_spot_api/models/enums/side_effect_type1.py` |
| `NewOrderRespTypeOrStr` | `binance_public_spot_api/models/enums/new_order_resp_type.py` |
| `SelfTradePreventionModeOrStr` | `binance_public_spot_api/models/enums/self_trade_prevention_mode.py` |
| `WorkingTimeInForceOrStr` | `binance_public_spot_api/models/enums/working_time_in_force.py` |
| `PendingAboveTimeInForceOrStr` | `binance_public_spot_api/models/enums/pending_above_time_in_force.py` |
| `PendingBelowTypeOrStr` | `binance_public_spot_api/models/enums/pending_below_type.py` |
| `PendingBelowTimeInForceOrStr` | `binance_public_spot_api/models/enums/pending_below_time_in_force.py` |
| `SapiV1MarginOrderOtocoResponse` | `binance_public_spot_api/models/sapi_v1_margin_order_otoco_response.py` |
| `MarginAccountNewOtocoTradeErrorBody` | `binance_public_spot_api/errors/margin_account_new_otoco_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.margin_account_new_order_trade

- **Route**: `POST /sapi/v1/margin/order`
- **Auth**: `api_key_auth`
- **Signature**: `def margin_account_new_order_trade(symbol: str, side: SideOrStr, type_: Type1OrStr, quantity: float, auto_repay_at_cancel: bool, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, quote_order_qty: float | None = None, price: float | None = None, stop_price: float | None = None, new_client_order_id: str | None = None, iceberg_qty: float | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, side_effect_type: SideEffectTypeOrStr | None = None, time_in_force: TimeInForceOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `side`, `type_`, `quantity`, `auto_repay_at_cancel`, `timestamp`, `signature`
- **Params**: `symbol` — query · `side` — query · `type_` — query `type` · `quantity` — query · `auto_repay_at_cancel` — query `autoRepayAtCancel` · `timestamp` — query · `signature` — query · `is_isolated` — query `isIsolated` · `quote_order_qty` — query `quoteOrderQty` · `price` — query · `stop_price` — query `stopPrice` · `new_client_order_id` — query `newClientOrderId` · `iceberg_qty` — query `icebergQty` · `new_order_resp_type` — query `newOrderRespType` · `side_effect_type` — query `sideEffectType` · `time_in_force` — query `timeInForce` · `self_trade_prevention_mode` — query `selfTradePreventionMode` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginOrderResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginOrderResponse, MarginAccountNewOrderTradeErrorBody]`
- **Error**: `MarginAccountNewOrderTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SideOrStr` | `binance_public_spot_api/models/enums/side.py` |
| `Type1OrStr` | `binance_public_spot_api/models/enums/type1.py` |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `NewOrderRespTypeOrStr` | `binance_public_spot_api/models/enums/new_order_resp_type.py` |
| `SideEffectTypeOrStr` | `binance_public_spot_api/models/enums/side_effect_type.py` |
| `TimeInForceOrStr` | `binance_public_spot_api/models/enums/time_in_force.py` |
| `SelfTradePreventionModeOrStr` | `binance_public_spot_api/models/enums/self_trade_prevention_mode.py` |
| `SapiV1MarginOrderResponse` | `binance_public_spot_api/models/unions/sapi_v1_margin_order_response.py` |
| `MarginAccountNewOrderTradeErrorBody` | `binance_public_spot_api/errors/margin_account_new_order_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.margin_interest_rate_history_user_data

- **Route**: `GET /sapi/v1/margin/interestRateHistory`
- **Auth**: `api_key_auth`
- **Signature**: `def margin_interest_rate_history_user_data(asset: str, timestamp: int, signature: str, *, vip_level: int | None = None, start_time: int | None = None, end_time: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset`, `timestamp`, `signature`
- **Params**: `asset` — query · `timestamp` — query · `signature` — query · `vip_level` — query `vipLevel` · `start_time` — query `startTime` · `end_time` — query `endTime` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1MarginInterestRateHistoryResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginInterestRateHistoryResponse], MarginInterestRateHistoryUserDataErrorBody]`
- **Error**: `MarginInterestRateHistoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginInterestRateHistoryResponse` | `binance_public_spot_api/models/sapi_v1_margin_interest_rate_history_response.py` |
| `MarginInterestRateHistoryUserDataErrorBody` | `binance_public_spot_api/errors/margin_interest_rate_history_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.margin_account_borrow_repay_margin

- **Route**: `POST /sapi/v1/margin/borrow-repay`
- **Auth**: `api_key_auth`
- **Signature**: `def margin_account_borrow_repay_margin(asset: str, is_isolated: str, symbol: str, amount: float, type_: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset`, `is_isolated`, `symbol`, `amount`, `type_`, `timestamp`, `signature`
- **Params**: `asset` — query · `is_isolated` — query `isIsolated` · `symbol` — query · `amount` — query · `type_` — query `type` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginBorrowRepayResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginBorrowRepayResponse, MarginAccountBorrowRepayMarginErrorBody]`
- **Error**: `MarginAccountBorrowRepayMarginErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginBorrowRepayResponse` | `binance_public_spot_api/models/sapi_v1_margin_borrow_repay_response.py` |
| `MarginAccountBorrowRepayMarginErrorBody` | `binance_public_spot_api/errors/margin_account_borrow_repay_margin_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.margin_manual_liquidation_margin

- **Route**: `POST /sapi/v1/margin/manual-liquidation`
- **Auth**: `api_key_auth`
- **Signature**: `def margin_manual_liquidation_margin(type_: Type4OrStr, timestamp: int, signature: str, *, symbol: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`, `timestamp`, `signature`
- **Params**: `type_` — query `type` · `timestamp` — query · `signature` — query · `symbol` — query
- **Returns (parsed)**: `list[SapiV1MarginManualLiquidationResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginManualLiquidationResponse], MarginManualLiquidationMarginErrorBody]`
- **Error**: `MarginManualLiquidationMarginErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Type4OrStr` | `binance_public_spot_api/models/enums/type4.py` |
| `SapiV1MarginManualLiquidationResponse` | `binance_public_spot_api/models/sapi_v1_margin_manual_liquidation_response.py` |
| `MarginManualLiquidationMarginErrorBody` | `binance_public_spot_api/errors/margin_manual_liquidation_margin_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_cross_margin_account_details_user_data

- **Route**: `GET /sapi/v1/margin/account`
- **Auth**: `api_key_auth`
- **Signature**: `def query_cross_margin_account_details_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginAccountResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginAccountResponse, QueryCrossMarginAccountDetailsUserDataErrorBody]`
- **Error**: `QueryCrossMarginAccountDetailsUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginAccountResponse` | `binance_public_spot_api/models/sapi_v1_margin_account_response.py` |
| `QueryCrossMarginAccountDetailsUserDataErrorBody` | `binance_public_spot_api/errors/query_cross_margin_account_details_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_cross_margin_fee_data_user_data

- **Route**: `GET /sapi/v1/margin/crossMarginData`
- **Auth**: `api_key_auth`
- **Signature**: `def query_cross_margin_fee_data_user_data(timestamp: int, signature: str, *, vip_level: int | None = None, coin: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `vip_level` — query `vipLevel` · `coin` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1MarginCrossMarginDataResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginCrossMarginDataResponse], QueryCrossMarginFeeDataUserDataErrorBody]`
- **Error**: `QueryCrossMarginFeeDataUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginCrossMarginDataResponse` | `binance_public_spot_api/models/sapi_v1_margin_cross_margin_data_response.py` |
| `QueryCrossMarginFeeDataUserDataErrorBody` | `binance_public_spot_api/errors/query_cross_margin_fee_data_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_current_margin_order_count_usage_trade

- **Route**: `GET /sapi/v1/margin/rateLimit/order`
- **Auth**: `api_key_auth`
- **Signature**: `def query_current_margin_order_count_usage_trade(timestamp: int, signature: str, *, is_isolated: str | None = None, symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `is_isolated` — query `isIsolated` · `symbol` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1MarginRateLimitOrderResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginRateLimitOrderResponse], QueryCurrentMarginOrderCountUsageTradeErrorBody]`
- **Error**: `QueryCurrentMarginOrderCountUsageTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginRateLimitOrderResponse` | `binance_public_spot_api/models/sapi_v1_margin_rate_limit_order_response.py` |
| `QueryCurrentMarginOrderCountUsageTradeErrorBody` | `binance_public_spot_api/errors/query_current_margin_order_count_usage_trade_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_enabled_isolated_margin_account_limit_user_data

- **Route**: `GET /sapi/v1/margin/isolated/accountLimit`
- **Auth**: `api_key_auth`
- **Signature**: `def query_enabled_isolated_margin_account_limit_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginIsolatedAccountLimitResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginIsolatedAccountLimitResponse, QueryEnabledIsolatedMarginAccountLimitUserDataErrorBody]`
- **Error**: `QueryEnabledIsolatedMarginAccountLimitUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginIsolatedAccountLimitResponse` | `binance_public_spot_api/models/sapi_v1_margin_isolated_account_limit_response.py` |
| `QueryEnabledIsolatedMarginAccountLimitUserDataErrorBody` | `binance_public_spot_api/errors/query_enabled_isolated_margin_account_limit_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_isolated_margin_account_info_user_data

- **Route**: `GET /sapi/v1/margin/isolated/account`
- **Auth**: `api_key_auth`
- **Signature**: `def query_isolated_margin_account_info_user_data(timestamp: int, signature: str, *, symbols: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `symbols` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `IsolatedMarginAccountInfo`
- **Returns (raw)**: `ApiResult[IsolatedMarginAccountInfo, QueryIsolatedMarginAccountInfoUserDataErrorBody]`
- **Error**: `QueryIsolatedMarginAccountInfoUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IsolatedMarginAccountInfo` | `binance_public_spot_api/models/isolated_margin_account_info.py` |
| `QueryIsolatedMarginAccountInfoUserDataErrorBody` | `binance_public_spot_api/errors/query_isolated_margin_account_info_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_isolated_margin_fee_data_user_data

- **Route**: `GET /sapi/v1/margin/isolatedMarginData`
- **Auth**: `api_key_auth`
- **Signature**: `def query_isolated_margin_fee_data_user_data(timestamp: int, signature: str, *, vip_level: int | None = None, symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `vip_level` — query `vipLevel` · `symbol` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1MarginIsolatedMarginDataResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginIsolatedMarginDataResponse], QueryIsolatedMarginFeeDataUserDataErrorBody]`
- **Error**: `QueryIsolatedMarginFeeDataUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginIsolatedMarginDataResponse` | `binance_public_spot_api/models/sapi_v1_margin_isolated_margin_data_response.py` |
| `QueryIsolatedMarginFeeDataUserDataErrorBody` | `binance_public_spot_api/errors/query_isolated_margin_fee_data_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_isolated_margin_tier_data_user_data

- **Route**: `GET /sapi/v1/margin/isolatedMarginTier`
- **Auth**: `api_key_auth`
- **Signature**: `def query_isolated_margin_tier_data_user_data(symbol: str, timestamp: int, signature: str, *, tier: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `tier` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1MarginIsolatedMarginTierResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginIsolatedMarginTierResponse], QueryIsolatedMarginTierDataUserDataErrorBody]`
- **Error**: `QueryIsolatedMarginTierDataUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginIsolatedMarginTierResponse` | `binance_public_spot_api/models/sapi_v1_margin_isolated_margin_tier_response.py` |
| `QueryIsolatedMarginTierDataUserDataErrorBody` | `binance_public_spot_api/errors/query_isolated_margin_tier_data_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data

- **Route**: `GET /sapi/v1/margin/leverageBracket`
- **Auth**: `api_key_auth`
- **Signature**: `def query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[SapiV1MarginLeverageBracketResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginLeverageBracketResponse], QueryLiabilityCoinLeverageBracketInCrossMarginProModeMarketDataErrorBody]`
- **Error**: `QueryLiabilityCoinLeverageBracketInCrossMarginProModeMarketDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginLeverageBracketResponse` | `binance_public_spot_api/models/sapi_v1_margin_leverage_bracket_response.py` |
| `QueryLiabilityCoinLeverageBracketInCrossMarginProModeMarketDataErrorBody` | `binance_public_spot_api/errors/query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_margin_account_s_all_orders_user_data

- **Route**: `GET /sapi/v1/margin/allOrders`
- **Auth**: `api_key_auth`
- **Signature**: `def query_margin_account_s_all_orders_user_data(symbol: str, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, order_id: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `is_isolated` — query `isIsolated` · `order_id` — query `orderId` · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[MarginOrderDetail]`
- **Returns (raw)**: `ApiResult[list[MarginOrderDetail], QueryMarginAccountSAllOrdersUserDataErrorBody]`
- **Error**: `QueryMarginAccountSAllOrdersUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `MarginOrderDetail` | `binance_public_spot_api/models/margin_order_detail.py` |
| `QueryMarginAccountSAllOrdersUserDataErrorBody` | `binance_public_spot_api/errors/query_margin_account_s_all_orders_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_margin_account_s_oco_user_data

- **Route**: `GET /sapi/v1/margin/orderList`
- **Auth**: `api_key_auth`
- **Signature**: `def query_margin_account_s_oco_user_data(timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, symbol: str | None = None, order_list_id: int | None = None, orig_client_order_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `is_isolated` — query `isIsolated` · `symbol` — query · `order_list_id` — query `orderListId` · `orig_client_order_id` — query `origClientOrderId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginOrderListResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginOrderListResponse, QueryMarginAccountSOcoUserDataErrorBody]`
- **Error**: `QueryMarginAccountSOcoUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `SapiV1MarginOrderListResponse` | `binance_public_spot_api/models/sapi_v1_margin_order_list_response.py` |
| `QueryMarginAccountSOcoUserDataErrorBody` | `binance_public_spot_api/errors/query_margin_account_s_oco_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_margin_account_s_open_oco_user_data

- **Route**: `GET /sapi/v1/margin/openOrderList`
- **Auth**: `api_key_auth`
- **Signature**: `def query_margin_account_s_open_oco_user_data(timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `is_isolated` — query `isIsolated` · `symbol` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1MarginOpenOrderListResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginOpenOrderListResponse], QueryMarginAccountSOpenOcoUserDataErrorBody]`
- **Error**: `QueryMarginAccountSOpenOcoUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `SapiV1MarginOpenOrderListResponse` | `binance_public_spot_api/models/sapi_v1_margin_open_order_list_response.py` |
| `QueryMarginAccountSOpenOcoUserDataErrorBody` | `binance_public_spot_api/errors/query_margin_account_s_open_oco_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_margin_account_s_open_orders_user_data

- **Route**: `GET /sapi/v1/margin/openOrders`
- **Auth**: `api_key_auth`
- **Signature**: `def query_margin_account_s_open_orders_user_data(timestamp: int, signature: str, *, symbol: str | None = None, is_isolated: IsIsolatedOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `symbol` — query · `is_isolated` — query `isIsolated` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[MarginOrderDetail]`
- **Returns (raw)**: `ApiResult[list[MarginOrderDetail], QueryMarginAccountSOpenOrdersUserDataErrorBody]`
- **Error**: `QueryMarginAccountSOpenOrdersUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `MarginOrderDetail` | `binance_public_spot_api/models/margin_order_detail.py` |
| `QueryMarginAccountSOpenOrdersUserDataErrorBody` | `binance_public_spot_api/errors/query_margin_account_s_open_orders_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_margin_account_s_order_user_data

- **Route**: `GET /sapi/v1/margin/order`
- **Auth**: `api_key_auth`
- **Signature**: `def query_margin_account_s_order_user_data(symbol: str, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, order_id: int | None = None, orig_client_order_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `is_isolated` — query `isIsolated` · `order_id` — query `orderId` · `orig_client_order_id` — query `origClientOrderId` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `MarginOrderDetail`
- **Returns (raw)**: `ApiResult[MarginOrderDetail, QueryMarginAccountSOrderUserDataErrorBody]`
- **Error**: `QueryMarginAccountSOrderUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `MarginOrderDetail` | `binance_public_spot_api/models/margin_order_detail.py` |
| `QueryMarginAccountSOrderUserDataErrorBody` | `binance_public_spot_api/errors/query_margin_account_s_order_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_margin_account_s_trade_list_user_data

- **Route**: `GET /sapi/v1/margin/myTrades`
- **Auth**: `api_key_auth`
- **Signature**: `def query_margin_account_s_trade_list_user_data(symbol: str, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, start_time: int | None = None, end_time: int | None = None, from_id: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `timestamp`, `signature`
- **Params**: `symbol` — query · `timestamp` — query · `signature` — query · `is_isolated` — query `isIsolated` · `start_time` — query `startTime` · `end_time` — query `endTime` · `from_id` — query `fromId` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[MarginTrade]`
- **Returns (raw)**: `ApiResult[list[MarginTrade], QueryMarginAccountSTradeListUserDataErrorBody]`
- **Error**: `QueryMarginAccountSTradeListUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `MarginTrade` | `binance_public_spot_api/models/margin_trade.py` |
| `QueryMarginAccountSTradeListUserDataErrorBody` | `binance_public_spot_api/errors/query_margin_account_s_trade_list_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_margin_account_s_all_oco_user_data

- **Route**: `GET /sapi/v1/margin/allOrderList`
- **Auth**: `api_key_auth`
- **Signature**: `def query_margin_account_s_all_oco_user_data(timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, symbol: str | None = None, from_id: str | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `is_isolated` — query `isIsolated` · `symbol` — query · `from_id` — query `fromId` · `start_time` — query `startTime` · `end_time` — query `endTime` · `limit` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `list[SapiV1MarginAllOrderListResponse]`
- **Returns (raw)**: `ApiResult[list[SapiV1MarginAllOrderListResponse], QueryMarginAccountSAllOcoUserDataErrorBody]`
- **Error**: `QueryMarginAccountSAllOcoUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IsIsolatedOrStr` | `binance_public_spot_api/models/enums/is_isolated.py` |
| `SapiV1MarginAllOrderListResponse` | `binance_public_spot_api/models/sapi_v1_margin_all_order_list_response.py` |
| `QueryMarginAccountSAllOcoUserDataErrorBody` | `binance_public_spot_api/errors/query_margin_account_s_all_oco_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_margin_available_inventory_user_data

- **Route**: `GET /sapi/v1/margin/available-inventory`
- **Auth**: `api_key_auth`
- **Signature**: `def query_margin_available_inventory_user_data(type_: Type4OrStr, timestamp: int, signature: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `type_`, `timestamp`, `signature`
- **Params**: `type_` — query `type` · `timestamp` — query · `signature` — query
- **Returns (parsed)**: `SapiV1MarginAvailableInventoryResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginAvailableInventoryResponse, QueryMarginAvailableInventoryUserDataErrorBody]`
- **Error**: `QueryMarginAvailableInventoryUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Type4OrStr` | `binance_public_spot_api/models/enums/type4.py` |
| `SapiV1MarginAvailableInventoryResponse` | `binance_public_spot_api/models/sapi_v1_margin_available_inventory_response.py` |
| `QueryMarginAvailableInventoryUserDataErrorBody` | `binance_public_spot_api/errors/query_margin_available_inventory_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_margin_price_index_market_data

- **Route**: `GET /sapi/v1/margin/priceIndex`
- **Auth**: `api_key_auth`
- **Signature**: `def query_margin_price_index_market_data(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `SapiV1MarginPriceIndexResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginPriceIndexResponse, QueryMarginPriceIndexMarketDataErrorBody]`
- **Error**: `QueryMarginPriceIndexMarketDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginPriceIndexResponse` | `binance_public_spot_api/models/sapi_v1_margin_price_index_response.py` |
| `QueryMarginPriceIndexMarketDataErrorBody` | `binance_public_spot_api/errors/query_margin_price_index_market_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_max_borrow_user_data

- **Route**: `GET /sapi/v1/margin/maxBorrowable`
- **Auth**: `api_key_auth`
- **Signature**: `def query_max_borrow_user_data(asset: str, timestamp: int, signature: str, *, isolated_symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset`, `timestamp`, `signature`
- **Params**: `asset` — query · `timestamp` — query · `signature` — query · `isolated_symbol` — query `isolatedSymbol` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginMaxBorrowableResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginMaxBorrowableResponse, QueryMaxBorrowUserDataErrorBody]`
- **Error**: `QueryMaxBorrowUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginMaxBorrowableResponse` | `binance_public_spot_api/models/sapi_v1_margin_max_borrowable_response.py` |
| `QueryMaxBorrowUserDataErrorBody` | `binance_public_spot_api/errors/query_max_borrow_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_max_transfer_out_amount_user_data

- **Route**: `GET /sapi/v1/margin/maxTransferable`
- **Auth**: `api_key_auth`
- **Signature**: `def query_max_transfer_out_amount_user_data(asset: str, timestamp: int, signature: str, *, isolated_symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset`, `timestamp`, `signature`
- **Params**: `asset` — query · `timestamp` — query · `signature` — query · `isolated_symbol` — query `isolatedSymbol` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginMaxTransferableResponse`
- **Returns (raw)**: `ApiResult[SapiV1MarginMaxTransferableResponse, QueryMaxTransferOutAmountUserDataErrorBody]`
- **Error**: `QueryMaxTransferOutAmountUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginMaxTransferableResponse` | `binance_public_spot_api/models/sapi_v1_margin_max_transferable_response.py` |
| `QueryMaxTransferOutAmountUserDataErrorBody` | `binance_public_spot_api/errors/query_max_transfer_out_amount_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.query_borrow_repay_records_in_margin_account_user_data

- **Route**: `GET /sapi/v1/margin/borrow-repay`
- **Auth**: `api_key_auth`
- **Signature**: `def query_borrow_repay_records_in_margin_account_user_data(asset: str, type_: str, timestamp: int, signature: str, *, isolated_symbol: str | None = None, tx_id: int | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asset`, `type_`, `timestamp`, `signature`
- **Params**: `asset` — query · `type_` — query `type` · `timestamp` — query · `signature` — query · `isolated_symbol` — query `isolatedSymbol` · `tx_id` — query `txId` · `start_time` — query `startTime` · `end_time` — query `endTime` · `current` — query · `size` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1MarginBorrowRepayResponse1`
- **Returns (raw)**: `ApiResult[SapiV1MarginBorrowRepayResponse1, QueryBorrowRepayRecordsInMarginAccountUserDataErrorBody]`
- **Error**: `QueryBorrowRepayRecordsInMarginAccountUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1MarginBorrowRepayResponse1` | `binance_public_spot_api/models/sapi_v1_margin_borrow_repay_response1.py` |
| `QueryBorrowRepayRecordsInMarginAccountUserDataErrorBody` | `binance_public_spot_api/errors/query_borrow_repay_records_in_margin_account_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

### client.margin.toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data

- **Route**: `POST /sapi/v1/bnbBurn`
- **Auth**: `api_key_auth`
- **Signature**: `def toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data(timestamp: int, signature: str, *, spot_bnb_burn: SpotBnbburnOrStr | None = None, interest_bnb_burn: InterestBnbburnOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `spot_bnb_burn` — query `spotBNBBurn` · `interest_bnb_burn` — query `interestBNBBurn` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `BnbBurnStatus`
- **Returns (raw)**: `ApiResult[BnbBurnStatus, ToggleBnbBurnOnSpotTradeAndMarginInterestUserDataErrorBody]`
- **Error**: `ToggleBnbBurnOnSpotTradeAndMarginInterestUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SpotBnbburnOrStr` | `binance_public_spot_api/models/enums/spot_bnbburn.py` |
| `InterestBnbburnOrStr` | `binance_public_spot_api/models/enums/interest_bnbburn.py` |
| `BnbBurnStatus` | `binance_public_spot_api/models/bnb_burn_status.py` |
| `ToggleBnbBurnOnSpotTradeAndMarginInterestUserDataErrorBody` | `binance_public_spot_api/errors/toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data_error.py` |
| `Error` | `binance_public_spot_api/models/error.py` |

