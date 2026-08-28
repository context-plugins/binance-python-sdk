# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [BinanceClient](binance/client.py)

## AutoInvest

> Source: [AutoInvest](binance/apis/auto_invest.py)

<details>
<summary><code>def change_plan_status(plan_id: int, status: Status1OrStr, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingAutoInvestPlanEditStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Change Plan Status

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.change_plan_status(plan_id, status, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestPlanEditStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangePlanStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.change_plan_status(plan_id, status, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestPlanEditStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangePlanStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>plan_id</code> | <code>int</code> | Value sent with the request. |
| <code>status</code> | <code>[Status1OrStr](binance/models/enums/status1.py)</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingAutoInvestPlanEditStatusResponse](binance/models/sapi_v1_lending_auto_invest_plan_edit_status_response.py)</code> -- Plan result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[ChangePlanStatusErrorBody](binance/errors/change_plan_status_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_list_of_plans(plan_type: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingAutoInvestPlanListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query plan lists

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.get_list_of_plans(plan_type, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestPlanListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListOfPlansErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.get_list_of_plans(plan_type, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestPlanListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListOfPlansErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>plan_type</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingAutoInvestPlanListResponse](binance/models/sapi_v1_lending_auto_invest_plan_list_response.py)</code> -- Plan result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetListOfPlansErrorBody](binance/errors/get_list_of_plans_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_target_asset_roi_data_user_data(target_asset: str, his_roi_type: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1LendingAutoInvestTargetAssetRoiListResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

ROI return list for target asset

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.get_target_asset_roi_data_user_data(target_asset, his_roi_type, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1LendingAutoInvestTargetAssetRoiListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTargetAssetRoiDataUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.get_target_asset_roi_data_user_data(
        target_asset, his_roi_type, timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1LendingAutoInvestTargetAssetRoiListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTargetAssetRoiDataUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>target_asset</code> | <code>str</code> | Value sent with the request. |
| <code>his_roi_type</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1LendingAutoInvestTargetAssetRoiListResponse](binance/models/sapi_v1_lending_auto_invest_target_asset_roi_list_response.py)&#93;</code> -- Target asset list

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetTargetAssetRoiDataUserDataErrorBody](binance/errors/get_target_asset_roi_data_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_target_asset_list_user_data(timestamp: int, signature: str, *, target_asset: str | None = None, size: int | None = None, current: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingAutoInvestTargetAssetListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.get_target_asset_list_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestTargetAssetListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTargetAssetListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.get_target_asset_list_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestTargetAssetListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTargetAssetListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>target_asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingAutoInvestTargetAssetListResponse](binance/models/sapi_v1_lending_auto_invest_target_asset_list_response.py)</code> -- Target asset list

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetTargetAssetListUserDataErrorBody](binance/errors/get_target_asset_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def index_linked_plan_rebalance_details_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1LendingAutoInvestRebalanceHistoryResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the history of Index Linked Plan Redemption transactions

Max 30 day difference between startTime and endTime
If no startTime and endTime, default to show past 30 day records

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.index_linked_plan_rebalance_details_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1LendingAutoInvestRebalanceHistoryResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IndexLinkedPlanRebalanceDetailsUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.index_linked_plan_rebalance_details_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1LendingAutoInvestRebalanceHistoryResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IndexLinkedPlanRebalanceDetailsUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1LendingAutoInvestRebalanceHistoryResponse](binance/models/sapi_v1_lending_auto_invest_rebalance_history_response.py)&#93;</code> -- Rebalance Details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[IndexLinkedPlanRebalanceDetailsUserDataErrorBody](binance/errors/index_linked_plan_rebalance_details_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def index_linked_plan_redemption_trade(index_id: int, redemption_percentage: int, timestamp: int, signature: str, *, request_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingAutoInvestRedeemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To redeem index-Linked plan holdings

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.index_linked_plan_redemption_trade(
        index_id, redemption_percentage, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestRedeemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IndexLinkedPlanRedemptionTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.index_linked_plan_redemption_trade(
        index_id, redemption_percentage, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestRedeemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IndexLinkedPlanRedemptionTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>index_id</code> | <code>int</code> | PORTFOLIO plan's Id |
| <code>redemption_percentage</code> | <code>int</code> | user redeem percentage,10/20/100. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>request_id</code> | <code>str \| None</code> | sourceType + unique, transactionId and requestId cannot be empty at the same time<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingAutoInvestRedeemResponse](binance/models/sapi_v1_lending_auto_invest_redeem_response.py)</code> -- Redemption result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[IndexLinkedPlanRedemptionTradeErrorBody](binance/errors/index_linked_plan_redemption_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def index_linked_plan_redemption_history_user_data(request_id: int, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, asset: str | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1LendingAutoInvestRedeemHistoryResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the history of Index Linked Plan Redemption transactions

Max 30 day difference between startTime and endTime
If no startTime and endTime, default to show past 30 day records

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.index_linked_plan_redemption_history_user_data(request_id, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1LendingAutoInvestRedeemHistoryResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IndexLinkedPlanRedemptionHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.index_linked_plan_redemption_history_user_data(
        request_id, timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1LendingAutoInvestRedeemHistoryResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IndexLinkedPlanRedemptionHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_id</code> | <code>int</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1LendingAutoInvestRedeemHistoryResponse](binance/models/sapi_v1_lending_auto_invest_redeem_history_response.py)&#93;</code> -- Redemption history

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[IndexLinkedPlanRedemptionHistoryUserDataErrorBody](binance/errors/index_linked_plan_redemption_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def investment_plan_adjustment(plan_id: int, subscription_amount: float, subscription_cycle: SubscriptionCycleOrStr, subscription_start_time: int, source_asset: str, timestamp: int, signature: str, *, subscription_start_day: int | None = None, subscription_start_weekday: SubscriptionStartWeekdayOrStr | None = None, flexible_allowed_to_use: bool | None = None, details: list[Detail1 | Detail1Dict] | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingAutoInvestPlanEditResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query Source Asset to be used for investment

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.investment_plan_adjustment(
        plan_id, subscription_amount, subscription_cycle, subscription_start_time, source_asset, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestPlanEditResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InvestmentPlanAdjustmentErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.investment_plan_adjustment(
        plan_id, subscription_amount, subscription_cycle, subscription_start_time, source_asset, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestPlanEditResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InvestmentPlanAdjustmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>plan_id</code> | <code>int</code> | Value sent with the request. |
| <code>subscription_amount</code> | <code>float</code> | Value sent with the request. |
| <code>subscription_cycle</code> | <code>[SubscriptionCycleOrStr](binance/models/enums/subscription_cycle.py)</code> | Value sent with the request. |
| <code>subscription_start_time</code> | <code>int</code> | Value sent with the request. |
| <code>source_asset</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>subscription_start_day</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>subscription_start_weekday</code> | <code>[SubscriptionStartWeekdayOrStr](binance/models/enums/subscription_start_weekday.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>flexible_allowed_to_use</code> | <code>bool \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>details</code> | <code>list&#91;[Detail1](binance/models/detail1.py) \| [Detail1Dict](binance/models/detail1.py)&#93; \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingAutoInvestPlanEditResponse](binance/models/sapi_v1_lending_auto_invest_plan_edit_response.py)</code> -- Plan result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[InvestmentPlanAdjustmentErrorBody](binance/errors/investment_plan_adjustment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def investment_plan_creation_user_data(source_type: SourceTypeOrStr, plan_type: PlanTypeOrStr, subscription_amount: float, subscription_cycle: SubscriptionCycleOrStr, subscription_start_time: int, source_asset: str, details: list[Detail1 | Detail1Dict], timestamp: int, signature: str, *, request_id: str | None = None, index_id: int | None = None, subscription_start_day: int | None = None, subscription_start_weekday: SubscriptionStartWeekdayOrStr | None = None, flexible_allowed_to_use: bool | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingAutoInvestPlanAddResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Post an investment plan creation

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.investment_plan_creation_user_data(
        source_type,
        plan_type,
        subscription_amount,
        subscription_cycle,
        subscription_start_time,
        source_asset,
        details,
        timestamp,
        signature,
    )
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestPlanAddResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InvestmentPlanCreationUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.investment_plan_creation_user_data(
        source_type,
        plan_type,
        subscription_amount,
        subscription_cycle,
        subscription_start_time,
        source_asset,
        details,
        timestamp,
        signature,
    )
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestPlanAddResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InvestmentPlanCreationUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>source_type</code> | <code>[SourceTypeOrStr](binance/models/enums/source_type.py)</code> | Value sent with the request. |
| <code>plan_type</code> | <code>[PlanTypeOrStr](binance/models/enums/plan_type.py)</code> | Value sent with the request. |
| <code>subscription_amount</code> | <code>float</code> | Value sent with the request. |
| <code>subscription_cycle</code> | <code>[SubscriptionCycleOrStr](binance/models/enums/subscription_cycle.py)</code> | Value sent with the request. |
| <code>subscription_start_time</code> | <code>int</code> | Value sent with the request. |
| <code>source_asset</code> | <code>str</code> | Value sent with the request. |
| <code>details</code> | <code>list&#91;[Detail1](binance/models/detail1.py) \| [Detail1Dict](binance/models/detail1.py)&#93;</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>request_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>index_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>subscription_start_day</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>subscription_start_weekday</code> | <code>[SubscriptionStartWeekdayOrStr](binance/models/enums/subscription_start_weekday.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>flexible_allowed_to_use</code> | <code>bool \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingAutoInvestPlanAddResponse](binance/models/sapi_v1_lending_auto_invest_plan_add_response.py)</code> -- Plan result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[InvestmentPlanCreationUserDataErrorBody](binance/errors/investment_plan_creation_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def one_time_transaction_trade(source_type: str, subscription_amount: float, source_asset: str, timestamp: int, signature: str, *, request_id: str | None = None, flexible_allowed_to_use: bool | None = None, plan_id: int | None = None, index_id: int | None = None, details: list[Detail5 | Detail5Dict] | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingAutoInvestOneOffResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

One time transaction

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.one_time_transaction_trade(
        source_type, subscription_amount, source_asset, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestOneOffResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OneTimeTransactionTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.one_time_transaction_trade(
        source_type, subscription_amount, source_asset, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestOneOffResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OneTimeTransactionTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>source_type</code> | <code>str</code> | Value sent with the request. |
| <code>subscription_amount</code> | <code>float</code> | Value sent with the request. |
| <code>source_asset</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>request_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>flexible_allowed_to_use</code> | <code>bool \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>plan_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>index_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>details</code> | <code>list&#91;[Detail5](binance/models/detail5.py) \| [Detail5Dict](binance/models/detail5.py)&#93; \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingAutoInvestOneOffResponse](binance/models/sapi_v1_lending_auto_invest_one_off_response.py)</code> -- transaction result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[OneTimeTransactionTradeErrorBody](binance/errors/one_time_transaction_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_index_details_user_data(index_id: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingAutoInvestIndexInfoResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query index details

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.query_index_details_user_data(index_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestIndexInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryIndexDetailsUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.query_index_details_user_data(index_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestIndexInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryIndexDetailsUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>index_id</code> | <code>int</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingAutoInvestIndexInfoResponse](binance/models/sapi_v1_lending_auto_invest_index_info_response.py)</code> -- Index result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryIndexDetailsUserDataErrorBody](binance/errors/query_index_details_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_index_linked_plan_position_details_user_data(index_id: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingAutoInvestIndexUserSummaryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Details on users Index-Linked plan position details

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.query_index_linked_plan_position_details_user_data(index_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestIndexUserSummaryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryIndexLinkedPlanPositionDetailsUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.query_index_linked_plan_position_details_user_data(
        index_id, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestIndexUserSummaryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryIndexLinkedPlanPositionDetailsUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>index_id</code> | <code>int</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingAutoInvestIndexUserSummaryResponse](binance/models/sapi_v1_lending_auto_invest_index_user_summary_response.py)</code> -- Position Details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryIndexLinkedPlanPositionDetailsUserDataErrorBody](binance/errors/query_index_linked_plan_position_details_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_one_time_transaction_status_user_data(transaction_id: int, timestamp: int, signature: str, *, request_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingAutoInvestOneOffStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Transaction status for one-time transaction

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.query_one_time_transaction_status_user_data(transaction_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestOneOffStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryOneTimeTransactionStatusUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.query_one_time_transaction_status_user_data(
        transaction_id, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestOneOffStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryOneTimeTransactionStatusUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>transaction_id</code> | <code>int</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>request_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingAutoInvestOneOffStatusResponse](binance/models/sapi_v1_lending_auto_invest_one_off_status_response.py)</code> -- transaction result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryOneTimeTransactionStatusUserDataErrorBody](binance/errors/query_one_time_transaction_status_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_all_source_asset_and_target_asset_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingAutoInvestAllAssetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query all source assets and target assets

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.query_all_source_asset_and_target_asset_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestAllAssetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryAllSourceAssetAndTargetAssetUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.query_all_source_asset_and_target_asset_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestAllAssetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryAllSourceAssetAndTargetAssetUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingAutoInvestAllAssetResponse](binance/models/sapi_v1_lending_auto_invest_all_asset_response.py)</code> -- Target asset

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryAllSourceAssetAndTargetAssetUserDataErrorBody](binance/errors/query_all_source_asset_and_target_asset_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_holding_details_of_the_plan(timestamp: int, signature: str, *, plan_id: int | None = None, request_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingAutoInvestPlanIdResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query holding details of the plan

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.query_holding_details_of_the_plan(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestPlanIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryHoldingDetailsOfThePlanErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.query_holding_details_of_the_plan(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestPlanIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryHoldingDetailsOfThePlanErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>plan_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingAutoInvestPlanIdResponse](binance/models/sapi_v1_lending_auto_invest_plan_id_response.py)</code> -- Plan result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryHoldingDetailsOfThePlanErrorBody](binance/errors/query_holding_details_of_the_plan_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_source_asset_list_user_data(usage_type: str, timestamp: int, signature: str, *, target_asset: str | None = None, index_id: int | None = None, flexible_allowed_to_use: bool | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingAutoInvestSourceAssetListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query Source Asset to be used for investment

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.query_source_asset_list_user_data(usage_type, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestSourceAssetListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySourceAssetListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.query_source_asset_list_user_data(usage_type, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingAutoInvestSourceAssetListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySourceAssetListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>usage_type</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>target_asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>index_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>flexible_allowed_to_use</code> | <code>bool \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingAutoInvestSourceAssetListResponse](binance/models/sapi_v1_lending_auto_invest_source_asset_list_response.py)</code> -- Asset list

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QuerySourceAssetListUserDataErrorBody](binance/errors/query_source_asset_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_subscription_transaction_history(timestamp: int, signature: str, *, plan_id: int | None = None, start_time: int | None = None, end_time: int | None = None, target_asset: int | None = None, plan_type: PlanType1OrStr | None = None, size: int | None = None, current: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1LendingAutoInvestHistoryListResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query subscription transaction history of a plan

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auto_invest.query_subscription_transaction_history(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1LendingAutoInvestHistoryListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySubscriptionTransactionHistoryErrorBody
```

**Async**

```python
try:
    response = await async_client.auto_invest.query_subscription_transaction_history(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1LendingAutoInvestHistoryListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySubscriptionTransactionHistoryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>plan_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>target_asset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>plan_type</code> | <code>[PlanType1OrStr](binance/models/enums/plan_type1.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1LendingAutoInvestHistoryListResponse](binance/models/sapi_v1_lending_auto_invest_history_list_response.py)&#93;</code> -- Plan result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QuerySubscriptionTransactionHistoryErrorBody](binance/errors/query_subscription_transaction_history_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Blvt

> Source: [Blvt](binance/apis/blvt.py)

<details>
<summary><code>def blvt_info_market_data(*, token_name: str | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1BlvtTokenInfoResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.blvt.blvt_info_market_data()
    # TODO: Handle 'response' of type list[SapiV1BlvtTokenInfoResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BlvtInfoMarketDataErrorBody
```

**Async**

```python
try:
    response = await async_client.blvt.blvt_info_market_data()
    # TODO: Handle 'response' of type list[SapiV1BlvtTokenInfoResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BlvtInfoMarketDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token_name</code> | <code>str \| None</code> | BTCDOWN, BTCUP<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1BlvtTokenInfoResponse](binance/models/sapi_v1_blvt_token_info_response.py)&#93;</code> -- List of token information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[BlvtInfoMarketDataErrorBody](binance/errors/blvt_info_market_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def blvt_user_limit_info_user_data(timestamp: int, signature: str, *, token_name: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1BlvtUserLimitResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.blvt.blvt_user_limit_info_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1BlvtUserLimitResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BlvtUserLimitInfoUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.blvt.blvt_user_limit_info_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1BlvtUserLimitResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BlvtUserLimitInfoUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>token_name</code> | <code>str \| None</code> | BTCDOWN, BTCUP<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1BlvtUserLimitResponse](binance/models/sapi_v1_blvt_user_limit_response.py)&#93;</code> -- List of token limits

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[BlvtUserLimitInfoUserDataErrorBody](binance/errors/blvt_user_limit_info_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_subscription_record_user_data(timestamp: int, signature: str, *, token_name: str | None = None, id: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1BlvtSubscribeRecordResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- Only the data of the latest 90 days is available

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.blvt.query_subscription_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1BlvtSubscribeRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySubscriptionRecordUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.blvt.query_subscription_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1BlvtSubscribeRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySubscriptionRecordUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>token_name</code> | <code>str \| None</code> | BTCDOWN, BTCUP<br>**Default**: <code>None</code> |
| <code>id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1BlvtSubscribeRecordResponse](binance/models/sapi_v1_blvt_subscribe_record_response.py)</code> -- List of subscription record

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QuerySubscriptionRecordUserDataErrorBody](binance/errors/query_subscription_record_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def redeem_blvt_user_data(token_name: str, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1BlvtRedeemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.blvt.redeem_blvt_user_data(token_name, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1BlvtRedeemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RedeemBlvtUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.blvt.redeem_blvt_user_data(token_name, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1BlvtRedeemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RedeemBlvtUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token_name</code> | <code>str</code> | BTCDOWN, BTCUP |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1BlvtRedeemResponse](binance/models/sapi_v1_blvt_redeem_response.py)</code> -- Redemption record

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RedeemBlvtUserDataErrorBody](binance/errors/redeem_blvt_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def redemption_record_user_data(timestamp: int, signature: str, *, token_name: str | None = None, id: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1BlvtRedeemRecordResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- Only the data of the latest 90 days is available

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.blvt.redemption_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1BlvtRedeemRecordResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RedemptionRecordUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.blvt.redemption_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1BlvtRedeemRecordResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RedemptionRecordUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>token_name</code> | <code>str \| None</code> | BTCDOWN, BTCUP<br>**Default**: <code>None</code> |
| <code>id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | default 1000, max 1000<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1BlvtRedeemRecordResponse](binance/models/sapi_v1_blvt_redeem_record_response.py)&#93;</code> -- List of redemption record

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RedemptionRecordUserDataErrorBody](binance/errors/redemption_record_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def subscribe_blvt_user_data(token_name: str, cost: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1BlvtSubscribeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.blvt.subscribe_blvt_user_data(token_name, cost, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1BlvtSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubscribeBlvtUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.blvt.subscribe_blvt_user_data(token_name, cost, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1BlvtSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubscribeBlvtUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token_name</code> | <code>str</code> | BTCDOWN, BTCUP |
| <code>cost</code> | <code>float</code> | Spot balance |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1BlvtSubscribeResponse](binance/models/sapi_v1_blvt_subscribe_response.py)</code> -- Subscription Info

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SubscribeBlvtUserDataErrorBody](binance/errors/subscribe_blvt_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## C2C

> Source: [C2C](binance/apis/c2_c.py)

<details>
<summary><code>def get_c2_c_trade_history_user_data(trade_type: TradeTypeOrStr, timestamp: int, signature: str, *, start_timestamp: int | None = None, end_timestamp: int | None = None, page: int | None = None, rows: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1C2COrderMatchListUserOrderHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If startTimestamp and endTimestamp are not sent, the recent 30-day data will be returned.
- The max interval between startTimestamp and endTimestamp is 30 days.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.c2_c.get_c2_c_trade_history_user_data(trade_type, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1C2COrderMatchListUserOrderHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetC2CTradeHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.c2_c.get_c2_c_trade_history_user_data(trade_type, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1C2COrderMatchListUserOrderHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetC2CTradeHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>trade_type</code> | <code>[TradeTypeOrStr](binance/models/enums/trade_type.py)</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_timestamp</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_timestamp</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>rows</code> | <code>int \| None</code> | default 100, max 100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1C2COrderMatchListUserOrderHistoryResponse](binance/models/sapi_v1_c2_c_order_match_list_user_order_history_response.py)</code> -- Trades history

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetC2CTradeHistoryUserDataErrorBody](binance/errors/get_c2_c_trade_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Convert

> Source: [Convert](binance/apis/convert.py)

<details>
<summary><code>def accept_quote_trade(quote_id: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ConvertAcceptQuoteResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Accept the offered quote by quote ID.

Weight(UID): 500

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.convert.accept_quote_trade(quote_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1ConvertAcceptQuoteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AcceptQuoteTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.convert.accept_quote_trade(quote_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1ConvertAcceptQuoteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AcceptQuoteTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>quote_id</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ConvertAcceptQuoteResponse](binance/models/sapi_v1_convert_accept_quote_response.py)</code> -- Accept Quote

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AcceptQuoteTradeErrorBody](binance/errors/accept_quote_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_limit_order_user_data(order_id: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ConvertLimitCancelOrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enable users to cancel a limit order

Weight(UID): 200

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.convert.cancel_limit_order_user_data(order_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1ConvertLimitCancelOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelLimitOrderUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.convert.cancel_limit_order_user_data(order_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1ConvertLimitCancelOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelLimitOrderUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>int</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ConvertLimitCancelOrderResponse](binance/models/sapi_v1_convert_limit_cancel_order_response.py)</code> -- Cancel Order

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CancelLimitOrderUserDataErrorBody](binance/errors/cancel_limit_order_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_convert_trade_history_user_data(start_time: int, end_time: int, timestamp: int, signature: str, *, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ConvertTradeFlowResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- The max interval between startTime and endTime is 30 days.

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.convert.get_convert_trade_history_user_data(start_time, end_time, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1ConvertTradeFlowResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetConvertTradeHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.convert.get_convert_trade_history_user_data(
        start_time, end_time, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ConvertTradeFlowResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetConvertTradeHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>start_time</code> | <code>int</code> | UTC timestamp in ms |
| <code>end_time</code> | <code>int</code> | UTC timestamp in ms |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>limit</code> | <code>int \| None</code> | default 100, max 1000<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ConvertTradeFlowResponse](binance/models/sapi_v1_convert_trade_flow_response.py)</code> -- Convert Trade History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetConvertTradeHistoryUserDataErrorBody](binance/errors/get_convert_trade_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_all_convert_pairs(*, from_asset: str | None = None, to_asset: str | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1ConvertExchangeInfoResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query for all convertible token pairs and the tokens’ respective upper/lower limits

Weight(IP): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.convert.list_all_convert_pairs()
    # TODO: Handle 'response' of type list[SapiV1ConvertExchangeInfoResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAllConvertPairsErrorBody
```

**Async**

```python
try:
    response = await async_client.convert.list_all_convert_pairs()
    # TODO: Handle 'response' of type list[SapiV1ConvertExchangeInfoResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAllConvertPairsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>from_asset</code> | <code>str \| None</code> | User spends coin<br>**Default**: <code>None</code> |
| <code>to_asset</code> | <code>str \| None</code> | User receives coin<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1ConvertExchangeInfoResponse](binance/models/sapi_v1_convert_exchange_info_response.py)&#93;</code> -- List Convert Pairs

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[ListAllConvertPairsErrorBody](binance/errors/list_all_convert_pairs_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def order_status_user_data(timestamp: int, signature: str, *, order_id: str | None = None, quote_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ConvertOrderStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query order status by order ID.

Weight(UID): 100

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.convert.order_status_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1ConvertOrderStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrderStatusUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.convert.order_status_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1ConvertOrderStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrderStatusUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>quote_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ConvertOrderStatusResponse](binance/models/sapi_v1_convert_order_status_response.py)</code> -- Order Status

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[OrderStatusUserDataErrorBody](binance/errors/order_status_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def place_limit_order_user_data(base_asset: str, quote_asset: str, limit_price: float, side: SideOrStr, timestamp: int, signature: str, *, base_amount: float | None = None, quote_amount: float | None = None, wallet_type: WalletTypeOrStr | None = None, expired_type: ExpiredTypeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ConvertLimitPlaceOrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enable users to place a limit order

- baseAsset or quoteAsset can be determined via exchangeInfo endpoint.
- Limit price is defined from baseAsset to quoteAsset.
- Either baseAmount or quoteAmount is used.

Weight(UID): 500

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.convert.place_limit_order_user_data(
        base_asset, quote_asset, limit_price, side, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ConvertLimitPlaceOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PlaceLimitOrderUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.convert.place_limit_order_user_data(
        base_asset, quote_asset, limit_price, side, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ConvertLimitPlaceOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PlaceLimitOrderUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>base_asset</code> | <code>str</code> | Value sent with the request. |
| <code>quote_asset</code> | <code>str</code> | Value sent with the request. |
| <code>limit_price</code> | <code>float</code> | Symbol limit price (from baseAsset to quoteAsset) |
| <code>side</code> | <code>[SideOrStr](binance/models/enums/side.py)</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>base_amount</code> | <code>float \| None</code> | Base asset amount. (One of baseAmount or quoteAmount is required)<br>**Default**: <code>None</code> |
| <code>quote_amount</code> | <code>float \| None</code> | Quote asset amount. (One of baseAmount or quoteAmount is required)<br>**Default**: <code>None</code> |
| <code>wallet_type</code> | <code>[WalletTypeOrStr](binance/models/enums/wallet_type.py) \| None</code> | SPOT or FUNDING or SPOT_FUNDING. It is to use which type of assets. Default is SPOT.<br>**Default**: <code>None</code> |
| <code>expired_type</code> | <code>[ExpiredTypeOrStr](binance/models/enums/expired_type.py) \| None</code> | 1_D, 3_D, 7_D, 30_D (D means day)<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ConvertLimitPlaceOrderResponse](binance/models/sapi_v1_convert_limit_place_order_response.py)</code>

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[PlaceLimitOrderUserDataErrorBody](binance/errors/place_limit_order_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_limit_open_orders_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ConvertLimitQueryOpenOrdersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enable users to query for all existing limit orders

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.convert.query_limit_open_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1ConvertLimitQueryOpenOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryLimitOpenOrdersUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.convert.query_limit_open_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1ConvertLimitQueryOpenOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryLimitOpenOrdersUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ConvertLimitQueryOpenOrdersResponse](binance/models/sapi_v1_convert_limit_query_open_orders_response.py)</code> -- All existing limit orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryLimitOpenOrdersUserDataErrorBody](binance/errors/query_limit_open_orders_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_order_quantity_precision_per_asset_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1ConvertAssetInfoResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query for supported asset precision information

Weight(IP): 100

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.convert.query_order_quantity_precision_per_asset_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1ConvertAssetInfoResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryOrderQuantityPrecisionPerAssetUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.convert.query_order_quantity_precision_per_asset_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1ConvertAssetInfoResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryOrderQuantityPrecisionPerAssetUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1ConvertAssetInfoResponse](binance/models/sapi_v1_convert_asset_info_response.py)&#93;</code> -- Asset Precision Information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryOrderQuantityPrecisionPerAssetUserDataErrorBody](binance/errors/query_order_quantity_precision_per_asset_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def send_quote_request_user_data(from_asset: str, to_asset: str, timestamp: int, signature: str, *, from_amount: float | None = None, to_amount: float | None = None, valid_time: str | None = None, wallet_type: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ConvertGetQuoteResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Request a quote for the requested token pairs

Weight(UID): 200

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.convert.send_quote_request_user_data(from_asset, to_asset, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1ConvertGetQuoteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SendQuoteRequestUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.convert.send_quote_request_user_data(from_asset, to_asset, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1ConvertGetQuoteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SendQuoteRequestUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>from_asset</code> | <code>str</code> | Value sent with the request. |
| <code>to_asset</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>from_amount</code> | <code>float \| None</code> | When specified, it is the amount you will be debited after the conversion<br>**Default**: <code>None</code> |
| <code>to_amount</code> | <code>float \| None</code> | When specified, it is the amount you will be debited after the conversion<br>**Default**: <code>None</code> |
| <code>valid_time</code> | <code>str \| None</code> | 10s, 30s, 1m, 2m, default 10s<br>**Default**: <code>None</code> |
| <code>wallet_type</code> | <code>str \| None</code> | SPOT or FUNDING. Default is SPOT<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ConvertGetQuoteResponse](binance/models/sapi_v1_convert_get_quote_response.py)</code> -- Quote Request

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SendQuoteRequestUserDataErrorBody](binance/errors/send_quote_request_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## CopyTrading

> Source: [CopyTrading](binance/apis/copy_trading.py)

<details>
<summary><code>def get_futures_lead_trader_status_trade(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1CopyTradingFuturesUserStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Futures Lead Trader Status

Weight(UID): 20

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.copy_trading.get_futures_lead_trader_status_trade(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1CopyTradingFuturesUserStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFuturesLeadTraderStatusTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.copy_trading.get_futures_lead_trader_status_trade(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1CopyTradingFuturesUserStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFuturesLeadTraderStatusTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1CopyTradingFuturesUserStatusResponse](binance/models/sapi_v1_copy_trading_futures_user_status_response.py)</code> -- Futures Lead Trader Status

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetFuturesLeadTraderStatusTradeErrorBody](binance/errors/get_futures_lead_trader_status_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_futures_lead_trading_symbol_whitelist_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1CopyTradingFuturesLeadSymbolResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Futures Lead Trading Symbol Whitelist

Weight(IP): 20

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.copy_trading.get_futures_lead_trading_symbol_whitelist_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1CopyTradingFuturesLeadSymbolResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFuturesLeadTradingSymbolWhitelistUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.copy_trading.get_futures_lead_trading_symbol_whitelist_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1CopyTradingFuturesLeadSymbolResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFuturesLeadTradingSymbolWhitelistUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1CopyTradingFuturesLeadSymbolResponse](binance/models/sapi_v1_copy_trading_futures_lead_symbol_response.py)</code> -- Futures Lead Trading Symbol Whitelist

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetFuturesLeadTradingSymbolWhitelistUserDataErrorBody](binance/errors/get_futures_lead_trading_symbol_whitelist_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## CryptoLoans

> Source: [CryptoLoans](binance/apis/crypto_loans.py)

<details>
<summary><code>def adjust_ltv_flexible_loan_adjust_ltv_trade(adjustment_amount: float, direction: DirectionOrStr, timestamp: int, signature: str, *, loan_coin: str | None = None, collateral_coin: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2LoanFlexibleAdjustLtvResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- API Key needs Spot & Margin Trading permission for this endpoint

Weight(UID): 6000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.adjust_ltv_flexible_loan_adjust_ltv_trade(
        adjustment_amount, direction, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV2LoanFlexibleAdjustLtvResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AdjustLtvFlexibleLoanAdjustLtvTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.adjust_ltv_flexible_loan_adjust_ltv_trade(
        adjustment_amount, direction, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV2LoanFlexibleAdjustLtvResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AdjustLtvFlexibleLoanAdjustLtvTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>adjustment_amount</code> | <code>float</code> | Value sent with the request. |
| <code>direction</code> | <code>[DirectionOrStr](binance/models/enums/direction.py)</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2LoanFlexibleAdjustLtvResponse](binance/models/sapi_v2_loan_flexible_adjust_ltv_response.py)</code> -- adjust LTV result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AdjustLtvFlexibleLoanAdjustLtvTradeErrorBody](binance/errors/adjust_ltv_flexible_loan_adjust_ltv_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data(timestamp: int, signature: str, *, loan_coin: str | None = None, collateral_coin: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2LoanFlexibleLtvAdjustmentHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If startTime and endTime are not sent, the recent 90-day data will be returned.
- The max interval between startTime and endTime is 180 days.

Weight(IP): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleLtvAdjustmentHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AdjustLtvGetFlexibleLoanLtvAdjustmentHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data(
        timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV2LoanFlexibleLtvAdjustmentHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AdjustLtvGetFlexibleLoanLtvAdjustmentHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2LoanFlexibleLtvAdjustmentHistoryResponse](binance/models/sapi_v2_loan_flexible_ltv_adjustment_history_response.py)</code> -- LTV adjustment history

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AdjustLtvGetFlexibleLoanLtvAdjustmentHistoryUserDataErrorBody](binance/errors/adjust_ltv_get_flexible_loan_ltv_adjustment_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def borrow_flexible_loan_borrow_trade(timestamp: int, signature: str, *, loan_coin: str | None = None, loan_amount: float | None = None, collateral_coin: str | None = None, collateral_amount: float | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2LoanFlexibleBorrowResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- Only available for master account

Weight(UID): 6000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.borrow_flexible_loan_borrow_trade(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleBorrowResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BorrowFlexibleLoanBorrowTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.borrow_flexible_loan_borrow_trade(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleBorrowResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BorrowFlexibleLoanBorrowTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>loan_amount</code> | <code>float \| None</code> | Loan amount<br>**Default**: <code>None</code> |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>collateral_amount</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2LoanFlexibleBorrowResponse](binance/models/sapi_v2_loan_flexible_borrow_response.py)</code> -- Collateral Assets Data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[BorrowFlexibleLoanBorrowTradeErrorBody](binance/errors/borrow_flexible_loan_borrow_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def borrow_get_flexible_loan_borrow_history_user_data(timestamp: int, signature: str, *, loan_coin: str | None = None, collateral_coin: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2LoanFlexibleBorrowHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If startTime and endTime are not sent, the recent 90-day data will be returned.
- The max interval between startTime and endTime is 180 days.

Weight(IP): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.borrow_get_flexible_loan_borrow_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleBorrowHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BorrowGetFlexibleLoanBorrowHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.borrow_get_flexible_loan_borrow_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleBorrowHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BorrowGetFlexibleLoanBorrowHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2LoanFlexibleBorrowHistoryResponse](binance/models/sapi_v2_loan_flexible_borrow_history_response.py)</code> -- Loan borrow histroy

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[BorrowGetFlexibleLoanBorrowHistoryUserDataErrorBody](binance/errors/borrow_get_flexible_loan_borrow_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def borrow_get_flexible_loan_ongoing_orders_user_data(timestamp: int, signature: str, *, loan_coin: str | None = None, collateral_coin: str | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2LoanFlexibleOngoingOrdersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 300

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.borrow_get_flexible_loan_ongoing_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleOngoingOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BorrowGetFlexibleLoanOngoingOrdersUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.borrow_get_flexible_loan_ongoing_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleOngoingOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BorrowGetFlexibleLoanOngoingOrdersUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2LoanFlexibleOngoingOrdersResponse](binance/models/sapi_v2_loan_flexible_ongoing_orders_response.py)</code> -- Collateral Assets Data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[BorrowGetFlexibleLoanOngoingOrdersUserDataErrorBody](binance/errors/borrow_get_flexible_loan_ongoing_orders_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def check_collateral_repay_rate_user_data(loan_coin: str, collateral_coin: str, repay_amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanRepayCollateralRateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the the rate of collateral coin / loan coin when using collateral repay, the rate will be valid within 8 second.

Weight(IP): 6000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.check_collateral_repay_rate_user_data(
        loan_coin, collateral_coin, repay_amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LoanRepayCollateralRateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckCollateralRepayRateUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.check_collateral_repay_rate_user_data(
        loan_coin, collateral_coin, repay_amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LoanRepayCollateralRateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckCollateralRepayRateUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>loan_coin</code> | <code>str</code> | Coin loaned |
| <code>collateral_coin</code> | <code>str</code> | Coin used as collateral |
| <code>repay_amount</code> | <code>float</code> | repay amount of loanCoin |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanRepayCollateralRateResponse](binance/models/sapi_v1_loan_repay_collateral_rate_response.py)</code> -- Collateral Assets Data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CheckCollateralRepayRateUserDataErrorBody](binance/errors/check_collateral_repay_rate_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def crypto_loan_adjust_ltv_trade(order_id: int, amount: float, direction: DirectionOrStr, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanAdjustLtvResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(UID): 6000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.crypto_loan_adjust_ltv_trade(order_id, amount, direction, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanAdjustLtvResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CryptoLoanAdjustLtvTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.crypto_loan_adjust_ltv_trade(
        order_id, amount, direction, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LoanAdjustLtvResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CryptoLoanAdjustLtvTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>int</code> | Order ID |
| <code>amount</code> | <code>float</code> | Amount |
| <code>direction</code> | <code>[DirectionOrStr](binance/models/enums/direction.py)</code> | 'ADDITIONAL', 'REDUCED' |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanAdjustLtvResponse](binance/models/sapi_v1_loan_adjust_ltv_response.py)</code> -- LTV Adjust

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CryptoLoanAdjustLtvTradeErrorBody](binance/errors/crypto_loan_adjust_ltv_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def crypto_loan_borrow_trade(loan_coin: str, collateral_coin: str, loan_term: int, timestamp: int, signature: str, *, loan_amount: float | None = None, collateral_amount: float | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanBorrowResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(UID): 6000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.crypto_loan_borrow_trade(loan_coin, collateral_coin, loan_term, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanBorrowResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CryptoLoanBorrowTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.crypto_loan_borrow_trade(
        loan_coin, collateral_coin, loan_term, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LoanBorrowResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CryptoLoanBorrowTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>loan_coin</code> | <code>str</code> | Coin loaned |
| <code>collateral_coin</code> | <code>str</code> | Coin used as collateral |
| <code>loan_term</code> | <code>int</code> | 7/14/30/90/180 days |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>loan_amount</code> | <code>float \| None</code> | Loan amount<br>**Default**: <code>None</code> |
| <code>collateral_amount</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanBorrowResponse](binance/models/sapi_v1_loan_borrow_response.py)</code> -- Borrow Information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CryptoLoanBorrowTradeErrorBody](binance/errors/crypto_loan_borrow_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def crypto_loan_customize_margin_call_trade(margin_call: float, timestamp: int, signature: str, *, order_id: int | None = None, collateral_coin: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanCustomizeMarginCallResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Customize margin call for ongoing orders only.

Weight(UID): 6000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.crypto_loan_customize_margin_call_trade(margin_call, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanCustomizeMarginCallResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CryptoLoanCustomizeMarginCallTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.crypto_loan_customize_margin_call_trade(
        margin_call, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LoanCustomizeMarginCallResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CryptoLoanCustomizeMarginCallTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>margin_call</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>int \| None</code> | Mandatory when collateralCoin is empty. Send either orderId or collateralCoin, if both parameters are sent, take orderId only.<br>**Default**: <code>None</code> |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanCustomizeMarginCallResponse](binance/models/sapi_v1_loan_customize_margin_call_response.py)</code> -- Collateral Assets Data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CryptoLoanCustomizeMarginCallTradeErrorBody](binance/errors/crypto_loan_customize_margin_call_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def crypto_loan_repay_trade(order_id: int, amount: float, timestamp: int, signature: str, *, type_: int | None = None, collateral_return: bool | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanRepayResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(UID): 6000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.crypto_loan_repay_trade(order_id, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanRepayResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CryptoLoanRepayTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.crypto_loan_repay_trade(order_id, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanRepayResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CryptoLoanRepayTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>int</code> | Order ID |
| <code>amount</code> | <code>float</code> | Repayment Amount |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>type_</code> | <code>int \| None</code> | Default: 1. 1 for 'repay with borrowed coin'; 2 for 'repay with collateral'.<br>**Default**: <code>None</code> |
| <code>collateral_return</code> | <code>bool \| None</code> | Default: TRUE. TRUE: Return extra collateral to spot account; FALSE: Keep extra collateral in the order.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanRepayResponse](binance/models/unions/sapi_v1_loan_repay_response.py)</code> -- Repayment Information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CryptoLoanRepayTradeErrorBody](binance/errors/crypto_loan_repay_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_collateral_assets_data_user_data(timestamp: int, signature: str, *, collateral_coin: str | None = None, vip_level: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanCollateralDataResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get LTV information and collateral limit of collateral assets. The collateral limit is shown in USD value.

Weight(IP): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.get_collateral_assets_data_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanCollateralDataResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCollateralAssetsDataUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.get_collateral_assets_data_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanCollateralDataResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCollateralAssetsDataUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>vip_level</code> | <code>int \| None</code> | Defaults to user's vip level<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanCollateralDataResponse](binance/models/sapi_v1_loan_collateral_data_response.py)</code> -- Collateral Assets Data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetCollateralAssetsDataUserDataErrorBody](binance/errors/get_collateral_assets_data_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_crypto_loans_borrow_history_user_data(timestamp: int, signature: str, *, order_id: int | None = None, loan_coin: str | None = None, collateral_coin: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanBorrowHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If startTime and endTime are not sent, the recent 90-day data will be returned.
- The max interval between startTime and endTime is 180 days.

Weight(IP): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.get_crypto_loans_borrow_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanBorrowHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCryptoLoansBorrowHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.get_crypto_loans_borrow_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanBorrowHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCryptoLoansBorrowHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>int \| None</code> | orderId in POST /sapi/v1/loan/borrow<br>**Default**: <code>None</code> |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | default 10, max 100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanBorrowHistoryResponse](binance/models/sapi_v1_loan_borrow_history_response.py)</code> -- Borrow History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetCryptoLoansBorrowHistoryUserDataErrorBody](binance/errors/get_crypto_loans_borrow_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_crypto_loans_income_history_user_data(timestamp: int, signature: str, *, asset: str | None = None, type_: Type9OrStr | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1LoanIncomeResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If startTime and endTime are not sent, the recent 7-day data will be returned.
- The max interval between startTime and endTime is 30 days.

Weight(UID): 6000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.get_crypto_loans_income_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1LoanIncomeResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCryptoLoansIncomeHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.get_crypto_loans_income_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1LoanIncomeResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCryptoLoansIncomeHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>type_</code> | <code>[Type9OrStr](binance/models/enums/type9.py) \| None</code> | All types will be returned by default.<br>  * `borrowIn`<br>  * `collateralSpent`<br>  * `repayAmount`<br>  * `collateralReturn` - Collateral return after repayment<br>  * `addCollateral`<br>  * `removeCollateral`<br>  * `collateralReturnAfterLiquidation`<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | default 20, max 100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1LoanIncomeResponse](binance/models/sapi_v1_loan_income_response.py)&#93;</code> -- Loan History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetCryptoLoansIncomeHistoryUserDataErrorBody](binance/errors/get_crypto_loans_income_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_flexible_loan_assets_data_user_data(timestamp: int, signature: str, *, loan_coin: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2LoanFlexibleLoanableDataResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get interest rate and borrow limit of flexible loanable assets. The borrow limit is shown in USD value.

Weight(IP): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.get_flexible_loan_assets_data_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleLoanableDataResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexibleLoanAssetsDataUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.get_flexible_loan_assets_data_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleLoanableDataResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexibleLoanAssetsDataUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2LoanFlexibleLoanableDataResponse](binance/models/sapi_v2_loan_flexible_loanable_data_response.py)</code> -- Loan asset data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetFlexibleLoanAssetsDataUserDataErrorBody](binance/errors/get_flexible_loan_assets_data_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_flexible_loan_collateral_assets_data_user_data(timestamp: int, signature: str, *, collateral_coin: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2LoanFlexibleCollateralDataResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get LTV information and collateral limit of flexible loan's collateral assets. The collateral limit is shown in USD value.

Weight(IP): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.get_flexible_loan_collateral_assets_data_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleCollateralDataResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexibleLoanCollateralAssetsDataUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.get_flexible_loan_collateral_assets_data_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleCollateralDataResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexibleLoanCollateralAssetsDataUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2LoanFlexibleCollateralDataResponse](binance/models/sapi_v2_loan_flexible_collateral_data_response.py)</code> -- Loan asset data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetFlexibleLoanCollateralAssetsDataUserDataErrorBody](binance/errors/get_flexible_loan_collateral_assets_data_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_loan_ltv_adjustment_history_user_data(timestamp: int, signature: str, *, order_id: int | None = None, loan_coin: str | None = None, collateral_coin: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanLtvAdjustmentHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

If startTime and endTime are not sent, the recent 90-day data will be returned.
The max interval between startTime and endTime is 180 days.

Weight(IP): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.get_loan_ltv_adjustment_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanLtvAdjustmentHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLoanLtvAdjustmentHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.get_loan_ltv_adjustment_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanLtvAdjustmentHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLoanLtvAdjustmentHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>int \| None</code> | Order ID<br>**Default**: <code>None</code> |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | default 10, max 100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanLtvAdjustmentHistoryResponse](binance/models/sapi_v1_loan_ltv_adjustment_history_response.py)</code> -- LTV Adjustment History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetLoanLtvAdjustmentHistoryUserDataErrorBody](binance/errors/get_loan_ltv_adjustment_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_loan_ongoing_orders_user_data(timestamp: int, signature: str, *, order_id: int | None = None, loan_coin: str | None = None, collateral_coin: str | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanOngoingOrdersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 300

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.get_loan_ongoing_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanOngoingOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLoanOngoingOrdersUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.get_loan_ongoing_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanOngoingOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLoanOngoingOrdersUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>int \| None</code> | orderId in POST /sapi/v1/loan/borrow<br>**Default**: <code>None</code> |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1; default:1, max:1000<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | default 10, max 100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanOngoingOrdersResponse](binance/models/sapi_v1_loan_ongoing_orders_response.py)</code> -- Ongoing Orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetLoanOngoingOrdersUserDataErrorBody](binance/errors/get_loan_ongoing_orders_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_loan_repayment_history_user_data(timestamp: int, signature: str, *, order_id: int | None = None, loan_coin: str | None = None, collateral_coin: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanRepayHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

If startTime and endTime are not sent, the recent 90-day data will be returned.
The max interval between startTime and endTime is 180 days.

Weight(IP): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.get_loan_repayment_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanRepayHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLoanRepaymentHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.get_loan_repayment_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanRepayHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLoanRepaymentHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>int \| None</code> | Order ID<br>**Default**: <code>None</code> |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | default 10, max 100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanRepayHistoryResponse](binance/models/sapi_v1_loan_repay_history_response.py)</code> -- Loan Repayment History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetLoanRepaymentHistoryUserDataErrorBody](binance/errors/get_loan_repayment_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_loanable_assets_data_user_data(timestamp: int, signature: str, *, loan_coin: str | None = None, vip_level: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanLoanableDataResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get interest rate and borrow limit of loanable assets. The borrow limit is shown in USD value.

Weight(IP): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.get_loanable_assets_data_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanLoanableDataResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLoanableAssetsDataUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.get_loanable_assets_data_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanLoanableDataResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLoanableAssetsDataUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>vip_level</code> | <code>int \| None</code> | Defaults to user's vip level<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanLoanableDataResponse](binance/models/sapi_v1_loan_loanable_data_response.py)</code> -- Loanable Assets Data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetLoanableAssetsDataUserDataErrorBody](binance/errors/get_loanable_assets_data_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def repay_flexible_loan_repay_trade(repay_amount: float, timestamp: int, signature: str, *, loan_coin: str | None = None, collateral_coin: str | None = None, collateral_return: bool | None = None, full_repayment: bool | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2LoanFlexibleRepayResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- repayAmount is mandatory even fullRepayment = FALSE

Weight(IP): 6000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.repay_flexible_loan_repay_trade(repay_amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleRepayResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RepayFlexibleLoanRepayTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.repay_flexible_loan_repay_trade(repay_amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleRepayResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RepayFlexibleLoanRepayTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>repay_amount</code> | <code>float</code> | repay amount of loanCoin |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>collateral_return</code> | <code>bool \| None</code> | Default: TRUE.<br>TRUE: Return extra collateral to earn account;<br>FALSE: Keep extra collateral in the order, and lower LTV.<br>**Default**: <code>None</code> |
| <code>full_repayment</code> | <code>bool \| None</code> | Default: FALSE.<br>TRUE: Full repayment;<br>FALSE: Partial repayment, based on loanAmount<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2LoanFlexibleRepayResponse](binance/models/sapi_v2_loan_flexible_repay_response.py)</code> -- Loan repay

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RepayFlexibleLoanRepayTradeErrorBody](binance/errors/repay_flexible_loan_repay_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def repay_get_flexible_loan_repayment_history_user_data(timestamp: int, signature: str, *, loan_coin: str | None = None, collateral_coin: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2LoanFlexibleRepayHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If startTime and endTime are not sent, the recent 90-day data will be returned.
- The max interval between startTime and endTime is 180 days.

Weight(IP): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_loans.repay_get_flexible_loan_repayment_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleRepayHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RepayGetFlexibleLoanRepaymentHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.crypto_loans.repay_get_flexible_loan_repayment_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2LoanFlexibleRepayHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RepayGetFlexibleLoanRepaymentHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2LoanFlexibleRepayHistoryResponse](binance/models/sapi_v2_loan_flexible_repay_history_response.py)</code> -- Loan repay history

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RepayGetFlexibleLoanRepaymentHistoryUserDataErrorBody](binance/errors/repay_get_flexible_loan_repayment_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## DualInvestment

> Source: [DualInvestment](binance/apis/dual_investment.py)

<details>
<summary><code>def change_auto_compound_status_user_data(position_id: int, auto_compound_plan: AutoCompoundPlanOrStr, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1DciProductAutoCompoundEditStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Change Auto-Compound status

- 15:31 ~ 16:00 UTC+8 This function is disabled

Weight(IP): 1

Rate Limit: Maximum 1 time/s per account

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.dual_investment.change_auto_compound_status_user_data(
        position_id, auto_compound_plan, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1DciProductAutoCompoundEditStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangeAutoCompoundStatusUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.dual_investment.change_auto_compound_status_user_data(
        position_id, auto_compound_plan, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1DciProductAutoCompoundEditStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangeAutoCompoundStatusUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>position_id</code> | <code>int</code> | Get positionId from /sapi/v1/dci/product/positions |
| <code>auto_compound_plan</code> | <code>[AutoCompoundPlanOrStr](binance/models/enums/auto_compound_plan.py)</code> | NONE: switch off the plan,<br>STANDARD: standard plan,<br>ADVANCED: advanced plan; |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1DciProductAutoCompoundEditStatusResponse](binance/models/sapi_v1_dci_product_auto_compound_edit_status_response.py)</code> -- Change Auto-Compound status response

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[ChangeAutoCompoundStatusUserDataErrorBody](binance/errors/change_auto_compound_status_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def check_dual_investment_accounts_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1DciProductAccountsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check Dual Investment accounts

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.dual_investment.check_dual_investment_accounts_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1DciProductAccountsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckDualInvestmentAccountsUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.dual_investment.check_dual_investment_accounts_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1DciProductAccountsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckDualInvestmentAccountsUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1DciProductAccountsResponse](binance/models/sapi_v1_dci_product_accounts_response.py)</code> -- Dual Investment accounts

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CheckDualInvestmentAccountsUserDataErrorBody](binance/errors/check_dual_investment_accounts_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_dual_investment_positions_user_data(timestamp: int, signature: str, *, status: Status2OrStr | None = None, page_size: str | None = None, page_index: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1DciProductPositionsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Dual Investment positions (batch)

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.dual_investment.get_dual_investment_positions_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1DciProductPositionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDualInvestmentPositionsUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.dual_investment.get_dual_investment_positions_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1DciProductPositionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDualInvestmentPositionsUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>status</code> | <code>[Status2OrStr](binance/models/enums/status2.py) \| None</code> | - PENDING: Products are purchasing, will give results later;<br>- PURCHASE_SUCCESS: purchase successfully;<br>- SETTLED: Products are finish settling;<br>- PURCHASE_FAIL: fail to purchase;<br>- REFUNDING: refund ongoing;<br>- REFUND_SUCCESS: refund to spot account successfully;<br>- SETTLING: Products are settling.<br>If don't fill this field, will response all the position status.<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>str \| None</code> | MIN 1, MAX 100; Default 100<br>**Default**: <code>None</code> |
| <code>page_index</code> | <code>int \| None</code> | Page number, default is first page, start form 1<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1DciProductPositionsResponse](binance/models/sapi_v1_dci_product_positions_response.py)</code> -- Dual Investment product list

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetDualInvestmentPositionsUserDataErrorBody](binance/errors/get_dual_investment_positions_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_dual_investment_product_list_user_data(option_type: OptionTypeOrStr, exercised_coin: str, invest_coin: str, timestamp: int, signature: str, *, page_size: str | None = None, page_index: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1DciProductListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Dual Investment product list

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.dual_investment.get_dual_investment_product_list_user_data(
        option_type, exercised_coin, invest_coin, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1DciProductListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDualInvestmentProductListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.dual_investment.get_dual_investment_product_list_user_data(
        option_type, exercised_coin, invest_coin, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1DciProductListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDualInvestmentProductListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>option_type</code> | <code>[OptionTypeOrStr](binance/models/enums/option_type.py)</code> | Input CALL or PUT |
| <code>exercised_coin</code> | <code>str</code> | Target exercised asset, e.g.:<br>if you subscribe to a high sell product (call option), you should input:<br>  - optionType: CALL,<br>  - exercisedCoin: USDT,<br>  - investCoin: BNB;<br><br>if you subscribe to a low buy product (put option), you should input:<br>  - optionType: PUT,<br>  - exercisedCoin: BNB,<br>  - investCoin: USDT; |
| <code>invest_coin</code> | <code>str</code> | Asset used for subscribing, e.g.:<br>if you subscribe to a high sell product (call option), you should input:<br>  - optionType: CALL,<br>  - exercisedCoin: USDT,<br>  - investCoin: BNB;<br><br>if you subscribe to a low buy product (put option), you should input:<br>  - optionType: PUT,<br>  - exercisedCoin: BNB,<br>  - investCoin: USDT; |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>page_size</code> | <code>str \| None</code> | MIN 1, MAX 100; Default 100<br>**Default**: <code>None</code> |
| <code>page_index</code> | <code>int \| None</code> | Page number, default is first page, start form 1<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1DciProductListResponse](binance/models/sapi_v1_dci_product_list_response.py)</code> -- Dual Investment product list

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetDualInvestmentProductListUserDataErrorBody](binance/errors/get_dual_investment_product_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def subscribe_dual_investment_products_user_data(id: str, order_id: str, deposit_amount: float, auto_compound_plan: AutoCompoundPlanOrStr, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1DciProductSubscribeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Subscribe Dual Investment products

- `Products are not available.` means that the APR changes to lower value, or the orders are not available.
- `Failed` is a system or network errors.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.dual_investment.subscribe_dual_investment_products_user_data(
        id, order_id, deposit_amount, auto_compound_plan, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1DciProductSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubscribeDualInvestmentProductsUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.dual_investment.subscribe_dual_investment_products_user_data(
        id, order_id, deposit_amount, auto_compound_plan, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1DciProductSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubscribeDualInvestmentProductsUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | get id from /sapi/v1/dci/product/list |
| <code>order_id</code> | <code>str</code> | get orderId from /sapi/v1/dci/product/list |
| <code>deposit_amount</code> | <code>float</code> | Value sent with the request. |
| <code>auto_compound_plan</code> | <code>[AutoCompoundPlanOrStr](binance/models/enums/auto_compound_plan.py)</code> | NONE: switch off the plan,<br>STANDARD: standard plan,<br>ADVANCED: advanced plan; |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1DciProductSubscribeResponse](binance/models/sapi_v1_dci_product_subscribe_response.py)</code> -- Dual Investment product subscription response

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SubscribeDualInvestmentProductsUserDataErrorBody](binance/errors/subscribe_dual_investment_products_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Fiat

> Source: [Fiat](binance/apis/fiat.py)

<details>
<summary><code>def fiat_deposit_withdraw_history_user_data(transaction_type: int, timestamp: int, signature: str, *, begin_time: int | None = None, end_time: int | None = None, page: int | None = None, rows: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1FiatOrdersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If beginTime and endTime are not sent, the recent 30-day data will be returned.

Weight(UID): 90000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.fiat.fiat_deposit_withdraw_history_user_data(transaction_type, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1FiatOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FiatDepositWithdrawHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.fiat.fiat_deposit_withdraw_history_user_data(transaction_type, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1FiatOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FiatDepositWithdrawHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>transaction_type</code> | <code>int</code> | * `0` - deposit<br>* `1` - withdraw |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>begin_time</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>rows</code> | <code>int \| None</code> | Default 100, max 500<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1FiatOrdersResponse](binance/models/sapi_v1_fiat_orders_response.py)</code> -- History of deposit/withdraw orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[FiatDepositWithdrawHistoryUserDataErrorBody](binance/errors/fiat_deposit_withdraw_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fiat_payments_history_user_data(transaction_type: int, timestamp: int, signature: str, *, begin_time: int | None = None, end_time: int | None = None, page: int | None = None, rows: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1FiatPaymentsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If beginTime and endTime are not sent, the recent 30-day data will be returned.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.fiat.fiat_payments_history_user_data(transaction_type, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1FiatPaymentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FiatPaymentsHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.fiat.fiat_payments_history_user_data(transaction_type, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1FiatPaymentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FiatPaymentsHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>transaction_type</code> | <code>int</code> | * `0` - deposit<br>* `1` - withdraw |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>begin_time</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>rows</code> | <code>int \| None</code> | Default 100, max 500<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1FiatPaymentsResponse](binance/models/sapi_v1_fiat_payments_response.py)</code> -- History of fiat payments

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[FiatPaymentsHistoryUserDataErrorBody](binance/errors/fiat_payments_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Futures

> Source: [Futures](binance/apis/futures.py)

<details>
<summary><code>def get_future_account_transaction_history_list_user_data(asset: str, start_time: int, timestamp: int, signature: str, *, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1FuturesTransferResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.futures.get_future_account_transaction_history_list_user_data(
        asset, start_time, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1FuturesTransferResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFutureAccountTransactionHistoryListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.futures.get_future_account_transaction_history_list_user_data(
        asset, start_time, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1FuturesTransferResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFutureAccountTransactionHistoryListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>start_time</code> | <code>int</code> | UTC timestamp in ms |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1FuturesTransferResponse1](binance/models/sapi_v1_futures_transfer_response1.py)</code> -- Futures Transfer Query

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetFutureAccountTransactionHistoryListUserDataErrorBody](binance/errors/get_future_account_transaction_history_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_future_tick_level_orderbook_historical_data_download_link_user_data(symbol: str, data_type: DataTypeOrStr, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1FuturesHistDataLinkResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.futures.get_future_tick_level_orderbook_historical_data_download_link_user_data(
        symbol, data_type, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1FuturesHistDataLinkResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFutureTickLevelOrderbookHistoricalDataDownloadLinkUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.futures.get_future_tick_level_orderbook_historical_data_download_link_user_data(
        symbol, data_type, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1FuturesHistDataLinkResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFutureTickLevelOrderbookHistoricalDataDownloadLinkUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Value sent with the request. |
| <code>data_type</code> | <code>[DataTypeOrStr](binance/models/enums/data_type.py)</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1FuturesHistDataLinkResponse](binance/models/sapi_v1_futures_hist_data_link_response.py)</code> -- data link

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetFutureTickLevelOrderbookHistoricalDataDownloadLinkUserDataErrorBody](binance/errors/get_future_tick_level_orderbook_historical_data_download_link_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def new_future_account_transfer_user_data(asset: str, amount: float, type_: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1FuturesTransferResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Execute transfer between spot account and futures account.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.futures.new_future_account_transfer_user_data(asset, amount, type_, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1FuturesTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type NewFutureAccountTransferUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.futures.new_future_account_transfer_user_data(
        asset, amount, type_, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1FuturesTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type NewFutureAccountTransferUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>type_</code> | <code>int</code> | 1: transfer from spot account to USDT-Ⓜ futures account. 2: transfer from USDT-Ⓜ futures account to spot account. 3: transfer from spot account to COIN-Ⓜ futures account. 4: transfer from COIN-Ⓜ futures account to spot account. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1FuturesTransferResponse](binance/models/sapi_v1_futures_transfer_response.py)</code> -- Futures Transfer

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[NewFutureAccountTransferUserDataErrorBody](binance/errors/new_future_account_transfer_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## FuturesAlgo

> Source: [FuturesAlgo](binance/apis/futures_algo.py)

<details>
<summary><code>def cancel_algo_order_trade(algo_id: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AlgoFuturesOrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancel an active order.
- You need to enable Futures Trading Permission for the api key which requests this endpoint.
- Base URL: https://api.binance.com

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.futures_algo.cancel_algo_order_trade(algo_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoFuturesOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelAlgoOrderTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.futures_algo.cancel_algo_order_trade(algo_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoFuturesOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelAlgoOrderTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>algo_id</code> | <code>int</code> | Eg. 14511 |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AlgoFuturesOrderResponse](binance/models/sapi_v1_algo_futures_order_response.py)</code> -- Cancelled order

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CancelAlgoOrderTradeErrorBody](binance/errors/cancel_algo_order_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_current_algo_open_orders_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AlgoFuturesOpenOrdersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- You need to enable Futures Trading Permission for the api key which requests this endpoint.
- Base URL: https://api.binance.com

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.futures_algo.query_current_algo_open_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoFuturesOpenOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryCurrentAlgoOpenOrdersUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.futures_algo.query_current_algo_open_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoFuturesOpenOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryCurrentAlgoOpenOrdersUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AlgoFuturesOpenOrdersResponse](binance/models/sapi_v1_algo_futures_open_orders_response.py)</code> -- Open Algo Orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryCurrentAlgoOpenOrdersUserDataErrorBody](binance/errors/query_current_algo_open_orders_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_historical_algo_orders_user_data(timestamp: int, signature: str, *, symbol: str | None = None, side: SideOrStr | None = None, start_time: int | None = None, end_time: int | None = None, page: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AlgoFuturesHistoricalOrdersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- You need to enable Futures Trading Permission for the api key which requests this endpoint.
- Base URL: https://api.binance.com

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.futures_algo.query_historical_algo_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoFuturesHistoricalOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryHistoricalAlgoOrdersUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.futures_algo.query_historical_algo_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoFuturesHistoricalOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryHistoricalAlgoOrdersUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>symbol</code> | <code>str \| None</code> | Trading symbol, e.g. BNBUSDT<br>**Default**: <code>None</code> |
| <code>side</code> | <code>[SideOrStr](binance/models/enums/side.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>str \| None</code> | MIN 1, MAX 100; Default 100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AlgoFuturesHistoricalOrdersResponse](binance/models/sapi_v1_algo_futures_historical_orders_response.py)</code> -- Historical Algo Orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryHistoricalAlgoOrdersUserDataErrorBody](binance/errors/query_historical_algo_orders_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_sub_orders_user_data(algo_id: int, timestamp: int, signature: str, *, page: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AlgoFuturesSubOrdersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- You need to enable Futures Trading Permission for the api key which requests this endpoint.
- Base URL: https://api.binance.com

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.futures_algo.query_sub_orders_user_data(algo_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoFuturesSubOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySubOrdersUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.futures_algo.query_sub_orders_user_data(algo_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoFuturesSubOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySubOrdersUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>algo_id</code> | <code>int</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>str \| None</code> | MIN 1, MAX 100; Default 100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AlgoFuturesSubOrdersResponse](binance/models/sapi_v1_algo_futures_sub_orders_response.py)</code> -- Sub orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QuerySubOrdersUserDataErrorBody](binance/errors/query_sub_orders_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def time_weighted_average_price_twap_new_order_trade(symbol: str, side: SideOrStr, quantity: float, duration: int, timestamp: int, signature: str, *, position_side: PositionSideOrStr | None = None, client_algo_id: str | None = None, reduce_only: bool | None = None, limit_price: float | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AlgoFuturesNewOrderTwapResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send in a Twap new order. Only support on USDⓈ-M Contracts.

You need to enable Futures Trading Permission for the api key which requests this endpoint.
Base URL: https://api.binance.com

- Total Algo open orders max allowed: 10 orders.
- Leverage of symbols and position mode will be the same as your futures account settings. You can set up through the trading page or fapi.
- Receiving "success": true does not mean that your order will be executed. Please use the query order endpoints(GET sapi/v1/algo/futures/openOrders or GET sapi/v1/algo/futures/historicalOrders) to check the order status. For example: Your futures balance is insufficient, or open position with reduce only or position side is inconsistent with your own setting. In these cases you will receive "success": true, but the order status will be expired after we check it.
- quantity * 60 / duration should be larger than minQty
- duration cannot be less than 5 mins or more than 24 hours.
- For delivery contracts, TWAP end time should be one hour earlier than the delivery time of the symbol.

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.futures_algo.time_weighted_average_price_twap_new_order_trade(
        symbol, side, quantity, duration, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1AlgoFuturesNewOrderTwapResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TimeWeightedAveragePriceTwapNewOrderTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.futures_algo.time_weighted_average_price_twap_new_order_trade(
        symbol, side, quantity, duration, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1AlgoFuturesNewOrderTwapResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TimeWeightedAveragePriceTwapNewOrderTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>side</code> | <code>[SideOrStr](binance/models/enums/side.py)</code> | Value sent with the request. |
| <code>quantity</code> | <code>float</code> | Quantity of base asset; The notional (quantity * mark price(base asset)) must be more than the equivalent of 10,000 USDT and less than the equivalent of 1,000,000 USDT |
| <code>duration</code> | <code>int</code> | Duration for TWAP orders in seconds. [300, 86400];Less than 5min => defaults to 5 min; Greater than 24h => defaults to 24h |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>position_side</code> | <code>[PositionSideOrStr](binance/models/enums/position_side.py) \| None</code> | Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.<br>**Default**: <code>None</code> |
| <code>client_algo_id</code> | <code>str \| None</code> | A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give default value<br>**Default**: <code>None</code> |
| <code>reduce_only</code> | <code>bool \| None</code> | 'true' or 'false'. Default 'false'; Cannot be sent in Hedge Mode; Cannot be sent when you open a position<br>**Default**: <code>None</code> |
| <code>limit_price</code> | <code>float \| None</code> | Limit price of the order; If it is not sent, will place order by market price by default<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AlgoFuturesNewOrderTwapResponse](binance/models/sapi_v1_algo_futures_new_order_twap_response.py)</code> -- Time-Weighted Average Price(Twap) New Order

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[TimeWeightedAveragePriceTwapNewOrderTradeErrorBody](binance/errors/time_weighted_average_price_twap_new_order_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def volume_participation_vp_new_order_trade(symbol: str, side: SideOrStr, quantity: float, urgency: UrgencyOrStr, timestamp: int, signature: str, *, position_side: PositionSideOrStr | None = None, client_algo_id: str | None = None, reduce_only: bool | None = None, limit_price: float | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AlgoFuturesNewOrderVpResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send in a VP new order. Only support on USDⓈ-M Contracts.

- You need to enable `Futures Trading Permission` for the api key which requests this endpoint.
- Base URL: https://api.binance.com

- Total Algo open orders max allowed: 10 orders.
- Leverage of symbols and position mode will be the same as your futures account settings. You can set up through the trading page or fapi.
- Receiving "success": true does not mean that your order will be executed. Please use the query order endpoints(GET sapi/v1/algo/futures/openOrders or GET sapi/v1/algo/futures/historicalOrders) to check the order status. For example: Your futures balance is insufficient, or open position with reduce only or position side is inconsistent with your own setting. In these cases you will receive "success": true, but the order status will be expired after we check it.

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.futures_algo.volume_participation_vp_new_order_trade(
        symbol, side, quantity, urgency, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1AlgoFuturesNewOrderVpResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VolumeParticipationVpNewOrderTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.futures_algo.volume_participation_vp_new_order_trade(
        symbol, side, quantity, urgency, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1AlgoFuturesNewOrderVpResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VolumeParticipationVpNewOrderTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>side</code> | <code>[SideOrStr](binance/models/enums/side.py)</code> | Value sent with the request. |
| <code>quantity</code> | <code>float</code> | Quantity of base asset; The notional (quantity * mark price(base asset)) must be more than the equivalent of 10,000 USDT and less than the equivalent of 1,000,000 USDT |
| <code>urgency</code> | <code>[UrgencyOrStr](binance/models/enums/urgency.py)</code> | Represent the relative speed of the current execution; ENUM: LOW, MEDIUM, HIGH |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>position_side</code> | <code>[PositionSideOrStr](binance/models/enums/position_side.py) \| None</code> | Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.<br>**Default**: <code>None</code> |
| <code>client_algo_id</code> | <code>str \| None</code> | A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give default value<br>**Default**: <code>None</code> |
| <code>reduce_only</code> | <code>bool \| None</code> | 'true' or 'false'. Default 'false'; Cannot be sent in Hedge Mode; Cannot be sent when you open a position<br>**Default**: <code>None</code> |
| <code>limit_price</code> | <code>float \| None</code> | Limit price of the order; If it is not sent, will place order by market price by default<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AlgoFuturesNewOrderVpResponse](binance/models/sapi_v1_algo_futures_new_order_vp_response.py)</code> -- Volume Participation(VP) Order

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[VolumeParticipationVpNewOrderTradeErrorBody](binance/errors/volume_participation_vp_new_order_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## GiftCard

> Source: [GiftCard](binance/apis/gift_card.py)

<details>
<summary><code>def buy_a_binance_code_trade(base_token: str, face_token: str, base_token_amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1GiftcardBuyCodeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API is for buying a fixed-value Binance Code, which means your Binance Code will be redeemable to a token that is different to the token that you are paying in. If the token you’re paying and the redeemable token are the same, please use the Create Binance Code endpoint.
You can use supported crypto currency or fiat token as baseToken to buy Binance Code that is redeemable to your chosen faceToken.
Once successfully purchased, the amount of baseToken would be deducted from your funding wallet.

To get started with, please make sure:
- You have a Binance account
- You have passed kyc
- You have a sufficient balance in your Binance funding wallet
- You need Enable Withdrawals for the API Key which requests this endpoint.

Daily creation volume: 2 BTC / 24H Daily creation times: 200 Codes / 24H

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.gift_card.buy_a_binance_code_trade(
        base_token, face_token, base_token_amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1GiftcardBuyCodeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BuyABinanceCodeTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.gift_card.buy_a_binance_code_trade(
        base_token, face_token, base_token_amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1GiftcardBuyCodeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BuyABinanceCodeTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>base_token</code> | <code>str</code> | The token you want to pay, example BUSD |
| <code>face_token</code> | <code>str</code> | The token you want to buy, example BNB. If faceToken = baseToken, it's the same as createCode endpoint. |
| <code>base_token_amount</code> | <code>float</code> | The base token asset quantity, example  1.002 |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1GiftcardBuyCodeResponse](binance/models/sapi_v1_giftcard_buy_code_response.py)</code> -- Code creation

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[BuyABinanceCodeTradeErrorBody](binance/errors/buy_a_binance_code_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_a_binance_code_user_data(token: str, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1GiftcardCreateCodeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API is for creating a Binance Code. To get started with, please make sure:

- You have a Binance account
- You have passed kyc
- You have a sufficient balance in your Binance funding wallet
- You need Enable Withdrawals for the API Key which requests this endpoint.

Daily creation volume: 2 BTC / 24H Daily creation times: 200 Codes / 24H

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.gift_card.create_a_binance_code_user_data(token, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1GiftcardCreateCodeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateABinanceCodeUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.gift_card.create_a_binance_code_user_data(token, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1GiftcardCreateCodeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateABinanceCodeUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | The coin type contained in the Binance Code |
| <code>amount</code> | <code>float</code> | The amount of the coin |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1GiftcardCreateCodeResponse](binance/models/sapi_v1_giftcard_create_code_response.py)</code> -- Code creation

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CreateABinanceCodeUserDataErrorBody](binance/errors/create_a_binance_code_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fetch_rsa_public_key_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1GiftcardCryptographyRsaPublicKeyResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API is for fetching the RSA Public Key.
This RSA Public key will be used to encrypt the card code.
Please note that the RSA Public key fetched is valid only for the current day.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.gift_card.fetch_rsa_public_key_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1GiftcardCryptographyRsaPublicKeyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FetchRsaPublicKeyUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.gift_card.fetch_rsa_public_key_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1GiftcardCryptographyRsaPublicKeyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FetchRsaPublicKeyUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1GiftcardCryptographyRsaPublicKeyResponse](binance/models/sapi_v1_giftcard_cryptography_rsa_public_key_response.py)</code> -- RSA Public Key.

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[FetchRsaPublicKeyUserDataErrorBody](binance/errors/fetch_rsa_public_key_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fetch_token_limit_user_data(base_token: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1GiftcardBuyCodeTokenLimitResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API is to help you verify which tokens are available for you to purchase fixed-value gift cards as mentioned in section 2 and it's limitation.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.gift_card.fetch_token_limit_user_data(base_token, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1GiftcardBuyCodeTokenLimitResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FetchTokenLimitUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.gift_card.fetch_token_limit_user_data(base_token, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1GiftcardBuyCodeTokenLimitResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FetchTokenLimitUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>base_token</code> | <code>str</code> | The token you want to pay, example BUSD |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1GiftcardBuyCodeTokenLimitResponse](binance/models/sapi_v1_giftcard_buy_code_token_limit_response.py)</code> -- Token limit

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[FetchTokenLimitUserDataErrorBody](binance/errors/fetch_token_limit_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def redeem_a_binance_code_user_data(code: str, timestamp: int, signature: str, *, external_uid: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1GiftcardRedeemCodeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API is for redeeming the Binance Code. Once redeemed, the coins will be deposited in your funding wallet.

Please note that if you enter the wrong code 5 times within 24 hours, you will no longer be able to redeem any Binance Code that day.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.gift_card.redeem_a_binance_code_user_data(code, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1GiftcardRedeemCodeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RedeemABinanceCodeUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.gift_card.redeem_a_binance_code_user_data(code, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1GiftcardRedeemCodeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RedeemABinanceCodeUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>code</code> | <code>str</code> | Binance Code |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>external_uid</code> | <code>str \| None</code> | Each external unique ID represents a unique user on the partner platform. The function helps you to identify the redemption behavior of different users, such as redemption frequency and amount. It also helps risk and limit control of a single account, such as daily limit on redemption volume, frequency, and incorrect number of entries. This will also prevent a single user account reach the partner's daily redemption limits. We strongly recommend you to use this feature and transfer us the User ID of your users if you have different users redeeming Binance codes on your platform. To protect user data privacy, you may choose to transfer the user id in any desired format (max. 400 characters).<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1GiftcardRedeemCodeResponse](binance/models/sapi_v1_giftcard_redeem_code_response.py)</code> -- Redeemed Information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RedeemABinanceCodeUserDataErrorBody](binance/errors/redeem_a_binance_code_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def verify_a_binance_code_user_data(reference_no: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1GiftcardVerifyResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API is for verifying whether the Binance Code is valid or not by entering Binance Code or reference number.

Please note that if you enter the wrong binance code 5 times within an hour, you will no longer be able to verify any binance code for that hour.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.gift_card.verify_a_binance_code_user_data(reference_no, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1GiftcardVerifyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VerifyABinanceCodeUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.gift_card.verify_a_binance_code_user_data(reference_no, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1GiftcardVerifyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VerifyABinanceCodeUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>reference_no</code> | <code>str</code> | reference number |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1GiftcardVerifyResponse](binance/models/sapi_v1_giftcard_verify_response.py)</code> -- Code Verification

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[VerifyABinanceCodeUserDataErrorBody](binance/errors/verify_a_binance_code_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## IsolatedMarginStream

> Source: [IsolatedMarginStream](binance/apis/isolated_margin_stream.py)

<details>
<summary><code>def close_a_listen_key_user_stream_3(*, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Close out a user data stream.

Weight: 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.isolated_margin_stream.close_a_listen_key_user_stream_3()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CloseAListenKeyUserStream3ErrorBody
```

**Async**

```python
try:
    response = await async_client.isolated_margin_stream.close_a_listen_key_user_stream_3()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CloseAListenKeyUserStream3ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>listen_key</code> | <code>str \| None</code> | User websocket listen key<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CloseAListenKeyUserStream3ErrorBody](binance/errors/close_a_listen_key_user_stream3_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_a_listen_key_user_stream(*, request_options: RequestOptionsOrDict | None = None) -> SapiV1UserDataStreamIsolatedResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Start a new user data stream.
The stream will close after 60 minutes unless a keepalive is sent. If the account has an active `listenKey`, that `listenKey` will be returned and its validity will be extended for 60 minutes.

Weight: 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.isolated_margin_stream.generate_a_listen_key_user_stream()
    # TODO: Handle 'response' of type SapiV1UserDataStreamIsolatedResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.isolated_margin_stream.generate_a_listen_key_user_stream()
    # TODO: Handle 'response' of type SapiV1UserDataStreamIsolatedResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1UserDataStreamIsolatedResponse](binance/models/sapi_v1_user_data_stream_isolated_response.py)</code> -- Isolated margin listen key

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RawError](binance/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def ping_keep_alive_a_listen_key_user_stream(*, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 30 minutes.

Weight: 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.isolated_margin_stream.ping_keep_alive_a_listen_key_user_stream()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PingKeepAliveAListenKeyUserStreamErrorBody
```

**Async**

```python
try:
    response = await async_client.isolated_margin_stream.ping_keep_alive_a_listen_key_user_stream()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PingKeepAliveAListenKeyUserStreamErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>listen_key</code> | <code>str \| None</code> | User websocket listen key<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[PingKeepAliveAListenKeyUserStreamErrorBody](binance/errors/ping_keep_alive_a_listen_key_user_stream_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Margin

> Source: [Margin](binance/apis/margin.py)

<details>
<summary><code>def adjust_cross_margin_max_leverage_user_data(max_leverage: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginMaxLeverageResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adjust cross margin max leverage

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.adjust_cross_margin_max_leverage_user_data(max_leverage, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginMaxLeverageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AdjustCrossMarginMaxLeverageUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.adjust_cross_margin_max_leverage_user_data(max_leverage, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginMaxLeverageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AdjustCrossMarginMaxLeverageUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>max_leverage</code> | <code>int</code> | Can only adjust 3 or 5 |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginMaxLeverageResponse](binance/models/sapi_v1_margin_max_leverage_response.py)</code> -- Adjust result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AdjustCrossMarginMaxLeverageUserDataErrorBody](binance/errors/adjust_cross_margin_max_leverage_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cross_margin_collateral_ratio_market_data(*, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginCrossMarginCollateralRatioResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 100

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.cross_margin_collateral_ratio_market_data()
    # TODO: Handle 'response' of type list[SapiV1MarginCrossMarginCollateralRatioResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CrossMarginCollateralRatioMarketDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.cross_margin_collateral_ratio_market_data()
    # TODO: Handle 'response' of type list[SapiV1MarginCrossMarginCollateralRatioResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CrossMarginCollateralRatioMarketDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginCrossMarginCollateralRatioResponse](binance/models/sapi_v1_margin_cross_margin_collateral_ratio_response.py)&#93;</code> -- Margin collateral ratio

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CrossMarginCollateralRatioMarketDataErrorBody](binance/errors/cross_margin_collateral_ratio_market_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def disable_isolated_margin_account_trade(symbol: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginIsolatedAccountResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Disable isolated margin account for a specific symbol. Each trading pair can only be deactivated once every 24 hours .

Weight(UID): 300

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.disable_isolated_margin_account_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginIsolatedAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DisableIsolatedMarginAccountTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.disable_isolated_margin_account_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginIsolatedAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DisableIsolatedMarginAccountTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginIsolatedAccountResponse](binance/models/sapi_v1_margin_isolated_account_response.py)</code> -- Isolated Margin Account status

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[DisableIsolatedMarginAccountTradeErrorBody](binance/errors/disable_isolated_margin_account_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_isolated_margin_account_trade(symbol: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginIsolatedAccountResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enable isolated margin account for a specific symbol.

Weight(UID): 300

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.enable_isolated_margin_account_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginIsolatedAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableIsolatedMarginAccountTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.enable_isolated_margin_account_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginIsolatedAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableIsolatedMarginAccountTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginIsolatedAccountResponse](binance/models/sapi_v1_margin_isolated_account_response.py)</code> -- Isolated Margin Account status

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[EnableIsolatedMarginAccountTradeErrorBody](binance/errors/enable_isolated_margin_account_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_all_cross_margin_pairs_market_data(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginAllPairsResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.get_all_cross_margin_pairs_market_data(symbol)
    # TODO: Handle 'response' of type list[SapiV1MarginAllPairsResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAllCrossMarginPairsMarketDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.get_all_cross_margin_pairs_market_data(symbol)
    # TODO: Handle 'response' of type list[SapiV1MarginAllPairsResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAllCrossMarginPairsMarketDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginAllPairsResponse](binance/models/sapi_v1_margin_all_pairs_response.py)&#93;</code> -- Margin pairs

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetAllCrossMarginPairsMarketDataErrorBody](binance/errors/get_all_cross_margin_pairs_market_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_all_isolated_margin_symbol_user_data(symbol: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginIsolatedAllPairsResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.get_all_isolated_margin_symbol_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginIsolatedAllPairsResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAllIsolatedMarginSymbolUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.get_all_isolated_margin_symbol_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginIsolatedAllPairsResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAllIsolatedMarginSymbolUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginIsolatedAllPairsResponse](binance/models/sapi_v1_margin_isolated_all_pairs_response.py)&#93;</code> -- All Isolated Margin Symbols

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetAllIsolatedMarginSymbolUserDataErrorBody](binance/errors/get_all_isolated_margin_symbol_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_all_margin_assets_market_data(asset: str, *, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginAllAssetsResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.get_all_margin_assets_market_data(asset)
    # TODO: Handle 'response' of type list[SapiV1MarginAllAssetsResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAllMarginAssetsMarketDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.get_all_margin_assets_market_data(asset)
    # TODO: Handle 'response' of type list[SapiV1MarginAllAssetsResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAllMarginAssetsMarketDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginAllAssetsResponse](binance/models/sapi_v1_margin_all_assets_response.py)&#93;</code> -- Assets details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetAllMarginAssetsMarketDataErrorBody](binance/errors/get_all_margin_assets_market_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_bnb_burn_status_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> BnbBurnStatus</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.get_bnb_burn_status_user_data(timestamp, signature)
    # TODO: Handle 'response' of type BnbBurnStatus
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBnbBurnStatusUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.get_bnb_burn_status_user_data(timestamp, signature)
    # TODO: Handle 'response' of type BnbBurnStatus
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBnbBurnStatusUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BnbBurnStatus](binance/models/bnb_burn_status.py)</code> -- Status on BNB to pay for trading fees

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetBnbBurnStatusUserDataErrorBody](binance/errors/get_bnb_burn_status_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_cross_margin_transfer_history_user_data(timestamp: int, signature: str, *, asset: str | None = None, type_: Type2OrStr | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, isolated_symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginTransferResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- Response in descending order
- Returns data for last 7 days by default
- Set `archived` to `true` to query data from 6 months ago

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.get_cross_margin_transfer_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCrossMarginTransferHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.get_cross_margin_transfer_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCrossMarginTransferHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>type_</code> | <code>[Type2OrStr](binance/models/enums/type2.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>isolated_symbol</code> | <code>str \| None</code> | Isolated symbol<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginTransferResponse](binance/models/sapi_v1_margin_transfer_response.py)</code> -- Margin account transfer history, response in descending order

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetCrossMarginTransferHistoryUserDataErrorBody](binance/errors/get_cross_margin_transfer_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_force_liquidation_record_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, isolated_symbol: str | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginForceLiquidationRecResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- Response in descending order

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.get_force_liquidation_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginForceLiquidationRecResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetForceLiquidationRecordUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.get_force_liquidation_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginForceLiquidationRecResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetForceLiquidationRecordUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>isolated_symbol</code> | <code>str \| None</code> | Isolated symbol<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginForceLiquidationRecResponse](binance/models/sapi_v1_margin_force_liquidation_rec_response.py)</code> -- Force Liquidation History, response in descending order

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetForceLiquidationRecordUserDataErrorBody](binance/errors/get_force_liquidation_record_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_interest_history_user_data(timestamp: int, signature: str, *, asset: str | None = None, isolated_symbol: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, archived: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginInterestHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- Response in descending order
- If `isolatedSymbol` is not sent, crossed margin data will be returned
- Set `archived` to `true` to query data from 6 months ago
- `type` in response has 4 enums:
  - `PERIODIC` interest charged per hour
  - `ON_BORROW` first interest charged on borrow
  - `PERIODIC_CONVERTED` interest charged per hour converted into BNB
  - `ON_BORROW_CONVERTED` first interest charged on borrow converted into BNB

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.get_interest_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginInterestHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetInterestHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.get_interest_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginInterestHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetInterestHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>isolated_symbol</code> | <code>str \| None</code> | Isolated symbol<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>archived</code> | <code>str \| None</code> | Default: false. Set to true for archived data from 6 months ago<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginInterestHistoryResponse](binance/models/sapi_v1_margin_interest_history_response.py)</code> -- Interest History, response in descending order

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetInterestHistoryUserDataErrorBody](binance/errors/get_interest_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_small_liability_exchange_coin_list_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginExchangeSmallLiabilityResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query the coins which can be small liability exchange

Weight(UID): 100

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.get_small_liability_exchange_coin_list_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginExchangeSmallLiabilityResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSmallLiabilityExchangeCoinListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.get_small_liability_exchange_coin_list_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginExchangeSmallLiabilityResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSmallLiabilityExchangeCoinListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginExchangeSmallLiabilityResponse](binance/models/sapi_v1_margin_exchange_small_liability_response.py)&#93;</code> -- coin list

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetSmallLiabilityExchangeCoinListUserDataErrorBody](binance/errors/get_small_liability_exchange_coin_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_small_liability_exchange_history_user_data(timestamp: int, signature: str, *, current: int | None = None, size: int | None = None, start_time: int | None = None, end_time: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginExchangeSmallLiabilityHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Small liability Exchange History

Weight(UID): 100

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.get_small_liability_exchange_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginExchangeSmallLiabilityHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSmallLiabilityExchangeHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.get_small_liability_exchange_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginExchangeSmallLiabilityHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSmallLiabilityExchangeHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginExchangeSmallLiabilityHistoryResponse](binance/models/sapi_v1_margin_exchange_small_liability_history_response.py)</code> -- coin list

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetSmallLiabilityExchangeHistoryUserDataErrorBody](binance/errors/get_small_liability_exchange_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_summary_of_margin_account_user_data(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginTradeCoeffResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get personal margin level information

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.get_summary_of_margin_account_user_data(email, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginTradeCoeffResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSummaryOfMarginAccountUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.get_summary_of_margin_account_user_data(email, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginTradeCoeffResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSummaryOfMarginAccountUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Email Address |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginTradeCoeffResponse](binance/models/sapi_v1_margin_trade_coeff_response.py)</code> -- Summary of Margin Account

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetSummaryOfMarginAccountUserDataErrorBody](binance/errors/get_summary_of_margin_account_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_a_future_hourly_interest_rate_user_data(timestamp: int, signature: str, *, assets: str | None = None, is_isolated: IsIsolatedOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginNextHourlyInterestRateResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get user the next hourly estimate interest

Weight(UID): 100

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.get_a_future_hourly_interest_rate_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginNextHourlyInterestRateResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAFutureHourlyInterestRateUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.get_a_future_hourly_interest_rate_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginNextHourlyInterestRateResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAFutureHourlyInterestRateUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>assets</code> | <code>str \| None</code> | List of assets, separated by commas, up to 20<br>**Default**: <code>None</code> |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | for isolated margin or not, "TRUE", "FALSE"<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginNextHourlyInterestRateResponse](binance/models/sapi_v1_margin_next_hourly_interest_rate_response.py)&#93;</code> -- hourly interest

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetAFutureHourlyInterestRateUserDataErrorBody](binance/errors/get_a_future_hourly_interest_rate_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_cross_or_isolated_margin_capital_flow_user_data(timestamp: int, signature: str, *, asset: str | None = None, symbol: str | None = None, type_: Type3OrStr | None = None, start_time: int | None = None, end_time: int | None = None, from_id: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginCapitalFlowResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get cross or isolated margin capital flow

Weight(IP): 100

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.get_cross_or_isolated_margin_capital_flow_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginCapitalFlowResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCrossOrIsolatedMarginCapitalFlowUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.get_cross_or_isolated_margin_capital_flow_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginCapitalFlowResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCrossOrIsolatedMarginCapitalFlowUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>symbol</code> | <code>str \| None</code> | Required when querying isolated data<br>**Default**: <code>None</code> |
| <code>type_</code> | <code>[Type3OrStr](binance/models/enums/type3.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | Only supports querying the data of the last 90 days<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>from_id</code> | <code>int \| None</code> | If fromId is set, the data with id > fromId will be returned. Otherwise the latest data will be returned<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The number of data items returned each time is limited. Default 500; Max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginCapitalFlowResponse](binance/models/sapi_v1_margin_capital_flow_response.py)&#93;</code> -- Margin capital flow

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetCrossOrIsolatedMarginCapitalFlowUserDataErrorBody](binance/errors/get_cross_or_isolated_margin_capital_flow_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginDelistScheduleResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get tokens or symbols delist schedule for cross margin and isolated margin

Weight(IP): 100

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data(
        timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1MarginDelistScheduleResponse]
except ApiError as e:
    # TODO: Handle 'e.error' of type GetTokensOrSymbolsDelistScheduleForCrossMarginAndIsolatedMarginMarketDataErrorBody
    ...
```

**Async**

```python
try:
    response = await async_client.margin.get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data(
        timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1MarginDelistScheduleResponse]
except ApiError as e:
    # TODO: Handle 'e.error' of type GetTokensOrSymbolsDelistScheduleForCrossMarginAndIsolatedMarginMarketDataErrorBody
    ...
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginDelistScheduleResponse](binance/models/sapi_v1_margin_delist_schedule_response.py)&#93;</code> -- tokens or symbols delist schedule

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetTokensOrSymbolsDelistScheduleForCrossMarginAndIsolatedMarginMarketDataErrorBody](binance/errors/get_tokens_or_symbols_delist_schedule_for_cross_margin_and_isolated_margin_market_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def margin_account_cancel_oco_trade(symbol: str, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, order_list_id: int | None = None, list_client_order_id: str | None = None, new_client_order_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> MarginOcoOrder</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancel an entire Order List for a margin account

- Canceling an individual leg will cancel the entire OCO
- Either `orderListId` or `listClientOrderId` must be provided

Weight(UID): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.margin_account_cancel_oco_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type MarginOcoOrder
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountCancelOcoTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.margin_account_cancel_oco_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type MarginOcoOrder
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountCancelOcoTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>order_list_id</code> | <code>int \| None</code> | Order list id<br>**Default**: <code>None</code> |
| <code>list_client_order_id</code> | <code>str \| None</code> | A unique Id for the entire orderList<br>**Default**: <code>None</code> |
| <code>new_client_order_id</code> | <code>str \| None</code> | Used to uniquely identify this cancel. Automatically generated by default<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MarginOcoOrder](binance/models/margin_oco_order.py)</code> -- Margin OCO details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[MarginAccountCancelOcoTradeErrorBody](binance/errors/margin_account_cancel_oco_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def margin_account_cancel_order_trade(symbol: str, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, order_id: int | None = None, orig_client_order_id: str | None = None, new_client_order_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> MarginOrder</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancel an active order for margin account.

Either `orderId` or `origClientOrderId` must be sent.

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.margin_account_cancel_order_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type MarginOrder
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountCancelOrderTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.margin_account_cancel_order_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type MarginOrder
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountCancelOrderTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>order_id</code> | <code>int \| None</code> | Order id<br>**Default**: <code>None</code> |
| <code>orig_client_order_id</code> | <code>str \| None</code> | Order id from client<br>**Default**: <code>None</code> |
| <code>new_client_order_id</code> | <code>str \| None</code> | Used to uniquely identify this cancel. Automatically generated by default<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MarginOrder](binance/models/margin_order.py)</code> -- Cancelled margin order details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[MarginAccountCancelOrderTradeErrorBody](binance/errors/margin_account_cancel_order_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def margin_account_cancel_all_open_orders_on_a_symbol_trade(symbol: str, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginOpenOrdersResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- Cancels all active orders on a symbol for margin account.
- This includes OCO orders.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.margin_account_cancel_all_open_orders_on_a_symbol_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginOpenOrdersResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountCancelAllOpenOrdersOnASymbolTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.margin_account_cancel_all_open_orders_on_a_symbol_trade(
        symbol, timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1MarginOpenOrdersResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountCancelAllOpenOrdersOnASymbolTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginOpenOrdersResponse](binance/models/unions/sapi_v1_margin_open_orders_response.py)&#93;</code> -- Cancelled margin orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[MarginAccountCancelAllOpenOrdersOnASymbolTradeErrorBody](binance/errors/margin_account_cancel_all_open_orders_on_a_symbol_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def margin_account_new_oco_trade(symbol: str, side: SideOrStr, quantity: float, price: float, stop_price: float, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, list_client_order_id: str | None = None, limit_client_order_id: str | None = None, limit_iceberg_qty: float | None = None, stop_client_order_id: str | None = None, stop_limit_price: float | None = None, stop_iceberg_qty: float | None = None, stop_limit_time_in_force: StopLimitTimeInForceOrStr | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, side_effect_type: SideEffectTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginOrderOcoResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send in a new OCO for a margin account

- Price Restrictions:
  - SELL: Limit Price > Last Price > Stop Price
  - BUY: Limit Price < Last Price < Stop Price
- Quantity Restrictions:
  - Both legs must have the same quantity
  - ICEBERG quantities however do not have to be the same.
- Order Rate Limit
  - OCO counts as 2 orders against the order rate limit.

Weight(UID): 6

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.margin_account_new_oco_trade(
        symbol, side, quantity, price, stop_price, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1MarginOrderOcoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountNewOcoTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.margin_account_new_oco_trade(
        symbol, side, quantity, price, stop_price, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1MarginOrderOcoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountNewOcoTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>side</code> | <code>[SideOrStr](binance/models/enums/side.py)</code> | Value sent with the request. |
| <code>quantity</code> | <code>float</code> | Value sent with the request. |
| <code>price</code> | <code>float</code> | Order price |
| <code>stop_price</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>list_client_order_id</code> | <code>str \| None</code> | A unique Id for the entire orderList<br>**Default**: <code>None</code> |
| <code>limit_client_order_id</code> | <code>str \| None</code> | A unique Id for the limit order<br>**Default**: <code>None</code> |
| <code>limit_iceberg_qty</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>stop_client_order_id</code> | <code>str \| None</code> | A unique Id for the stop loss/stop loss limit leg<br>**Default**: <code>None</code> |
| <code>stop_limit_price</code> | <code>float \| None</code> | If provided, stopLimitTimeInForce is required.<br>**Default**: <code>None</code> |
| <code>stop_iceberg_qty</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>stop_limit_time_in_force</code> | <code>[StopLimitTimeInForceOrStr](binance/models/enums/stop_limit_time_in_force.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>new_order_resp_type</code> | <code>[NewOrderRespTypeOrStr](binance/models/enums/new_order_resp_type.py) \| None</code> | Set the response JSON.<br>**Default**: <code>None</code> |
| <code>side_effect_type</code> | <code>[SideEffectTypeOrStr](binance/models/enums/side_effect_type.py) \| None</code> | Default `NO_SIDE_EFFECT`<br>**Default**: <code>None</code> |
| <code>self_trade_prevention_mode</code> | <code>[SelfTradePreventionModeOrStr](binance/models/enums/self_trade_prevention_mode.py) \| None</code> | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginOrderOcoResponse](binance/models/sapi_v1_margin_order_oco_response.py)</code> -- New Margin OCO details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[MarginAccountNewOcoTradeErrorBody](binance/errors/margin_account_new_oco_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def margin_account_new_oto_trade(symbol: str, working_type: WorkingTypeOrStr, working_side: WorkingSideOrStr, working_price: float, working_quantity: float, working_iceberg_qty: float, pending_type: PendingTypeOrStr, pending_side: PendingSideOrStr, pending_quantity: float, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, list_client_order_id: str | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, side_effect_type: SideEffectType1OrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, auto_repay_at_cancel: bool | None = None, working_client_order_id: str | None = None, working_time_in_force: WorkingTimeInForceOrStr | None = None, pending_client_order_id: str | None = None, pending_price: float | None = None, pending_stop_price: float | None = None, pending_trailing_delta: float | None = None, pending_iceberg_qty: float | None = None, pending_time_in_force: PendingTimeInForceOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginOrderOtoResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Post a new `OTO` order for margin account:
- An `OTO` (One-Triggers-the-Other) is an order list comprised of 2 orders
- The first order is called the working order and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the working order goes on the order book.
- The second order is called the pending order. It can be any order type except for `MARKET` orders using parameter `quoteOrderQty`. The pending order is only placed on the order book when the working order gets fully filled.
- If either the working order or the pending order is cancelled individually, the other order in the order list will also be canceled or expired.
- When the order list is placed, if the working order gets immediately fully filled, the placement response will show the working order as `FILLED` but the pending order will still appear as `PENDING_NEW`. You need to query the status of the pending order again to see its updated status.
- OTOs add 2 orders to the unfilled order count, `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.

Weight(UID): 6

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.margin_account_new_oto_trade(
        symbol,
        working_type,
        working_side,
        working_price,
        working_quantity,
        working_iceberg_qty,
        pending_type,
        pending_side,
        pending_quantity,
        timestamp,
        signature,
    )
    # TODO: Handle 'response' of type SapiV1MarginOrderOtoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountNewOtoTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.margin_account_new_oto_trade(
        symbol,
        working_type,
        working_side,
        working_price,
        working_quantity,
        working_iceberg_qty,
        pending_type,
        pending_side,
        pending_quantity,
        timestamp,
        signature,
    )
    # TODO: Handle 'response' of type SapiV1MarginOrderOtoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountNewOtoTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>working_type</code> | <code>[WorkingTypeOrStr](binance/models/enums/working_type.py)</code> | Supported values: LIMIT,LIMIT_MAKER |
| <code>working_side</code> | <code>[WorkingSideOrStr](binance/models/enums/working_side.py)</code> | BUY,SELL |
| <code>working_price</code> | <code>float</code> | Value sent with the request. |
| <code>working_quantity</code> | <code>float</code> | Sets the quantity for the working order. |
| <code>working_iceberg_qty</code> | <code>float</code> | This can only be used if workingTimeInForce is GTC. |
| <code>pending_type</code> | <code>[PendingTypeOrStr](binance/models/enums/pending_type.py)</code> | Supported values: Order Types Note that MARKET orders using quoteOrderQty are not supported. |
| <code>pending_side</code> | <code>[PendingSideOrStr](binance/models/enums/pending_side.py)</code> | BUY,SELL |
| <code>pending_quantity</code> | <code>float</code> | Sets the quantity for the pending order. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>list_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open order lists. Automatically generated if not sent.<br>A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired.<br>`listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.<br>**Default**: <code>None</code> |
| <code>new_order_resp_type</code> | <code>[NewOrderRespTypeOrStr](binance/models/enums/new_order_resp_type.py) \| None</code> | Set the response JSON.<br>**Default**: <code>None</code> |
| <code>side_effect_type</code> | <code>[SideEffectType1OrStr](binance/models/enums/side_effect_type1.py) \| None</code> | Default `NO_SIDE_EFFECT`<br>**Default**: <code>None</code> |
| <code>self_trade_prevention_mode</code> | <code>[SelfTradePreventionModeOrStr](binance/models/enums/self_trade_prevention_mode.py) \| None</code> | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.<br>**Default**: <code>None</code> |
| <code>auto_repay_at_cancel</code> | <code>bool \| None</code> | Only when MARGIN_BUY order takes effect, true means that the debt generated by the order needs to be repay after the order is cancelled. The default is true<br>**Default**: <code>None</code> |
| <code>working_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.<br>**Default**: <code>None</code> |
| <code>working_time_in_force</code> | <code>[WorkingTimeInForceOrStr](binance/models/enums/working_time_in_force.py) \| None</code> | GTC, IOC, FOK<br>**Default**: <code>None</code> |
| <code>pending_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent.<br>**Default**: <code>None</code> |
| <code>pending_price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_stop_price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_trailing_delta</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_iceberg_qty</code> | <code>float \| None</code> | This can only be used if pendingTimeInForce is GTC.<br>**Default**: <code>None</code> |
| <code>pending_time_in_force</code> | <code>[PendingTimeInForceOrStr](binance/models/enums/pending_time_in_force.py) \| None</code> | GTC, IOC, FOK<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginOrderOtoResponse](binance/models/sapi_v1_margin_order_oto_response.py)</code> -- OTO order

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[MarginAccountNewOtoTradeErrorBody](binance/errors/margin_account_new_oto_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def margin_account_new_otoco_trade(symbol: str, working_type: WorkingTypeOrStr, working_side: WorkingSideOrStr, working_price: float, working_quantity: float, working_iceberg_qty: float, pending_side: PendingSideOrStr, pending_quantity: float, pending_above_type: PendingAboveTypeOrStr, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, side_effect_type: SideEffectType1OrStr | None = None, auto_repay_at_cancel: bool | None = None, list_client_order_id: str | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, working_client_order_id: str | None = None, working_time_in_force: WorkingTimeInForceOrStr | None = None, pending_above_client_order_id: str | None = None, pending_above_price: float | None = None, pending_above_stop_price: float | None = None, pending_above_trailing_delta: float | None = None, pending_above_iceberg_qty: float | None = None, pending_above_time_in_force: PendingAboveTimeInForceOrStr | None = None, pending_below_type: PendingBelowTypeOrStr | None = None, pending_below_client_order_id: str | None = None, pending_below_price: float | None = None, pending_below_stop_price: float | None = None, pending_below_trailing_delta: float | None = None, pending_below_iceberg_qty: float | None = None, pending_below_time_in_force: PendingBelowTimeInForceOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginOrderOtocoResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Post a new `OTOCO` order for margin account:
- An `OTOCO` (One-Triggers-the-Other-Cancel-the-Other) is an order list comprised of 3 orders
- The first order is called the working order and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the working order goes on the order book.
  - The behavior of the working order is the same as the `OTO`.
- `OTOCO` has 2 pending orders (pending above and pending below), forming an `OCO` pair. The pending orders are only placed on the order book when the working order gets fully filled.
  - The rules of the pending above and pending below follow the same rules as the Order List `OCO`.
- OTOCOs add 3 orders to the unfilled order count, `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.

Weight(UID): 6

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.margin_account_new_otoco_trade(
        symbol,
        working_type,
        working_side,
        working_price,
        working_quantity,
        working_iceberg_qty,
        pending_side,
        pending_quantity,
        pending_above_type,
        timestamp,
        signature,
    )
    # TODO: Handle 'response' of type SapiV1MarginOrderOtocoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountNewOtocoTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.margin_account_new_otoco_trade(
        symbol,
        working_type,
        working_side,
        working_price,
        working_quantity,
        working_iceberg_qty,
        pending_side,
        pending_quantity,
        pending_above_type,
        timestamp,
        signature,
    )
    # TODO: Handle 'response' of type SapiV1MarginOrderOtocoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountNewOtocoTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>working_type</code> | <code>[WorkingTypeOrStr](binance/models/enums/working_type.py)</code> | Supported values: LIMIT,LIMIT_MAKER |
| <code>working_side</code> | <code>[WorkingSideOrStr](binance/models/enums/working_side.py)</code> | BUY,SELL |
| <code>working_price</code> | <code>float</code> | Value sent with the request. |
| <code>working_quantity</code> | <code>float</code> | Sets the quantity for the working order. |
| <code>working_iceberg_qty</code> | <code>float</code> | This can only be used if workingTimeInForce is GTC. |
| <code>pending_side</code> | <code>[PendingSideOrStr](binance/models/enums/pending_side.py)</code> | BUY,SELL |
| <code>pending_quantity</code> | <code>float</code> | Sets the quantity for the pending order. |
| <code>pending_above_type</code> | <code>[PendingAboveTypeOrStr](binance/models/enums/pending_above_type.py)</code> | Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>side_effect_type</code> | <code>[SideEffectType1OrStr](binance/models/enums/side_effect_type1.py) \| None</code> | Default `NO_SIDE_EFFECT`<br>**Default**: <code>None</code> |
| <code>auto_repay_at_cancel</code> | <code>bool \| None</code> | Only when MARGIN_BUY order takes effect, true means that the debt generated by the order needs to be repay after the order is cancelled. The default is true<br>**Default**: <code>None</code> |
| <code>list_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open order lists. Automatically generated if not sent.<br>A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired.<br>`listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.<br>**Default**: <code>None</code> |
| <code>new_order_resp_type</code> | <code>[NewOrderRespTypeOrStr](binance/models/enums/new_order_resp_type.py) \| None</code> | Set the response JSON.<br>**Default**: <code>None</code> |
| <code>self_trade_prevention_mode</code> | <code>[SelfTradePreventionModeOrStr](binance/models/enums/self_trade_prevention_mode.py) \| None</code> | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.<br>**Default**: <code>None</code> |
| <code>working_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.<br>**Default**: <code>None</code> |
| <code>working_time_in_force</code> | <code>[WorkingTimeInForceOrStr](binance/models/enums/working_time_in_force.py) \| None</code> | GTC, IOC, FOK<br>**Default**: <code>None</code> |
| <code>pending_above_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent.<br>**Default**: <code>None</code> |
| <code>pending_above_price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_above_stop_price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_above_trailing_delta</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_above_iceberg_qty</code> | <code>float \| None</code> | This can only be used if pendingAboveTimeInForce is GTC.<br>**Default**: <code>None</code> |
| <code>pending_above_time_in_force</code> | <code>[PendingAboveTimeInForceOrStr](binance/models/enums/pending_above_time_in_force.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_below_type</code> | <code>[PendingBelowTypeOrStr](binance/models/enums/pending_below_type.py) \| None</code> | Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT<br>**Default**: <code>None</code> |
| <code>pending_below_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent.<br>**Default**: <code>None</code> |
| <code>pending_below_price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_below_stop_price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_below_trailing_delta</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_below_iceberg_qty</code> | <code>float \| None</code> | This can only be used if pendingBelowTimeInForce is GTC.<br>**Default**: <code>None</code> |
| <code>pending_below_time_in_force</code> | <code>[PendingBelowTimeInForceOrStr](binance/models/enums/pending_below_time_in_force.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginOrderOtocoResponse](binance/models/sapi_v1_margin_order_otoco_response.py)</code> -- OTOCO order

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[MarginAccountNewOtocoTradeErrorBody](binance/errors/margin_account_new_otoco_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def margin_account_new_order_trade(symbol: str, side: SideOrStr, type_: Type1OrStr, quantity: float, auto_repay_at_cancel: bool, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, quote_order_qty: float | None = None, price: float | None = None, stop_price: float | None = None, new_client_order_id: str | None = None, iceberg_qty: float | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, side_effect_type: SideEffectTypeOrStr | None = None, time_in_force: TimeInForceOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginOrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Post a new order for margin account.

Weight(UID): 6

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.margin_account_new_order_trade(
        symbol, side, type_, quantity, auto_repay_at_cancel, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1MarginOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountNewOrderTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.margin_account_new_order_trade(
        symbol, side, type_, quantity, auto_repay_at_cancel, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1MarginOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountNewOrderTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>side</code> | <code>[SideOrStr](binance/models/enums/side.py)</code> | Value sent with the request. |
| <code>type_</code> | <code>[Type1OrStr](binance/models/enums/type1.py)</code> | Order type |
| <code>quantity</code> | <code>float</code> | Value sent with the request. |
| <code>auto_repay_at_cancel</code> | <code>bool</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>quote_order_qty</code> | <code>float \| None</code> | Quote quantity<br>**Default**: <code>None</code> |
| <code>price</code> | <code>float \| None</code> | Order price<br>**Default**: <code>None</code> |
| <code>stop_price</code> | <code>float \| None</code> | Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.<br>**Default**: <code>None</code> |
| <code>new_client_order_id</code> | <code>str \| None</code> | Used to uniquely identify this cancel. Automatically generated by default<br>**Default**: <code>None</code> |
| <code>iceberg_qty</code> | <code>float \| None</code> | Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.<br>**Default**: <code>None</code> |
| <code>new_order_resp_type</code> | <code>[NewOrderRespTypeOrStr](binance/models/enums/new_order_resp_type.py) \| None</code> | Set the response JSON.<br>**Default**: <code>None</code> |
| <code>side_effect_type</code> | <code>[SideEffectTypeOrStr](binance/models/enums/side_effect_type.py) \| None</code> | Default `NO_SIDE_EFFECT`<br>**Default**: <code>None</code> |
| <code>time_in_force</code> | <code>[TimeInForceOrStr](binance/models/enums/time_in_force.py) \| None</code> | Order time in force<br>**Default**: <code>None</code> |
| <code>self_trade_prevention_mode</code> | <code>[SelfTradePreventionModeOrStr](binance/models/enums/self_trade_prevention_mode.py) \| None</code> | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginOrderResponse](binance/models/unions/sapi_v1_margin_order_response.py)</code> -- Margin order info

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[MarginAccountNewOrderTradeErrorBody](binance/errors/margin_account_new_order_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def margin_interest_rate_history_user_data(asset: str, timestamp: int, signature: str, *, vip_level: int | None = None, start_time: int | None = None, end_time: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginInterestRateHistoryResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The max interval between startTime and endTime is 30 days.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.margin_interest_rate_history_user_data(asset, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginInterestRateHistoryResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginInterestRateHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.margin_interest_rate_history_user_data(asset, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginInterestRateHistoryResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginInterestRateHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>vip_level</code> | <code>int \| None</code> | Defaults to user's vip level<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginInterestRateHistoryResponse](binance/models/sapi_v1_margin_interest_rate_history_response.py)&#93;</code> -- Margin Interest Rate History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[MarginInterestRateHistoryUserDataErrorBody](binance/errors/margin_interest_rate_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def margin_account_borrow_repay_margin(asset: str, is_isolated: str, symbol: str, amount: float, type_: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginBorrowRepayResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Margin account borrow/repay(MARGIN)

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.margin_account_borrow_repay_margin(
        asset, is_isolated, symbol, amount, type_, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1MarginBorrowRepayResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountBorrowRepayMarginErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.margin_account_borrow_repay_margin(
        asset, is_isolated, symbol, amount, type_, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1MarginBorrowRepayResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginAccountBorrowRepayMarginErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>is_isolated</code> | <code>str</code> | TRUE for isolated margin, FALSE for crossed margin |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>type_</code> | <code>str</code> | BORROW or REPAY |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginBorrowRepayResponse](binance/models/sapi_v1_margin_borrow_repay_response.py)</code> -- Margin account borrow/repay

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[MarginAccountBorrowRepayMarginErrorBody](binance/errors/margin_account_borrow_repay_margin_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def margin_manual_liquidation_margin(type_: Type4OrStr, timestamp: int, signature: str, *, symbol: str | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginManualLiquidationResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Margin manual liquidation

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.margin_manual_liquidation_margin(type_, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginManualLiquidationResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginManualLiquidationMarginErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.margin_manual_liquidation_margin(type_, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginManualLiquidationResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginManualLiquidationMarginErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[Type4OrStr](binance/models/enums/type4.py)</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>symbol</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginManualLiquidationResponse](binance/models/sapi_v1_margin_manual_liquidation_response.py)&#93;</code> -- Margin manual liquidation

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[MarginManualLiquidationMarginErrorBody](binance/errors/margin_manual_liquidation_margin_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_cross_margin_account_details_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginAccountResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_cross_margin_account_details_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryCrossMarginAccountDetailsUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_cross_margin_account_details_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryCrossMarginAccountDetailsUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginAccountResponse](binance/models/sapi_v1_margin_account_response.py)</code> -- Margin account details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryCrossMarginAccountDetailsUserDataErrorBody](binance/errors/query_cross_margin_account_details_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_cross_margin_fee_data_user_data(timestamp: int, signature: str, *, vip_level: int | None = None, coin: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginCrossMarginDataResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get cross margin fee data collection with any vip level or user's current specific data as https://www.binance.com/en/margin-fee

Weight(IP): 1 when coin is specified; 5 when the coin parameter is omitted

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_cross_margin_fee_data_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginCrossMarginDataResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryCrossMarginFeeDataUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_cross_margin_fee_data_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginCrossMarginDataResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryCrossMarginFeeDataUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>vip_level</code> | <code>int \| None</code> | Defaults to user's vip level<br>**Default**: <code>None</code> |
| <code>coin</code> | <code>str \| None</code> | Coin name<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginCrossMarginDataResponse](binance/models/sapi_v1_margin_cross_margin_data_response.py)&#93;</code> -- Cross Margin Fee Data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryCrossMarginFeeDataUserDataErrorBody](binance/errors/query_cross_margin_fee_data_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_current_margin_order_count_usage_trade(timestamp: int, signature: str, *, is_isolated: str | None = None, symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginRateLimitOrderResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Displays the user's current margin order count usage for all intervals.

Weight(IP): 20

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_current_margin_order_count_usage_trade(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginRateLimitOrderResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryCurrentMarginOrderCountUsageTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_current_margin_order_count_usage_trade(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginRateLimitOrderResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryCurrentMarginOrderCountUsageTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>is_isolated</code> | <code>str \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>symbol</code> | <code>str \| None</code> | isolated symbol, mandatory for isolated margin<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginRateLimitOrderResponse](binance/models/sapi_v1_margin_rate_limit_order_response.py)&#93;</code> -- Usage.

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryCurrentMarginOrderCountUsageTradeErrorBody](binance/errors/query_current_margin_order_count_usage_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_enabled_isolated_margin_account_limit_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginIsolatedAccountLimitResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query enabled isolated margin account limit.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_enabled_isolated_margin_account_limit_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginIsolatedAccountLimitResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryEnabledIsolatedMarginAccountLimitUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_enabled_isolated_margin_account_limit_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginIsolatedAccountLimitResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryEnabledIsolatedMarginAccountLimitUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginIsolatedAccountLimitResponse](binance/models/sapi_v1_margin_isolated_account_limit_response.py)</code> -- Number of enabled Isolated Margin Account and its limit

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryEnabledIsolatedMarginAccountLimitUserDataErrorBody](binance/errors/query_enabled_isolated_margin_account_limit_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_isolated_margin_account_info_user_data(timestamp: int, signature: str, *, symbols: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> IsolatedMarginAccountInfo</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If "symbols" is not sent, all isolated assets will be returned.
- If "symbols" is sent, only the isolated assets of the sent symbols will be returned.

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_isolated_margin_account_info_user_data(timestamp, signature)
    # TODO: Handle 'response' of type IsolatedMarginAccountInfo
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryIsolatedMarginAccountInfoUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_isolated_margin_account_info_user_data(timestamp, signature)
    # TODO: Handle 'response' of type IsolatedMarginAccountInfo
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryIsolatedMarginAccountInfoUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>symbols</code> | <code>str \| None</code> | Max 5 symbols can be sent; separated by ','<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[IsolatedMarginAccountInfo](binance/models/isolated_margin_account_info.py)</code> -- Isolated Margin Account Info when "symbols" is not sent

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryIsolatedMarginAccountInfoUserDataErrorBody](binance/errors/query_isolated_margin_account_info_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_isolated_margin_fee_data_user_data(timestamp: int, signature: str, *, vip_level: int | None = None, symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginIsolatedMarginDataResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get isolated margin fee data collection with any vip level or user's current specific data as https://www.binance.com/en/margin-fee

Weight(IP): 1 when a single is specified; 10 when the symbol parameter is omitted

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_isolated_margin_fee_data_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginIsolatedMarginDataResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryIsolatedMarginFeeDataUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_isolated_margin_fee_data_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginIsolatedMarginDataResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryIsolatedMarginFeeDataUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>vip_level</code> | <code>int \| None</code> | Defaults to user's vip level<br>**Default**: <code>None</code> |
| <code>symbol</code> | <code>str \| None</code> | Trading symbol, e.g. BNBUSDT<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginIsolatedMarginDataResponse](binance/models/sapi_v1_margin_isolated_margin_data_response.py)&#93;</code> -- Isolated Margin Fee Data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryIsolatedMarginFeeDataUserDataErrorBody](binance/errors/query_isolated_margin_fee_data_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_isolated_margin_tier_data_user_data(symbol: str, timestamp: int, signature: str, *, tier: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginIsolatedMarginTierResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get isolated margin tier data collection with any tier as https://www.binance.com/en/margin-data

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_isolated_margin_tier_data_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginIsolatedMarginTierResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryIsolatedMarginTierDataUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_isolated_margin_tier_data_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginIsolatedMarginTierResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryIsolatedMarginTierDataUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>tier</code> | <code>str \| None</code> | All margin tier data will be returned if tier is omitted<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginIsolatedMarginTierResponse](binance/models/sapi_v1_margin_isolated_margin_tier_response.py)&#93;</code> -- Isolated Margin Tier Data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryIsolatedMarginTierDataUserDataErrorBody](binance/errors/query_isolated_margin_tier_data_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data(*, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginLeverageBracketResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Liability Coin Leverage Bracket in Cross Margin Pro Mode

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data()
    # TODO: Handle 'response' of type list[SapiV1MarginLeverageBracketResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryLiabilityCoinLeverageBracketInCrossMarginProModeMarketDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data()
    # TODO: Handle 'response' of type list[SapiV1MarginLeverageBracketResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryLiabilityCoinLeverageBracketInCrossMarginProModeMarketDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginLeverageBracketResponse](binance/models/sapi_v1_margin_leverage_bracket_response.py)&#93;</code> -- Leverage info

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryLiabilityCoinLeverageBracketInCrossMarginProModeMarketDataErrorBody](binance/errors/query_liability_coin_leverage_bracket_in_cross_margin_pro_mode_market_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_margin_account_s_all_orders_user_data(symbol: str, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, order_id: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[MarginOrderDetail]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If `orderId` is set, it will get orders >= that orderId. Otherwise most recent orders are returned.
- For some historical orders `cummulativeQuoteQty` will be < 0, meaning the data is not available at this time.

Weight(IP): 200

Request Limit: 60 times/min per IP

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_margin_account_s_all_orders_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[MarginOrderDetail]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAccountSAllOrdersUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_margin_account_s_all_orders_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[MarginOrderDetail]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAccountSAllOrdersUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>order_id</code> | <code>int \| None</code> | Order id<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[MarginOrderDetail](binance/models/margin_order_detail.py)&#93;</code> -- Margin order list

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryMarginAccountSAllOrdersUserDataErrorBody](binance/errors/query_margin_account_s_all_orders_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_margin_account_s_oco_user_data(timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, symbol: str | None = None, order_list_id: int | None = None, orig_client_order_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginOrderListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a specific OCO based on provided optional parameters

- Either `orderListId` or `origClientOrderId` must be provided

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_margin_account_s_oco_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginOrderListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAccountSOcoUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_margin_account_s_oco_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginOrderListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAccountSOcoUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>symbol</code> | <code>str \| None</code> | Mandatory for isolated margin, not supported for cross margin<br>**Default**: <code>None</code> |
| <code>order_list_id</code> | <code>int \| None</code> | Order list id<br>**Default**: <code>None</code> |
| <code>orig_client_order_id</code> | <code>str \| None</code> | Order id from client<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginOrderListResponse](binance/models/sapi_v1_margin_order_list_response.py)</code> -- Margin OCO details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryMarginAccountSOcoUserDataErrorBody](binance/errors/query_margin_account_s_oco_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_margin_account_s_open_oco_user_data(timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginOpenOrderListResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_margin_account_s_open_oco_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginOpenOrderListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAccountSOpenOcoUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_margin_account_s_open_oco_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginOpenOrderListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAccountSOpenOcoUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>symbol</code> | <code>str \| None</code> | Mandatory for isolated margin, not supported for cross margin<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginOpenOrderListResponse](binance/models/sapi_v1_margin_open_order_list_response.py)&#93;</code> -- List of Open Margin OCO orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryMarginAccountSOpenOcoUserDataErrorBody](binance/errors/query_margin_account_s_open_oco_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_margin_account_s_open_orders_user_data(timestamp: int, signature: str, *, symbol: str | None = None, is_isolated: IsIsolatedOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[MarginOrderDetail]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If the `symbol` is not sent, orders for all symbols will be returned in an array.
- When all symbols are returned, the number of requests counted against the rate limiter is equal to the number of symbols currently trading on the exchange
- If isIsolated ="TRUE", symbol must be sent.

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_margin_account_s_open_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[MarginOrderDetail]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAccountSOpenOrdersUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_margin_account_s_open_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[MarginOrderDetail]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAccountSOpenOrdersUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>symbol</code> | <code>str \| None</code> | Trading symbol, e.g. BNBUSDT<br>**Default**: <code>None</code> |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[MarginOrderDetail](binance/models/margin_order_detail.py)&#93;</code> -- Margin open orders list

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryMarginAccountSOpenOrdersUserDataErrorBody](binance/errors/query_margin_account_s_open_orders_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_margin_account_s_order_user_data(symbol: str, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, order_id: int | None = None, orig_client_order_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> MarginOrderDetail</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- Either `orderId` or `origClientOrderId` must be sent.
- For some historical orders `cummulativeQuoteQty` will be < 0, meaning the data is not available at this time.

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_margin_account_s_order_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type MarginOrderDetail
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAccountSOrderUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_margin_account_s_order_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type MarginOrderDetail
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAccountSOrderUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>order_id</code> | <code>int \| None</code> | Order id<br>**Default**: <code>None</code> |
| <code>orig_client_order_id</code> | <code>str \| None</code> | Order id from client<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MarginOrderDetail](binance/models/margin_order_detail.py)</code> -- Interest History, response in descending order

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryMarginAccountSOrderUserDataErrorBody](binance/errors/query_margin_account_s_order_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_margin_account_s_trade_list_user_data(symbol: str, timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, start_time: int | None = None, end_time: int | None = None, from_id: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[MarginTrade]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If `fromId` is set, it will get orders >= that `fromId`. Otherwise most recent trades are returned.

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_margin_account_s_trade_list_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[MarginTrade]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAccountSTradeListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_margin_account_s_trade_list_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[MarginTrade]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAccountSTradeListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>from_id</code> | <code>int \| None</code> | Trade id to fetch from. Default gets most recent trades.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[MarginTrade](binance/models/margin_trade.py)&#93;</code> -- List of margin trades

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryMarginAccountSTradeListUserDataErrorBody](binance/errors/query_margin_account_s_trade_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_margin_account_s_all_oco_user_data(timestamp: int, signature: str, *, is_isolated: IsIsolatedOrStr | None = None, symbol: str | None = None, from_id: str | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1MarginAllOrderListResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves all OCO for a specific margin account based on provided optional parameters

Weight(IP): 200

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_margin_account_s_all_oco_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginAllOrderListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAccountSAllOcoUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_margin_account_s_all_oco_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1MarginAllOrderListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAccountSAllOcoUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>is_isolated</code> | <code>[IsIsolatedOrStr](binance/models/enums/is_isolated.py) \| None</code> | * `TRUE` - For isolated margin<br>* `FALSE` - Default, not for isolated margin<br>**Default**: <code>None</code> |
| <code>symbol</code> | <code>str \| None</code> | Mandatory for isolated margin, not supported for cross margin<br>**Default**: <code>None</code> |
| <code>from_id</code> | <code>str \| None</code> | If supplied, neither `startTime` or `endTime` can be provided<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default Value: 500; Max Value: 1000<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1MarginAllOrderListResponse](binance/models/sapi_v1_margin_all_order_list_response.py)&#93;</code> -- List of Margin OCO orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryMarginAccountSAllOcoUserDataErrorBody](binance/errors/query_margin_account_s_all_oco_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_margin_available_inventory_user_data(type_: Type4OrStr, timestamp: int, signature: str, *, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginAvailableInventoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Margin available Inventory query

Weight(UID): 50

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_margin_available_inventory_user_data(type_, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginAvailableInventoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAvailableInventoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_margin_available_inventory_user_data(type_, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginAvailableInventoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginAvailableInventoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[Type4OrStr](binance/models/enums/type4.py)</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginAvailableInventoryResponse](binance/models/sapi_v1_margin_available_inventory_response.py)</code> -- Margin available Inventory

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryMarginAvailableInventoryUserDataErrorBody](binance/errors/query_margin_available_inventory_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_margin_price_index_market_data(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginPriceIndexResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_margin_price_index_market_data(symbol)
    # TODO: Handle 'response' of type SapiV1MarginPriceIndexResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginPriceIndexMarketDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_margin_price_index_market_data(symbol)
    # TODO: Handle 'response' of type SapiV1MarginPriceIndexResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMarginPriceIndexMarketDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginPriceIndexResponse](binance/models/sapi_v1_margin_price_index_response.py)</code> -- Price index

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryMarginPriceIndexMarketDataErrorBody](binance/errors/query_margin_price_index_market_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_max_borrow_user_data(asset: str, timestamp: int, signature: str, *, isolated_symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginMaxBorrowableResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If `isolatedSymbol` is not sent, crossed margin data will be sent.
- `borrowLimit` is also available from https://www.binance.com/en/margin-fee

Weight(IP): 50

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_max_borrow_user_data(asset, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginMaxBorrowableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMaxBorrowUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_max_borrow_user_data(asset, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginMaxBorrowableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMaxBorrowUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>isolated_symbol</code> | <code>str \| None</code> | Isolated symbol<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginMaxBorrowableResponse](binance/models/sapi_v1_margin_max_borrowable_response.py)</code> -- Details on max borrow amount

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryMaxBorrowUserDataErrorBody](binance/errors/query_max_borrow_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_max_transfer_out_amount_user_data(asset: str, timestamp: int, signature: str, *, isolated_symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginMaxTransferableResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If `isolatedSymbol` is not sent, crossed margin data will be sent.

Weight(IP): 50

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_max_transfer_out_amount_user_data(asset, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginMaxTransferableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMaxTransferOutAmountUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_max_transfer_out_amount_user_data(asset, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginMaxTransferableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMaxTransferOutAmountUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>isolated_symbol</code> | <code>str \| None</code> | Isolated symbol<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginMaxTransferableResponse](binance/models/sapi_v1_margin_max_transferable_response.py)</code> -- Details on max transferable amount

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryMaxTransferOutAmountUserDataErrorBody](binance/errors/query_max_transfer_out_amount_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_borrow_repay_records_in_margin_account_user_data(asset: str, type_: str, timestamp: int, signature: str, *, isolated_symbol: str | None = None, tx_id: int | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MarginBorrowRepayResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query borrow/repay records in Margin account

- txId or startTime must be sent. txId takes precedence. Response in descending order
- If an asset is sent, data within 30 days before endTime; If an asset is not sent, data within 7 days before endTime
- If neither startTime nor endTime is sent, the recent 7-day data will be returned.
- startTime set as endTime - 7 days by default, endTime set as current time by default

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.query_borrow_repay_records_in_margin_account_user_data(asset, type_, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MarginBorrowRepayResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryBorrowRepayRecordsInMarginAccountUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.query_borrow_repay_records_in_margin_account_user_data(
        asset, type_, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1MarginBorrowRepayResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryBorrowRepayRecordsInMarginAccountUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>type_</code> | <code>str</code> | BORROW or REPAY |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>isolated_symbol</code> | <code>str \| None</code> | Isolated symbol<br>**Default**: <code>None</code> |
| <code>tx_id</code> | <code>int \| None</code> | tranId in POST /sapi/v1/margin/loan<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MarginBorrowRepayResponse1](binance/models/sapi_v1_margin_borrow_repay_response1.py)</code> -- Margin account borrow/repay

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryBorrowRepayRecordsInMarginAccountUserDataErrorBody](binance/errors/query_borrow_repay_records_in_margin_account_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data(timestamp: int, signature: str, *, spot_bnb_burn: SpotBnbburnOrStr | None = None, interest_bnb_burn: InterestBnbburnOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> BnbBurnStatus</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- "spotBNBBurn" and "interestBNBBurn" should be sent at least one.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin.toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data(timestamp, signature)
    # TODO: Handle 'response' of type BnbBurnStatus
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ToggleBnbBurnOnSpotTradeAndMarginInterestUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.margin.toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data(
        timestamp, signature
    )
    # TODO: Handle 'response' of type BnbBurnStatus
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ToggleBnbBurnOnSpotTradeAndMarginInterestUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>spot_bnb_burn</code> | <code>[SpotBnbburnOrStr](binance/models/enums/spot_bnbburn.py) \| None</code> | Determines whether to use BNB to pay for trading fees on SPOT<br>**Default**: <code>None</code> |
| <code>interest_bnb_burn</code> | <code>[InterestBnbburnOrStr](binance/models/enums/interest_bnbburn.py) \| None</code> | Determines whether to use BNB to pay for margin loan's interest<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BnbBurnStatus](binance/models/bnb_burn_status.py)</code> -- Status on BNB to pay for trading fees

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[ToggleBnbBurnOnSpotTradeAndMarginInterestUserDataErrorBody](binance/errors/toggle_bnb_burn_on_spot_trade_and_margin_interest_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## MarginStream

> Source: [MarginStream](binance/apis/margin_stream.py)

<details>
<summary><code>def close_a_listen_key_user_stream_2(*, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Close out a user data stream.

Weight: 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin_stream.close_a_listen_key_user_stream_2()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CloseAListenKeyUserStream2ErrorBody
```

**Async**

```python
try:
    response = await async_client.margin_stream.close_a_listen_key_user_stream_2()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CloseAListenKeyUserStream2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>listen_key</code> | <code>str \| None</code> | User websocket listen key<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CloseAListenKeyUserStream2ErrorBody](binance/errors/close_a_listen_key_user_stream2_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_a_listen_key_user_stream_2(*, request_options: RequestOptionsOrDict | None = None) -> SapiV1UserDataStreamResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Start a new user data stream.
The stream will close after 60 minutes unless a keepalive is sent. If the account has an active `listenKey`, that `listenKey` will be returned and its validity will be extended for 60 minutes.

Weight: 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin_stream.create_a_listen_key_user_stream_2()
    # TODO: Handle 'response' of type SapiV1UserDataStreamResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.margin_stream.create_a_listen_key_user_stream_2()
    # TODO: Handle 'response' of type SapiV1UserDataStreamResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1UserDataStreamResponse](binance/models/sapi_v1_user_data_stream_response.py)</code> -- Margin listen key

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RawError](binance/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def ping_keep_alive_a_listen_key_user_stream_2(*, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 30 minutes.

Weight: 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.margin_stream.ping_keep_alive_a_listen_key_user_stream_2()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PingKeepAliveAListenKeyUserStream2ErrorBody
```

**Async**

```python
try:
    response = await async_client.margin_stream.ping_keep_alive_a_listen_key_user_stream_2()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PingKeepAliveAListenKeyUserStream2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>listen_key</code> | <code>str \| None</code> | User websocket listen key<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[PingKeepAliveAListenKeyUserStream2ErrorBody](binance/errors/ping_keep_alive_a_listen_key_user_stream2_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Market

> Source: [Market](binance/apis/market.py)

<details>
<summary><code>def hr_ticker_price_change_statistics24(*, symbol: str | None = None, symbols: str | None = None, type_: TypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiV3Ticker24HrResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

24 hour rolling window price change statistics. Careful when accessing this with no symbol.

- If the symbol is not sent, tickers for all symbols will be returned in an array.

Weight(IP):
- `2` for a single symbol;
- `80` when the symbol parameter is omitted;

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.hr_ticker_price_change_statistics24()
    # TODO: Handle 'response' of type ApiV3Ticker24HrResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type HrTickerPriceChangeStatistics24ErrorBody
```

**Async**

```python
try:
    response = await async_client.market.hr_ticker_price_change_statistics24()
    # TODO: Handle 'response' of type ApiV3Ticker24HrResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type HrTickerPriceChangeStatistics24ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Trading symbol, e.g. BNBUSDT<br>**Default**: <code>None</code> |
| <code>symbols</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>type_</code> | <code>[TypeOrStr](binance/models/enums/type.py) \| None</code> | Supported values: FULL or MINI.<br>If none provided, the default is FULL<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3Ticker24HrResponse](binance/models/unions/api_v3_ticker24_hr_response.py)</code> -- 24hr ticker

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[HrTickerPriceChangeStatistics24ErrorBody](binance/errors/hr_ticker_price_change_statistics24_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def check_server_time(*, request_options: RequestOptionsOrDict | None = None) -> ApiV3TimeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Test connectivity to the Rest API and get the current server time.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.check_server_time()
    # TODO: Handle 'response' of type ApiV3TimeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.market.check_server_time()
    # TODO: Handle 'response' of type ApiV3TimeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3TimeResponse](binance/models/api_v3_time_response.py)</code> -- Binance server UTC timestamp

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RawError](binance/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def compressed_aggregate_trades_list(symbol: str, *, from_id: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[AggTrade]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get compressed, aggregate trades. Trades that fill at the time, from the same order, with the same price will have the quantity aggregated.
- If `fromId`, `startTime`, and `endTime` are not sent, the most recent aggregate trades will be returned.
- Note that if a trade has the following values, this was a duplicate aggregate trade and marked as invalid:

p = '0' // price

  q = '0' // qty

  f = -1 // ﬁrst_trade_id

  l = -1 // last_trade_id

Weight(IP): 2

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.compressed_aggregate_trades_list(symbol)
    # TODO: Handle 'response' of type list[AggTrade]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CompressedAggregateTradesListErrorBody
```

**Async**

```python
try:
    response = await async_client.market.compressed_aggregate_trades_list(symbol)
    # TODO: Handle 'response' of type list[AggTrade]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CompressedAggregateTradesListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>from_id</code> | <code>int \| None</code> | Trade id to fetch from. Default gets most recent trades.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[AggTrade](binance/models/agg_trade.py)&#93;</code> -- Trade list

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CompressedAggregateTradesListErrorBody](binance/errors/compressed_aggregate_trades_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def current_average_price(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiV3AvgPriceResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Current average price for a symbol.

Weight(IP): 2

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.current_average_price(symbol)
    # TODO: Handle 'response' of type ApiV3AvgPriceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CurrentAveragePriceErrorBody
```

**Async**

```python
try:
    response = await async_client.market.current_average_price(symbol)
    # TODO: Handle 'response' of type ApiV3AvgPriceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CurrentAveragePriceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3AvgPriceResponse](binance/models/api_v3_avg_price_response.py)</code> -- Average price

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CurrentAveragePriceErrorBody](binance/errors/current_average_price_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def exchange_information(*, symbol: str | None = None, symbols: str | None = None, permissions: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiV3ExchangeInfoResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Current exchange trading rules and symbol information

- If any symbol provided in either symbol or symbols do not exist, the endpoint will throw an error.
- All parameters are optional.
- permissions can support single or multiple values (e.g. SPOT, ["MARGIN","LEVERAGED"])
- If permissions parameter not provided, the default values will be ["SPOT","MARGIN","LEVERAGED"].
  - To display all permissions you need to specify them explicitly. (e.g. SPOT, MARGIN,...)

Examples of Symbol Permissions Interpretation from the Response:
- [["A","B"]] means you may place an order if your account has either permission "A" or permission "B".
- [["A"],["B"]] means you can place an order if your account has permission "A" and permission "B".
- [["A"],["B","C"]] means you can place an order if your account has permission "A" and permission "B" or permission "C". (Inclusive or is applied here, not exclusive or, so your account may have both permission "B" and permission "C".)

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.exchange_information()
    # TODO: Handle 'response' of type ApiV3ExchangeInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExchangeInformationErrorBody
```

**Async**

```python
try:
    response = await async_client.market.exchange_information()
    # TODO: Handle 'response' of type ApiV3ExchangeInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExchangeInformationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Trading symbol, e.g. BNBUSDT<br>**Default**: <code>None</code> |
| <code>symbols</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>permissions</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3ExchangeInfoResponse](binance/models/api_v3_exchange_info_response.py)</code> -- Current exchange trading rules and symbol information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[ExchangeInformationErrorBody](binance/errors/exchange_information_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def kline_candlestick_data(symbol: str, interval: IntervalOrStr, *, start_time: int | None = None, end_time: int | None = None, time_zone: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[list[ApiV3KlinesResponse]]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Kline/candlestick bars for a symbol.
Klines are uniquely identified by their open time.

- If `startTime` and `endTime` are not sent, the most recent klines are returned.

Weight(IP): 2

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.kline_candlestick_data(symbol, interval)
    # TODO: Handle 'response' of type list[list[ApiV3KlinesResponse]]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type KlineCandlestickDataErrorBody
```

**Async**

```python
try:
    response = await async_client.market.kline_candlestick_data(symbol, interval)
    # TODO: Handle 'response' of type list[list[ApiV3KlinesResponse]]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type KlineCandlestickDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>interval</code> | <code>[IntervalOrStr](binance/models/enums/interval.py)</code> | kline intervals |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>time_zone</code> | <code>str \| None</code> | Default: 0 (UTC)<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;list&#91;[ApiV3KlinesResponse](binance/models/unions/api_v3_klines_response.py)&#93;&#93;</code> -- Kline data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[KlineCandlestickDataErrorBody](binance/errors/kline_candlestick_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def old_trade_lookup(symbol: str, *, limit: int | None = None, from_id: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[Trade]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get older market trades.

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.old_trade_lookup(symbol)
    # TODO: Handle 'response' of type list[Trade]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.market.old_trade_lookup(symbol)
    # TODO: Handle 'response' of type list[Trade]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>from_id</code> | <code>int \| None</code> | Trade id to fetch from. Default gets most recent trades.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[Trade](binance/models/trade.py)&#93;</code> -- Trade list

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RawError](binance/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def order_book(symbol: str, *, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None) -> ApiV3DepthResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

| Limit               | Weight(IP)  |
|---------------------|-------------|
| 1-100               | 5           |
| 101-500             | 25          |
| 501-1000            | 50          |
| 1001-5000           | 250         |

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.order_book(symbol)
    # TODO: Handle 'response' of type ApiV3DepthResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrderBookErrorBody
```

**Async**

```python
try:
    response = await async_client.market.order_book(symbol)
    # TODO: Handle 'response' of type ApiV3DepthResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrderBookErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>limit</code> | <code>int \| None</code> | If limit > 5000, then the response will truncate to 5000<br>**Default**: <code>100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3DepthResponse](binance/models/api_v3_depth_response.py)</code> -- Order book

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[OrderBookErrorBody](binance/errors/order_book_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def recent_trades_list(symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[Trade]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get recent trades.

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.recent_trades_list(symbol)
    # TODO: Handle 'response' of type list[Trade]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RecentTradesListErrorBody
```

**Async**

```python
try:
    response = await async_client.market.recent_trades_list(symbol)
    # TODO: Handle 'response' of type list[Trade]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RecentTradesListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[Trade](binance/models/trade.py)&#93;</code> -- Trade list

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RecentTradesListErrorBody](binance/errors/recent_trades_list_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def rolling_window_price_change_statistics(*, symbol: str | None = None, symbols: str | None = None, window_size: str | None = None, type_: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiV3TickerResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The window used to compute statistics is typically slightly wider than requested windowSize.

openTime for /api/v3/ticker always starts on a minute, while the closeTime is the current time of the request. As such, the effective window might be up to 1 minute wider than requested.

E.g. If the closeTime is 1641287867099 (January 04, 2022 09:17:47:099 UTC) , and the windowSize is 1d. the openTime will be: 1641201420000 (January 3, 2022, 09:17:00 UTC)

Weight(IP): 4 for each requested symbol regardless of windowSize.

The weight for this request will cap at 200 once the number of symbols in the request is more than 50.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.rolling_window_price_change_statistics()
    # TODO: Handle 'response' of type ApiV3TickerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RollingWindowPriceChangeStatisticsErrorBody
```

**Async**

```python
try:
    response = await async_client.market.rolling_window_price_change_statistics()
    # TODO: Handle 'response' of type ApiV3TickerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RollingWindowPriceChangeStatisticsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Trading symbol, e.g. BNBUSDT<br>**Default**: <code>None</code> |
| <code>symbols</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>window_size</code> | <code>str \| None</code> | Defaults to 1d if no parameter provided.<br>Supported windowSize values:<br>1m,2m....59m for minutes<br>1h, 2h....23h - for hours<br>1d...7d - for days.<br><br>Units cannot be combined (e.g. 1d2h is not allowed)<br>**Default**: <code>None</code> |
| <code>type_</code> | <code>str \| None</code> | Supported values: FULL or MINI.<br>If none provided, the default is FULL<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3TickerResponse](binance/models/api_v3_ticker_response.py)</code> -- Rolling price ticker

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RollingWindowPriceChangeStatisticsErrorBody](binance/errors/rolling_window_price_change_statistics_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def symbol_order_book_ticker(*, symbol: str | None = None, symbols: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiV3TickerBookTickerResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Best price/qty on the order book for a symbol or symbols.

- If the symbol is not sent, bookTickers for all symbols will be returned in an array.

Weight(IP):
- `2` for a single symbol;
- `4` when the symbol parameter is omitted;

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.symbol_order_book_ticker()
    # TODO: Handle 'response' of type ApiV3TickerBookTickerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SymbolOrderBookTickerErrorBody
```

**Async**

```python
try:
    response = await async_client.market.symbol_order_book_ticker()
    # TODO: Handle 'response' of type ApiV3TickerBookTickerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SymbolOrderBookTickerErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Trading symbol, e.g. BNBUSDT<br>**Default**: <code>None</code> |
| <code>symbols</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3TickerBookTickerResponse](binance/models/unions/api_v3_ticker_book_ticker_response.py)</code> -- Order book ticker

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SymbolOrderBookTickerErrorBody](binance/errors/symbol_order_book_ticker_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def symbol_price_ticker(*, symbol: str | None = None, symbols: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiV3TickerPriceResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Latest price for a symbol or symbols.

- If the symbol is not sent, prices for all symbols will be returned in an array.

Weight(IP):
- `2` for a single symbol;
- `4` when the symbol parameter is omitted;

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.symbol_price_ticker()
    # TODO: Handle 'response' of type ApiV3TickerPriceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SymbolPriceTickerErrorBody
```

**Async**

```python
try:
    response = await async_client.market.symbol_price_ticker()
    # TODO: Handle 'response' of type ApiV3TickerPriceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SymbolPriceTickerErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Trading symbol, e.g. BNBUSDT<br>**Default**: <code>None</code> |
| <code>symbols</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3TickerPriceResponse](binance/models/unions/api_v3_ticker_price_response.py)</code> -- Price ticker

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SymbolPriceTickerErrorBody](binance/errors/symbol_price_ticker_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def test_connectivity(*, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Test connectivity to the Rest API.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.test_connectivity()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.market.test_connectivity()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RawError](binance/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def trading_day_ticker(*, symbol: str | None = None, symbols: str | None = None, time_zone: str | None = None, type_: TypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiV3TickerTradingDayResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Price change statistics for a trading day.

Notes:
- Supported values for timeZone:
  - Hours and minutes (e.g. -1:00, 05:45)
  - Only hours (e.g. 0, 8, 4)

Weight:
- `4` for each requested symbol.
- The weight for this request will cap at `200` once the number of symbols in the request is more than `50`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.trading_day_ticker()
    # TODO: Handle 'response' of type ApiV3TickerTradingDayResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TradingDayTickerErrorBody
```

**Async**

```python
try:
    response = await async_client.market.trading_day_ticker()
    # TODO: Handle 'response' of type ApiV3TickerTradingDayResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TradingDayTickerErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Trading symbol, e.g. BNBUSDT<br>**Default**: <code>None</code> |
| <code>symbols</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>time_zone</code> | <code>str \| None</code> | Default: 0 (UTC)<br>**Default**: <code>None</code> |
| <code>type_</code> | <code>[TypeOrStr](binance/models/enums/type.py) \| None</code> | Supported values: FULL or MINI.<br>If none provided, the default is FULL<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3TickerTradingDayResponse](binance/models/unions/api_v3_ticker_trading_day_response.py)</code> -- Trading day ticker

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[TradingDayTickerErrorBody](binance/errors/trading_day_ticker_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def ui_klines(symbol: str, interval: IntervalOrStr, *, start_time: int | None = None, end_time: int | None = None, time_zone: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[list[ApiV3UiKlinesResponse]]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The request is similar to klines having the same parameters and response.

uiKlines return modified kline data, optimized for presentation of candlestick charts.

Weight(IP): 2

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.market.ui_klines(symbol, interval)
    # TODO: Handle 'response' of type list[list[ApiV3UiKlinesResponse]]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UiklinesErrorBody
```

**Async**

```python
try:
    response = await async_client.market.ui_klines(symbol, interval)
    # TODO: Handle 'response' of type list[list[ApiV3UiKlinesResponse]]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UiklinesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>interval</code> | <code>[IntervalOrStr](binance/models/enums/interval.py)</code> | kline intervals |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>time_zone</code> | <code>str \| None</code> | Default: 0 (UTC)<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;list&#91;[ApiV3UiKlinesResponse](binance/models/unions/api_v3_ui_klines_response.py)&#93;&#93;</code> -- UIKline data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[UiklinesErrorBody](binance/errors/uiklines_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Mining

> Source: [Mining](binance/apis/mining.py)

<details>
<summary><code>def account_list_user_data(algo: str, user_name: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MiningStatisticsUserListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 5

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.mining.account_list_user_data(algo, user_name, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningStatisticsUserListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AccountListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.mining.account_list_user_data(algo, user_name, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningStatisticsUserListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AccountListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>algo</code> | <code>str</code> | Algorithm(sha256) |
| <code>user_name</code> | <code>str</code> | Mining Account |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MiningStatisticsUserListResponse](binance/models/sapi_v1_mining_statistics_user_list_response.py)</code> -- List of mining accounts

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AccountListUserDataErrorBody](binance/errors/account_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def acquiring_algorithm_market_data(*, request_options: RequestOptionsOrDict | None = None) -> SapiV1MiningPubAlgoListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.mining.acquiring_algorithm_market_data()
    # TODO: Handle 'response' of type SapiV1MiningPubAlgoListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AcquiringAlgorithmMarketDataErrorBody
```

**Async**

```python
try:
    response = await async_client.mining.acquiring_algorithm_market_data()
    # TODO: Handle 'response' of type SapiV1MiningPubAlgoListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AcquiringAlgorithmMarketDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MiningPubAlgoListResponse](binance/models/sapi_v1_mining_pub_algo_list_response.py)</code> -- Algorithm information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AcquiringAlgorithmMarketDataErrorBody](binance/errors/acquiring_algorithm_market_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def acquiring_coin_name_market_data(*, request_options: RequestOptionsOrDict | None = None) -> SapiV1MiningPubCoinListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.mining.acquiring_coin_name_market_data()
    # TODO: Handle 'response' of type SapiV1MiningPubCoinListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AcquiringCoinNameMarketDataErrorBody
```

**Async**

```python
try:
    response = await async_client.mining.acquiring_coin_name_market_data()
    # TODO: Handle 'response' of type SapiV1MiningPubCoinListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AcquiringCoinNameMarketDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MiningPubCoinListResponse](binance/models/sapi_v1_mining_pub_coin_list_response.py)</code> -- Coin information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AcquiringCoinNameMarketDataErrorBody](binance/errors/acquiring_coin_name_market_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_hashrate_resale_configuration_user_data(config_id: str, user_name: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MiningHashTransferConfigCancelResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 5

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.mining.cancel_hashrate_resale_configuration_user_data(config_id, user_name, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningHashTransferConfigCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelHashrateResaleConfigurationUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.mining.cancel_hashrate_resale_configuration_user_data(
        config_id, user_name, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1MiningHashTransferConfigCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelHashrateResaleConfigurationUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>config_id</code> | <code>str</code> | Mining ID |
| <code>user_name</code> | <code>str</code> | Mining Account |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MiningHashTransferConfigCancelResponse](binance/models/sapi_v1_mining_hash_transfer_config_cancel_response.py)</code> -- Success flag

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CancelHashrateResaleConfigurationUserDataErrorBody](binance/errors/cancel_hashrate_resale_configuration_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def earnings_list_user_data(algo: str, user_name: str, timestamp: int, signature: str, *, coin: str | None = None, start_date: str | None = None, end_date: str | None = None, page_index: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MiningPaymentListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 5

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.mining.earnings_list_user_data(algo, user_name, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningPaymentListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EarningsListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.mining.earnings_list_user_data(algo, user_name, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningPaymentListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EarningsListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>algo</code> | <code>str</code> | Algorithm(sha256) |
| <code>user_name</code> | <code>str</code> | Mining Account |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>coin</code> | <code>str \| None</code> | Coin name<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>str \| None</code> | Search date, millisecond timestamp, while empty query all<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | Search date, millisecond timestamp, while empty query all<br>**Default**: <code>None</code> |
| <code>page_index</code> | <code>int \| None</code> | Page number, default is first page, start form 1<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>str \| None</code> | Number of pages, minimum 10, maximum 200<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MiningPaymentListResponse](binance/models/sapi_v1_mining_payment_list_response.py)</code> -- List of earnings

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[EarningsListUserDataErrorBody](binance/errors/earnings_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def extra_bonus_list_user_data(algo: str, user_name: str, timestamp: int, signature: str, *, coin: str | None = None, start_date: str | None = None, end_date: str | None = None, page_index: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MiningPaymentOtherResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 5

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.mining.extra_bonus_list_user_data(algo, user_name, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningPaymentOtherResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExtraBonusListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.mining.extra_bonus_list_user_data(algo, user_name, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningPaymentOtherResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExtraBonusListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>algo</code> | <code>str</code> | Algorithm(sha256) |
| <code>user_name</code> | <code>str</code> | Mining Account |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>coin</code> | <code>str \| None</code> | Coin name<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>str \| None</code> | Search date, millisecond timestamp, while empty query all<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | Search date, millisecond timestamp, while empty query all<br>**Default**: <code>None</code> |
| <code>page_index</code> | <code>int \| None</code> | Page number, default is first page, start form 1<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>str \| None</code> | Number of pages, minimum 10, maximum 200<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MiningPaymentOtherResponse](binance/models/sapi_v1_mining_payment_other_response.py)</code> -- List of extra bonuses

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[ExtraBonusListUserDataErrorBody](binance/errors/extra_bonus_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def hashrate_resale_details_user_data(config_id: str, user_name: str, timestamp: int, signature: str, *, page_index: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MiningHashTransferProfitDetailsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 5

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.mining.hashrate_resale_details_user_data(config_id, user_name, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningHashTransferProfitDetailsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type HashrateResaleDetailsUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.mining.hashrate_resale_details_user_data(config_id, user_name, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningHashTransferProfitDetailsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type HashrateResaleDetailsUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>config_id</code> | <code>str</code> | Mining ID |
| <code>user_name</code> | <code>str</code> | Mining Account |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>page_index</code> | <code>int \| None</code> | Page number, default is first page, start form 1<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>str \| None</code> | Number of pages, minimum 10, maximum 200<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MiningHashTransferProfitDetailsResponse](binance/models/sapi_v1_mining_hash_transfer_profit_details_response.py)</code> -- List of hashrate resale details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[HashrateResaleDetailsUserDataErrorBody](binance/errors/hashrate_resale_details_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def hashrate_resale_list_user_data(timestamp: int, signature: str, *, page_index: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MiningHashTransferConfigDetailsListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 5

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.mining.hashrate_resale_list_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningHashTransferConfigDetailsListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type HashrateResaleListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.mining.hashrate_resale_list_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningHashTransferConfigDetailsListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type HashrateResaleListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>page_index</code> | <code>int \| None</code> | Page number, default is first page, start form 1<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>str \| None</code> | Number of pages, minimum 10, maximum 200<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MiningHashTransferConfigDetailsListResponse](binance/models/sapi_v1_mining_hash_transfer_config_details_list_response.py)</code> -- List of hashrate resales

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[HashrateResaleListUserDataErrorBody](binance/errors/hashrate_resale_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def hashrate_resale_request_user_data(user_name: str, algo: str, to_pool_user: str, hash_rate: str, timestamp: int, signature: str, *, start_date: str | None = None, end_date: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MiningHashTransferConfigResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 5

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.mining.hashrate_resale_request_user_data(
        user_name, algo, to_pool_user, hash_rate, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1MiningHashTransferConfigResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type HashrateResaleRequestUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.mining.hashrate_resale_request_user_data(
        user_name, algo, to_pool_user, hash_rate, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1MiningHashTransferConfigResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type HashrateResaleRequestUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>user_name</code> | <code>str</code> | Mining Account |
| <code>algo</code> | <code>str</code> | Algorithm(sha256) |
| <code>to_pool_user</code> | <code>str</code> | Mining Account |
| <code>hash_rate</code> | <code>str</code> | Resale hashrate h/s must be transferred (BTC is greater than 500000000000 ETH is greater than 500000) |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_date</code> | <code>str \| None</code> | Search date, millisecond timestamp, while empty query all<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | Search date, millisecond timestamp, while empty query all<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MiningHashTransferConfigResponse](binance/models/sapi_v1_mining_hash_transfer_config_response.py)</code> -- Mining Account Id

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[HashrateResaleRequestUserDataErrorBody](binance/errors/hashrate_resale_request_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def mining_account_earning_user_data(algo: str, timestamp: int, signature: str, *, start_date: str | None = None, end_date: str | None = None, page_index: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MiningPaymentUidResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 5

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.mining.mining_account_earning_user_data(algo, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningPaymentUidResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MiningAccountEarningUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.mining.mining_account_earning_user_data(algo, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningPaymentUidResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MiningAccountEarningUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>algo</code> | <code>str</code> | Algorithm(sha256) |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_date</code> | <code>str \| None</code> | Search date, millisecond timestamp, while empty query all<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | Search date, millisecond timestamp, while empty query all<br>**Default**: <code>None</code> |
| <code>page_index</code> | <code>int \| None</code> | Page number, default is first page, start form 1<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>str \| None</code> | Number of pages, minimum 10, maximum 200<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MiningPaymentUidResponse](binance/models/sapi_v1_mining_payment_uid_response.py)</code> -- Mining account earnings

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[MiningAccountEarningUserDataErrorBody](binance/errors/mining_account_earning_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def request_for_detail_miner_list_user_data(algo: str, user_name: str, worker_name: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MiningWorkerDetailResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 5

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.mining.request_for_detail_miner_list_user_data(algo, user_name, worker_name, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningWorkerDetailResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RequestForDetailMinerListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.mining.request_for_detail_miner_list_user_data(
        algo, user_name, worker_name, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1MiningWorkerDetailResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RequestForDetailMinerListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>algo</code> | <code>str</code> | Algorithm(sha256) |
| <code>user_name</code> | <code>str</code> | Mining Account |
| <code>worker_name</code> | <code>str</code> | Miner’s name |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MiningWorkerDetailResponse](binance/models/sapi_v1_mining_worker_detail_response.py)</code> -- List of workers' hashrates'

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RequestForDetailMinerListUserDataErrorBody](binance/errors/request_for_detail_miner_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def request_for_miner_list_user_data(algo: str, user_name: str, timestamp: int, signature: str, *, page_index: int | None = None, sort: int | None = None, sort_column: int | None = None, worker_status: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MiningWorkerListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 5

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.mining.request_for_miner_list_user_data(algo, user_name, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningWorkerListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RequestForMinerListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.mining.request_for_miner_list_user_data(algo, user_name, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningWorkerListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RequestForMinerListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>algo</code> | <code>str</code> | Algorithm(sha256) |
| <code>user_name</code> | <code>str</code> | Mining Account |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>page_index</code> | <code>int \| None</code> | Page number, default is first page, start form 1<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>int \| None</code> | sort sequence(default=0)0 positive sequence, 1 negative sequence<br>**Default**: <code>None</code> |
| <code>sort_column</code> | <code>int \| None</code> | Sort by( default 1): 1: miner name, 2: real-time computing power, 3: daily average computing power, 4: real-time rejection rate, 5: last submission time<br>**Default**: <code>None</code> |
| <code>worker_status</code> | <code>int \| None</code> | miners status(default=0)0 all, 1 valid, 2 invalid, 3 failure<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MiningWorkerListResponse](binance/models/sapi_v1_mining_worker_list_response.py)</code> -- List of workers

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RequestForMinerListUserDataErrorBody](binance/errors/request_for_miner_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def statistic_list_user_data(algo: str, user_name: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1MiningStatisticsUserStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 5

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.mining.statistic_list_user_data(algo, user_name, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningStatisticsUserStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StatisticListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.mining.statistic_list_user_data(algo, user_name, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1MiningStatisticsUserStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StatisticListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>algo</code> | <code>str</code> | Algorithm(sha256) |
| <code>user_name</code> | <code>str</code> | Mining Account |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1MiningStatisticsUserStatusResponse](binance/models/sapi_v1_mining_statistics_user_status_response.py)</code> -- Mining account statistics

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[StatisticListUserDataErrorBody](binance/errors/statistic_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Nft

> Source: [Nft](binance/apis/nft.py)

<details>
<summary><code>def get_nft_asset_user_data(timestamp: int, signature: str, *, limit: int | None = None, page: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1NftUserGetAssetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.nft.get_nft_asset_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1NftUserGetAssetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetNftAssetUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.nft.get_nft_asset_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1NftUserGetAssetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetNftAssetUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>limit</code> | <code>int \| None</code> | Default 50, Max 50<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1NftUserGetAssetResponse](binance/models/sapi_v1_nft_user_get_asset_response.py)</code> -- Asset Information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetNftAssetUserDataErrorBody](binance/errors/get_nft_asset_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_nft_deposit_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, page: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1NftHistoryDepositResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- The max interval between startTime and endTime is 90 days.
- If startTime and endTime are not sent, the recent 7 days' data will be returned.

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.nft.get_nft_deposit_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1NftHistoryDepositResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetNftDepositHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.nft.get_nft_deposit_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1NftHistoryDepositResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetNftDepositHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 50, Max 50<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1NftHistoryDepositResponse](binance/models/sapi_v1_nft_history_deposit_response.py)</code> -- NFT Deposit History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetNftDepositHistoryUserDataErrorBody](binance/errors/get_nft_deposit_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_nft_transaction_history_user_data(order_type: int, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, page: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1NftHistoryTransactionsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- The max interval between startTime and endTime is 90 days.
- If startTime and endTime are not sent, the recent 7 days' data will be returned.

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.nft.get_nft_transaction_history_user_data(order_type, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1NftHistoryTransactionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetNftTransactionHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.nft.get_nft_transaction_history_user_data(order_type, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1NftHistoryTransactionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetNftTransactionHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_type</code> | <code>int</code> | 0: purchase order, 1: sell order, 2: royalty income, 3: primary market order, 4: mint fee |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 50, Max 50<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1NftHistoryTransactionsResponse](binance/models/sapi_v1_nft_history_transactions_response.py)</code> -- NFT Transaction History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetNftTransactionHistoryUserDataErrorBody](binance/errors/get_nft_transaction_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_nft_withdraw_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, page: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1NftHistoryWithdrawResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- The max interval between startTime and endTime is 90 days.
- If startTime and endTime are not sent, the recent 7 days' data will be returned.

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.nft.get_nft_withdraw_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1NftHistoryWithdrawResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetNftWithdrawHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.nft.get_nft_withdraw_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1NftHistoryWithdrawResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetNftWithdrawHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 50, Max 50<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1NftHistoryWithdrawResponse](binance/models/sapi_v1_nft_history_withdraw_response.py)</code> -- NFT Withdraw History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetNftWithdrawHistoryUserDataErrorBody](binance/errors/get_nft_withdraw_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Pay

> Source: [Pay](binance/apis/pay.py)

<details>
<summary><code>def get_pay_trade_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1PayTransactionsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If startTime and endTime are not sent, the recent 90 days' data will be returned.
- The max interval between startTime and endTime is 90 days.
- Support for querying orders within the last 18 months.

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.pay.get_pay_trade_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PayTransactionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPayTradeHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.pay.get_pay_trade_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PayTransactionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPayTradeHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | default 100, max 100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1PayTransactionsResponse](binance/models/sapi_v1_pay_transactions_response.py)</code> -- Pay History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetPayTradeHistoryUserDataErrorBody](binance/errors/get_pay_trade_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## PortfolioMargin

> Source: [PortfolioMargin](binance/apis/portfolio_margin.py)

<details>
<summary><code>def bnb_transfer_user_data(transfer_side: TransferSideOrStr, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1PortfolioBnbTransferResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

BNB transfer can be between Margin Account and USDM Account

Weight(IP): 1500

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.portfolio_margin.bnb_transfer_user_data(transfer_side, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioBnbTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BnbTransferUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.portfolio_margin.bnb_transfer_user_data(transfer_side, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioBnbTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BnbTransferUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>transfer_side</code> | <code>[TransferSideOrStr](binance/models/enums/transfer_side.py)</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1PortfolioBnbTransferResponse](binance/models/sapi_v1_portfolio_bnb_transfer_response.py)</code> -- Result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[BnbTransferUserDataErrorBody](binance/errors/bnb_transfer_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def change_auto_repay_futures_status_user_data(auto_repay: bool, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1PortfolioRepayFuturesSwitchResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Change Auto-repay-futures Status

Weight(IP): 1500

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.portfolio_margin.change_auto_repay_futures_status_user_data(auto_repay, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioRepayFuturesSwitchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangeAutoRepayFuturesStatusUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.portfolio_margin.change_auto_repay_futures_status_user_data(
        auto_repay, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1PortfolioRepayFuturesSwitchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangeAutoRepayFuturesStatusUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>auto_repay</code> | <code>bool</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1PortfolioRepayFuturesSwitchResponse](binance/models/sapi_v1_portfolio_repay_futures_switch_response.py)</code> -- Result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[ChangeAutoRepayFuturesStatusUserDataErrorBody](binance/errors/change_auto_repay_futures_status_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fund_auto_collection_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1PortfolioAutoCollectionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Transfers all assets from Futures Account to Margin account

Weight(IP): 1500

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.portfolio_margin.fund_auto_collection_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioAutoCollectionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FundAutoCollectionUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.portfolio_margin.fund_auto_collection_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioAutoCollectionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FundAutoCollectionUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1PortfolioAutoCollectionResponse](binance/models/sapi_v1_portfolio_auto_collection_response.py)</code> -- Result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[FundAutoCollectionUserDataErrorBody](binance/errors/fund_auto_collection_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fund_collection_by_asset_user_data(asset: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1PortfolioAssetCollectionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Transfers specific asset from Futures Account to Margin account

Weight(IP): 60

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.portfolio_margin.fund_collection_by_asset_user_data(asset, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioAssetCollectionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FundCollectionByAssetUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.portfolio_margin.fund_collection_by_asset_user_data(asset, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioAssetCollectionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FundCollectionByAssetUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1PortfolioAssetCollectionResponse](binance/models/sapi_v1_portfolio_asset_collection_response.py)</code> -- Result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[FundCollectionByAssetUserDataErrorBody](binance/errors/fund_collection_by_asset_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_auto_repay_futures_status_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1PortfolioRepayFuturesSwitchResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query Auto-repay-futures Status

Weight(IP): 30

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.portfolio_margin.get_auto_repay_futures_status_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioRepayFuturesSwitchResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAutoRepayFuturesStatusUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.portfolio_margin.get_auto_repay_futures_status_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioRepayFuturesSwitchResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAutoRepayFuturesStatusUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1PortfolioRepayFuturesSwitchResponse1](binance/models/sapi_v1_portfolio_repay_futures_switch_response1.py)</code> -- Result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetAutoRepayFuturesStatusUserDataErrorBody](binance/errors/get_auto_repay_futures_status_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_portfolio_margin_asset_leverage_user_data(*, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1PortfolioMarginAssetLeverageResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 50

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.portfolio_margin.get_portfolio_margin_asset_leverage_user_data()
    # TODO: Handle 'response' of type list[SapiV1PortfolioMarginAssetLeverageResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPortfolioMarginAssetLeverageUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.portfolio_margin.get_portfolio_margin_asset_leverage_user_data()
    # TODO: Handle 'response' of type list[SapiV1PortfolioMarginAssetLeverageResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPortfolioMarginAssetLeverageUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1PortfolioMarginAssetLeverageResponse](binance/models/sapi_v1_portfolio_margin_asset_leverage_response.py)&#93;</code> -- Classic Portfolio Margin Collateral Rate

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetPortfolioMarginAssetLeverageUserDataErrorBody](binance/errors/get_portfolio_margin_asset_leverage_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def portfolio_margin_account_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1PortfolioAccountResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the account info

'Weight(IP): 1'

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.portfolio_margin.portfolio_margin_account_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PortfolioMarginAccountUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.portfolio_margin.portfolio_margin_account_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PortfolioMarginAccountUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1PortfolioAccountResponse](binance/models/sapi_v1_portfolio_account_response.py)</code> -- Portfolio account.

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[PortfolioMarginAccountUserDataErrorBody](binance/errors/portfolio_margin_account_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def portfolio_margin_bankruptcy_loan_amount_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1PortfolioPmLoanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query Portfolio Margin Bankruptcy Loan Amount.

Weight(UID): 500

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.portfolio_margin.portfolio_margin_bankruptcy_loan_amount_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioPmLoanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PortfolioMarginBankruptcyLoanAmountUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.portfolio_margin.portfolio_margin_bankruptcy_loan_amount_user_data(
        timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1PortfolioPmLoanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PortfolioMarginBankruptcyLoanAmountUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1PortfolioPmLoanResponse](binance/models/sapi_v1_portfolio_pm_loan_response.py)</code> -- Portfolio Margin Bankruptcy Loan Amount.

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[PortfolioMarginBankruptcyLoanAmountUserDataErrorBody](binance/errors/portfolio_margin_bankruptcy_loan_amount_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def portfolio_margin_bankruptcy_loan_repay_user_data(timestamp: int, signature: str, *, from_: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1PortfolioRepayResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Repay Portfolio Margin Bankruptcy Loan.

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.portfolio_margin.portfolio_margin_bankruptcy_loan_repay_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioRepayResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PortfolioMarginBankruptcyLoanRepayUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.portfolio_margin.portfolio_margin_bankruptcy_loan_repay_user_data(
        timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1PortfolioRepayResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PortfolioMarginBankruptcyLoanRepayUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>from_</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1PortfolioRepayResponse](binance/models/sapi_v1_portfolio_repay_response.py)</code> -- Transaction.

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[PortfolioMarginBankruptcyLoanRepayUserDataErrorBody](binance/errors/portfolio_margin_bankruptcy_loan_repay_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def portfolio_margin_collateral_rate_market_data(*, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1PortfolioCollateralRateResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Portfolio Margin Collateral Rate.

Weight(IP): 50

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.portfolio_margin.portfolio_margin_collateral_rate_market_data()
    # TODO: Handle 'response' of type list[SapiV1PortfolioCollateralRateResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PortfolioMarginCollateralRateMarketDataErrorBody
```

**Async**

```python
try:
    response = await async_client.portfolio_margin.portfolio_margin_collateral_rate_market_data()
    # TODO: Handle 'response' of type list[SapiV1PortfolioCollateralRateResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PortfolioMarginCollateralRateMarketDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1PortfolioCollateralRateResponse](binance/models/sapi_v1_portfolio_collateral_rate_response.py)&#93;</code> -- Portfolio Margin Collateral Rate.

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[PortfolioMarginCollateralRateMarketDataErrorBody](binance/errors/portfolio_margin_collateral_rate_market_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def portfolio_margin_pro_tiered_collateral_rate_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV2PortfolioCollateralRateResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Portfolio Margin PRO Tiered Collateral Rate

Weight(IP): 50

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.portfolio_margin.portfolio_margin_pro_tiered_collateral_rate_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV2PortfolioCollateralRateResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PortfolioMarginProTieredCollateralRateUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.portfolio_margin.portfolio_margin_pro_tiered_collateral_rate_user_data(
        timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV2PortfolioCollateralRateResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PortfolioMarginProTieredCollateralRateUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV2PortfolioCollateralRateResponse](binance/models/sapi_v2_portfolio_collateral_rate_response.py)&#93;</code> -- Portfolio Margin Collateral Rate.

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[PortfolioMarginProTieredCollateralRateUserDataErrorBody](binance/errors/portfolio_margin_pro_tiered_collateral_rate_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_classic_portfolio_margin_negative_balance_interest_history_user_data(asset: str, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1PortfolioInterestHistoryResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query interest history of negative balance for portfolio margin.

Weight(IP): 50

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.portfolio_margin.query_classic_portfolio_margin_negative_balance_interest_history_user_data(
        asset, timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1PortfolioInterestHistoryResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryClassicPortfolioMarginNegativeBalanceInterestHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.portfolio_margin.query_classic_portfolio_margin_negative_balance_interest_history_user_data(
        asset, timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1PortfolioInterestHistoryResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryClassicPortfolioMarginNegativeBalanceInterestHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1PortfolioInterestHistoryResponse](binance/models/sapi_v1_portfolio_interest_history_response.py)&#93;</code> -- Balance interest history

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryClassicPortfolioMarginNegativeBalanceInterestHistoryUserDataErrorBody](binance/errors/query_classic_portfolio_margin_negative_balance_interest_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_portfolio_margin_asset_index_price_market_data(*, asset: str | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1PortfolioAssetIndexPriceResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query Portfolio Margin Asset Index Price

Weight(IP):
- 1 if send asset
- 50 if not send asset

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.portfolio_margin.query_portfolio_margin_asset_index_price_market_data()
    # TODO: Handle 'response' of type list[SapiV1PortfolioAssetIndexPriceResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryPortfolioMarginAssetIndexPriceMarketDataErrorBody
```

**Async**

```python
try:
    response = await async_client.portfolio_margin.query_portfolio_margin_asset_index_price_market_data()
    # TODO: Handle 'response' of type list[SapiV1PortfolioAssetIndexPriceResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryPortfolioMarginAssetIndexPriceMarketDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1PortfolioAssetIndexPriceResponse](binance/models/sapi_v1_portfolio_asset_index_price_response.py)&#93;</code> -- asset price index

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryPortfolioMarginAssetIndexPriceMarketDataErrorBody](binance/errors/query_portfolio_margin_asset_index_price_market_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def repay_futures_negative_balance_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1PortfolioRepayFuturesNegativeBalanceResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Repay futures Negative Balance

Weight(IP): 1500

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.portfolio_margin.repay_futures_negative_balance_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioRepayFuturesNegativeBalanceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RepayFuturesNegativeBalanceUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.portfolio_margin.repay_futures_negative_balance_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1PortfolioRepayFuturesNegativeBalanceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RepayFuturesNegativeBalanceUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1PortfolioRepayFuturesNegativeBalanceResponse](binance/models/sapi_v1_portfolio_repay_futures_negative_balance_response.py)</code> -- Result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RepayFuturesNegativeBalanceUserDataErrorBody](binance/errors/repay_futures_negative_balance_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Rebate

> Source: [Rebate](binance/apis/rebate.py)

<details>
<summary><code>def get_spot_rebate_history_records_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, page: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1RebateTaxQueryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- The max interval between startTime and endTime is 90 days.
- If startTime and endTime are not sent, the recent 7 days' data will be returned.
- The earliest startTime is supported on June 10, 2020

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.rebate.get_spot_rebate_history_records_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1RebateTaxQueryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSpotRebateHistoryRecordsUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.rebate.get_spot_rebate_history_records_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1RebateTaxQueryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSpotRebateHistoryRecordsUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | default 1<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1RebateTaxQueryResponse](binance/models/sapi_v1_rebate_tax_query_response.py)</code> -- Rebate History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetSpotRebateHistoryRecordsUserDataErrorBody](binance/errors/get_spot_rebate_history_records_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Savings

> Source: [Savings](binance/apis/savings.py)

<details>
<summary><code>def change_fixed_activity_position_to_daily_position_user_data(project_id: str, lot: str, timestamp: int, signature: str, *, position_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingPositionChangedResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- PositionId is mandatory parameter for fixed position.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.savings.change_fixed_activity_position_to_daily_position_user_data(
        project_id, lot, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LendingPositionChangedResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangeFixedActivityPositionToDailyPositionUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.savings.change_fixed_activity_position_to_daily_position_user_data(
        project_id, lot, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LendingPositionChangedResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangeFixedActivityPositionToDailyPositionUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | Value sent with the request. |
| <code>lot</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>position_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingPositionChangedResponse](binance/models/sapi_v1_lending_position_changed_response.py)</code> -- Purchase information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[ChangeFixedActivityPositionToDailyPositionUserDataErrorBody](binance/errors/change_fixed_activity_position_to_daily_position_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_fixed_activity_project_list_user_data(type_: Type8OrStr, timestamp: int, signature: str, *, asset: str | None = None, status: StatusOrStr | None = None, is_sort_asc: bool | None = None, sort_by: SortByOrStr | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1LendingProjectListResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.savings.get_fixed_activity_project_list_user_data(type_, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1LendingProjectListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFixedActivityProjectListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.savings.get_fixed_activity_project_list_user_data(type_, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1LendingProjectListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFixedActivityProjectListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[Type8OrStr](binance/models/enums/type8.py)</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[StatusOrStr](binance/models/enums/status.py) \| None</code> | Default `ALL`<br>**Default**: <code>None</code> |
| <code>is_sort_asc</code> | <code>bool \| None</code> | default "true"<br>**Default**: <code>None</code> |
| <code>sort_by</code> | <code>[SortByOrStr](binance/models/enums/sort_by.py) \| None</code> | Default `START_TIME`<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1LendingProjectListResponse](binance/models/sapi_v1_lending_project_list_response.py)&#93;</code> -- List of fixed projects

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetFixedActivityProjectListUserDataErrorBody](binance/errors/get_fixed_activity_project_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_fixed_activity_project_position_user_data(asset: str, timestamp: int, signature: str, *, project_id: str | None = None, status: StatusOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1LendingProjectPositionListResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.savings.get_fixed_activity_project_position_user_data(asset, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1LendingProjectPositionListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFixedActivityProjectPositionUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.savings.get_fixed_activity_project_position_user_data(asset, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1LendingProjectPositionListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFixedActivityProjectPositionUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>project_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[StatusOrStr](binance/models/enums/status.py) \| None</code> | Default `ALL`<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1LendingProjectPositionListResponse](binance/models/sapi_v1_lending_project_position_list_response.py)&#93;</code> -- List of fixed project positions

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetFixedActivityProjectPositionUserDataErrorBody](binance/errors/get_fixed_activity_project_position_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def purchase_fixed_activity_project_user_data(project_id: str, lot: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LendingCustomizedFixedPurchaseResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.savings.purchase_fixed_activity_project_user_data(project_id, lot, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LendingCustomizedFixedPurchaseResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PurchaseFixedActivityProjectUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.savings.purchase_fixed_activity_project_user_data(
        project_id, lot, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LendingCustomizedFixedPurchaseResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PurchaseFixedActivityProjectUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | Value sent with the request. |
| <code>lot</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LendingCustomizedFixedPurchaseResponse](binance/models/sapi_v1_lending_customized_fixed_purchase_response.py)</code> -- Generated Purchase Id

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[PurchaseFixedActivityProjectUserDataErrorBody](binance/errors/purchase_fixed_activity_project_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SimpleEarn

> Source: [SimpleEarn](binance/apis/simple_earn.py)

<details>
<summary><code>def get_collateral_record_user_data(timestamp: int, signature: str, *, product_id: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_collateral_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCollateralRecordUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_collateral_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCollateralRecordUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>product_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnFlexibleHistoryCollateralRecordResponse](binance/models/sapi_v1_simple_earn_flexible_history_collateral_record_response.py)</code> -- Collateral Record

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetCollateralRecordUserDataErrorBody](binance/errors/get_collateral_record_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_flexible_personal_left_quota_user_data(product_id: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_flexible_personal_left_quota_user_data(product_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexiblePersonalLeftQuotaUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_flexible_personal_left_quota_user_data(
        product_id, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexiblePersonalLeftQuotaUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnFlexiblePersonalLeftQuotaResponse](binance/models/sapi_v1_simple_earn_flexible_personal_left_quota_response.py)</code> -- Flexible Personal Left Quota

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetFlexiblePersonalLeftQuotaUserDataErrorBody](binance/errors/get_flexible_personal_left_quota_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_flexible_product_position_user_data(timestamp: int, signature: str, *, asset: str | None = None, product_id: str | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnFlexiblePositionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_flexible_product_position_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexiblePositionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexibleProductPositionUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_flexible_product_position_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexiblePositionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexibleProductPositionUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>product_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnFlexiblePositionResponse](binance/models/sapi_v1_simple_earn_flexible_position_response.py)</code> -- Flexible Product Position

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetFlexibleProductPositionUserDataErrorBody](binance/errors/get_flexible_product_position_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_flexible_redemption_record_user_data(*, product_id: str | None = None, redeem_id: str | None = None, asset: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_flexible_redemption_record_user_data()
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexibleRedemptionRecordUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_flexible_redemption_record_user_data()
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexibleRedemptionRecordUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>redeem_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnFlexibleHistoryRedemptionRecordResponse](binance/models/sapi_v1_simple_earn_flexible_history_redemption_record_response.py)</code> -- Flexible Redemption Record

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetFlexibleRedemptionRecordUserDataErrorBody](binance/errors/get_flexible_redemption_record_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_flexible_rewards_history_user_data(type_: str, *, product_id: str | None = None, asset: str | None = None, start_time: int | None = None, end_time: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_flexible_rewards_history_user_data(type_)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexibleRewardsHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_flexible_rewards_history_user_data(type_)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexibleRewardsHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>str</code> | "BONUS", "REALTIME", "REWARDS" |
| <code>product_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnFlexibleHistoryRewardsRecordResponse](binance/models/sapi_v1_simple_earn_flexible_history_rewards_record_response.py)</code> -- Flexible Rewards History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetFlexibleRewardsHistoryUserDataErrorBody](binance/errors/get_flexible_rewards_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_flexible_subscription_preview_user_data(product_id: str, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_flexible_subscription_preview_user_data(product_id, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexibleSubscriptionPreviewUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_flexible_subscription_preview_user_data(
        product_id, amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexibleSubscriptionPreviewUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnFlexibleSubscriptionPreviewResponse](binance/models/sapi_v1_simple_earn_flexible_subscription_preview_response.py)</code> -- Flexible Subscription Preview

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetFlexibleSubscriptionPreviewUserDataErrorBody](binance/errors/get_flexible_subscription_preview_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_flexible_subscription_record_user_data(timestamp: int, signature: str, *, product_id: str | None = None, purchase_id: str | None = None, asset: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_flexible_subscription_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexibleSubscriptionRecordUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_flexible_subscription_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFlexibleSubscriptionRecordUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>product_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>purchase_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnFlexibleHistorySubscriptionRecordResponse](binance/models/sapi_v1_simple_earn_flexible_history_subscription_record_response.py)</code> -- Flexible Product Position

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetFlexibleSubscriptionRecordUserDataErrorBody](binance/errors/get_flexible_subscription_record_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_locked_personal_left_quota_user_data(project_id: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnLockedPersonalLeftQuotaResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_locked_personal_left_quota_user_data(project_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedPersonalLeftQuotaResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLockedPersonalLeftQuotaUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_locked_personal_left_quota_user_data(project_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedPersonalLeftQuotaResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLockedPersonalLeftQuotaUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnLockedPersonalLeftQuotaResponse](binance/models/sapi_v1_simple_earn_locked_personal_left_quota_response.py)</code> -- Locked Personal Left Quota

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetLockedPersonalLeftQuotaUserDataErrorBody](binance/errors/get_locked_personal_left_quota_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_locked_product_position_user_data(timestamp: int, signature: str, *, asset: str | None = None, position_id: str | None = None, project_id: str | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnLockedPositionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_locked_product_position_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedPositionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLockedProductPositionUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_locked_product_position_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedPositionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLockedProductPositionUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>position_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>project_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnLockedPositionResponse](binance/models/sapi_v1_simple_earn_locked_position_response.py)</code> -- Locked Product Position

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetLockedProductPositionUserDataErrorBody](binance/errors/get_locked_product_position_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_locked_redemption_record_user_data(timestamp: int, signature: str, *, position_id: str | None = None, redeem_id: str | None = None, asset: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_locked_redemption_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLockedRedemptionRecordUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_locked_redemption_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLockedRedemptionRecordUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>position_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>redeem_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnLockedHistoryRedemptionRecordResponse](binance/models/sapi_v1_simple_earn_locked_history_redemption_record_response.py)</code> -- Locked Redemption Record

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetLockedRedemptionRecordUserDataErrorBody](binance/errors/get_locked_redemption_record_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_locked_rewards_history_user_data(timestamp: int, signature: str, *, position_id: str | None = None, asset: str | None = None, start_time: int | None = None, end_time: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnLockedHistoryRewardsRecordResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_locked_rewards_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedHistoryRewardsRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLockedRewardsHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_locked_rewards_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedHistoryRewardsRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLockedRewardsHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>position_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnLockedHistoryRewardsRecordResponse](binance/models/sapi_v1_simple_earn_locked_history_rewards_record_response.py)</code> -- Locked Rewards History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetLockedRewardsHistoryUserDataErrorBody](binance/errors/get_locked_rewards_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_locked_subscription_preview_user_data(project_id: str, amount: float, timestamp: int, signature: str, *, auto_subscribe: bool | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1SimpleEarnLockedSubscriptionPreviewResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_locked_subscription_preview_user_data(project_id, amount, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1SimpleEarnLockedSubscriptionPreviewResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLockedSubscriptionPreviewUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_locked_subscription_preview_user_data(
        project_id, amount, timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1SimpleEarnLockedSubscriptionPreviewResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLockedSubscriptionPreviewUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>auto_subscribe</code> | <code>bool \| None</code> | true or false, default true.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1SimpleEarnLockedSubscriptionPreviewResponse](binance/models/sapi_v1_simple_earn_locked_subscription_preview_response.py)&#93;</code> -- Locked Product Subscription Response

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetLockedSubscriptionPreviewUserDataErrorBody](binance/errors/get_locked_subscription_preview_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_locked_subscription_record_user_data(timestamp: int, signature: str, *, purchase_id: str | None = None, asset: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_locked_subscription_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLockedSubscriptionRecordUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_locked_subscription_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLockedSubscriptionRecordUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>purchase_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnLockedHistorySubscriptionRecordResponse](binance/models/sapi_v1_simple_earn_locked_history_subscription_record_response.py)</code> -- Locked Subscription Record

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetLockedSubscriptionRecordUserDataErrorBody](binance/errors/get_locked_subscription_record_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_rate_history_user_data(product_id: str, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_rate_history_user_data(product_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRateHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_rate_history_user_data(product_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRateHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnFlexibleHistoryRateHistoryResponse](binance/models/sapi_v1_simple_earn_flexible_history_rate_history_response.py)</code> -- Rate History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetRateHistoryUserDataErrorBody](binance/errors/get_rate_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_simple_earn_flexible_product_list_user_data(timestamp: int, signature: str, *, asset: str | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnFlexibleListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get available Simple Earn flexible product list

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_simple_earn_flexible_product_list_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSimpleEarnFlexibleProductListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_simple_earn_flexible_product_list_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSimpleEarnFlexibleProductListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnFlexibleListResponse](binance/models/sapi_v1_simple_earn_flexible_list_response.py)</code> -- Simple Earn Flexible Product List

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetSimpleEarnFlexibleProductListUserDataErrorBody](binance/errors/get_simple_earn_flexible_product_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_simple_earn_locked_product_list_user_data(timestamp: int, signature: str, *, asset: str | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnLockedListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.get_simple_earn_locked_product_list_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSimpleEarnLockedProductListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.get_simple_earn_locked_product_list_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSimpleEarnLockedProductListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnLockedListResponse](binance/models/sapi_v1_simple_earn_locked_list_response.py)</code> -- Simple Earn Locked Product List

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetSimpleEarnLockedProductListUserDataErrorBody](binance/errors/get_simple_earn_locked_product_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def redeem_flexible_product_trade(product_id: str, timestamp: int, signature: str, *, redeem_all: bool | None = None, amount: float | None = None, dest_account: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnFlexibleRedeemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

Rate Limit: 1/3s per account

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.redeem_flexible_product_trade(product_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleRedeemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RedeemFlexibleProductTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.redeem_flexible_product_trade(product_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleRedeemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RedeemFlexibleProductTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>redeem_all</code> | <code>bool \| None</code> | true or false, default to false<br>**Default**: <code>None</code> |
| <code>amount</code> | <code>float \| None</code> | if redeemAll is false, amount is mandatory<br>**Default**: <code>None</code> |
| <code>dest_account</code> | <code>str \| None</code> | SPOT,FUND,ALL, default SPOT<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnFlexibleRedeemResponse](binance/models/sapi_v1_simple_earn_flexible_redeem_response.py)</code> -- Redeem Flexible Product

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RedeemFlexibleProductTradeErrorBody](binance/errors/redeem_flexible_product_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def redeem_locked_product_trade(position_id: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnLockedRedeemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

Rate Limit: 1/3s per account

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.redeem_locked_product_trade(position_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedRedeemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RedeemLockedProductTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.redeem_locked_product_trade(position_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedRedeemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RedeemLockedProductTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>position_id</code> | <code>str</code> | 1234 |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnLockedRedeemResponse](binance/models/sapi_v1_simple_earn_locked_redeem_response.py)</code> -- Redeem Locked Product

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RedeemLockedProductTradeErrorBody](binance/errors/redeem_locked_product_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_flexible_auto_subscribe_user_data(product_id: str, auto_subscribe: bool, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.set_flexible_auto_subscribe_user_data(
        product_id, auto_subscribe, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetFlexibleAutoSubscribeUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.set_flexible_auto_subscribe_user_data(
        product_id, auto_subscribe, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetFlexibleAutoSubscribeUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>str</code> | Value sent with the request. |
| <code>auto_subscribe</code> | <code>bool</code> | true or false |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnFlexibleSetAutoSubscribeResponse](binance/models/sapi_v1_simple_earn_flexible_set_auto_subscribe_response.py)</code> -- Flexible Product Subscription Response

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SetFlexibleAutoSubscribeUserDataErrorBody](binance/errors/set_flexible_auto_subscribe_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_locked_auto_subscribe_user_data(position_id: str, auto_subscribe: bool, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnLockedSetAutoSubscribeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.set_locked_auto_subscribe_user_data(position_id, auto_subscribe, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedSetAutoSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetLockedAutoSubscribeUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.set_locked_auto_subscribe_user_data(
        position_id, auto_subscribe, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedSetAutoSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetLockedAutoSubscribeUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>position_id</code> | <code>str</code> | Value sent with the request. |
| <code>auto_subscribe</code> | <code>bool</code> | true or false |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnLockedSetAutoSubscribeResponse](binance/models/sapi_v1_simple_earn_locked_set_auto_subscribe_response.py)</code> -- Locked Auto Subscribe

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SetLockedAutoSubscribeUserDataErrorBody](binance/errors/set_locked_auto_subscribe_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_locked_product_redeem_option_user_data(position_id: str, timestamp: int, signature: str, *, redeem_to: RedeemToOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnLockedSetRedeemOptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set redeem option for Locked product

Weight(IP): 50

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.set_locked_product_redeem_option_user_data(position_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedSetRedeemOptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetLockedProductRedeemOptionUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.set_locked_product_redeem_option_user_data(
        position_id, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedSetRedeemOptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetLockedProductRedeemOptionUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>position_id</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>redeem_to</code> | <code>[RedeemToOrStr](binance/models/enums/redeem_to.py) \| None</code> | SPOT,FLEXIBLE, default FLEXIBLE<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnLockedSetRedeemOptionResponse](binance/models/sapi_v1_simple_earn_locked_set_redeem_option_response.py)</code> -- Locked Product Redeem Option

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SetLockedProductRedeemOptionUserDataErrorBody](binance/errors/set_locked_product_redeem_option_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def simple_account_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnAccountResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.simple_account_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SimpleAccountUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.simple_account_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SimpleAccountUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnAccountResponse](binance/models/sapi_v1_simple_earn_account_response.py)</code> -- Account Information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SimpleAccountUserDataErrorBody](binance/errors/simple_account_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def subscribe_flexible_product_trade(product_id: str, amount: float, timestamp: int, signature: str, *, auto_subscribe: bool | None = None, source_account: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnFlexibleSubscribeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

Rate Limit: 1/3s per account

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.subscribe_flexible_product_trade(product_id, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubscribeFlexibleProductTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.subscribe_flexible_product_trade(product_id, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnFlexibleSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubscribeFlexibleProductTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>auto_subscribe</code> | <code>bool \| None</code> | true or false, default true.<br>**Default**: <code>None</code> |
| <code>source_account</code> | <code>str \| None</code> | SPOT,FUND,ALL, default SPOT<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnFlexibleSubscribeResponse](binance/models/sapi_v1_simple_earn_flexible_subscribe_response.py)</code> -- Flexible Product Subscription Response

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SubscribeFlexibleProductTradeErrorBody](binance/errors/subscribe_flexible_product_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def subscribe_locked_product_trade(project_id: str, amount: float, timestamp: int, signature: str, *, auto_subscribe: bool | None = None, source_account: str | None = None, redeem_to: RedeemToOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SimpleEarnLockedSubscribeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

Rate Limit: 1/3s per account

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_earn.subscribe_locked_product_trade(project_id, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubscribeLockedProductTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.simple_earn.subscribe_locked_product_trade(project_id, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SimpleEarnLockedSubscribeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubscribeLockedProductTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>auto_subscribe</code> | <code>bool \| None</code> | true or false, default true.<br>**Default**: <code>None</code> |
| <code>source_account</code> | <code>str \| None</code> | SPOT,FUND,ALL, default SPOT<br>**Default**: <code>None</code> |
| <code>redeem_to</code> | <code>[RedeemToOrStr](binance/models/enums/redeem_to.py) \| None</code> | SPOT,FLEXIBLE, default FLEXIBLE<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SimpleEarnLockedSubscribeResponse](binance/models/sapi_v1_simple_earn_locked_subscribe_response.py)</code> -- Locked Product Subscription Response

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SubscribeLockedProductTradeErrorBody](binance/errors/subscribe_locked_product_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SpotAlgo

> Source: [SpotAlgo](binance/apis/spot_algo.py)

<details>
<summary><code>def cancel_algo_order(algo_id: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AlgoSpotOrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancel an open TWAP order

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.spot_algo.cancel_algo_order(algo_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoSpotOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelAlgoOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.spot_algo.cancel_algo_order(algo_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoSpotOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelAlgoOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>algo_id</code> | <code>int</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AlgoSpotOrderResponse](binance/models/sapi_v1_algo_spot_order_response.py)</code> -- Cancelled twap order response

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CancelAlgoOrderErrorBody](binance/errors/cancel_algo_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_current_algo_open_orders(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AlgoSpotOpenOrdersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get all open SPOT TWAP orders

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.spot_algo.query_current_algo_open_orders(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoSpotOpenOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryCurrentAlgoOpenOrdersErrorBody
```

**Async**

```python
try:
    response = await async_client.spot_algo.query_current_algo_open_orders(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoSpotOpenOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryCurrentAlgoOpenOrdersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AlgoSpotOpenOrdersResponse](binance/models/sapi_v1_algo_spot_open_orders_response.py)</code> -- twap open orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryCurrentAlgoOpenOrdersErrorBody](binance/errors/query_current_algo_open_orders_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_historical_algo_orders(symbol: str, side: SideOrStr, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, page: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AlgoSpotHistoricalOrdersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get all historical SPOT TWAP orders

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.spot_algo.query_historical_algo_orders(symbol, side, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoSpotHistoricalOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryHistoricalAlgoOrdersErrorBody
```

**Async**

```python
try:
    response = await async_client.spot_algo.query_historical_algo_orders(symbol, side, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoSpotHistoricalOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryHistoricalAlgoOrdersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>side</code> | <code>[SideOrStr](binance/models/enums/side.py)</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>str \| None</code> | MIN 1, MAX 100; Default 100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AlgoSpotHistoricalOrdersResponse](binance/models/sapi_v1_algo_spot_historical_orders_response.py)</code> -- twap historical orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryHistoricalAlgoOrdersErrorBody](binance/errors/query_historical_algo_orders_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_sub_orders(algo_id: int, timestamp: int, signature: str, *, page: int | None = None, page_size: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AlgoSpotSubOrdersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get respective sub orders for a specified algoId

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.spot_algo.query_sub_orders(algo_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoSpotSubOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySubOrdersErrorBody
```

**Async**

```python
try:
    response = await async_client.spot_algo.query_sub_orders(algo_id, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AlgoSpotSubOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySubOrdersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>algo_id</code> | <code>int</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>str \| None</code> | MIN 1, MAX 100; Default 100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AlgoSpotSubOrdersResponse](binance/models/sapi_v1_algo_spot_sub_orders_response.py)</code> -- twap sub orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QuerySubOrdersErrorBody](binance/errors/query_sub_orders_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def time_weighted_average_price_twap_new_order(symbol: str, side: SideOrStr, quantity: float, duration: int, timestamp: int, signature: str, *, client_algo_id: str | None = None, limit_price: float | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AlgoSpotNewOrderTwapResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Place a new spot TWAP order with Algo service.

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.spot_algo.time_weighted_average_price_twap_new_order(
        symbol, side, quantity, duration, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1AlgoSpotNewOrderTwapResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TimeWeightedAveragePriceTwapNewOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.spot_algo.time_weighted_average_price_twap_new_order(
        symbol, side, quantity, duration, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1AlgoSpotNewOrderTwapResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TimeWeightedAveragePriceTwapNewOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>side</code> | <code>[SideOrStr](binance/models/enums/side.py)</code> | Value sent with the request. |
| <code>quantity</code> | <code>float</code> | Value sent with the request. |
| <code>duration</code> | <code>int</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>client_algo_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit_price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AlgoSpotNewOrderTwapResponse](binance/models/sapi_v1_algo_spot_new_order_twap_response.py)</code> -- twap order response

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[TimeWeightedAveragePriceTwapNewOrderErrorBody](binance/errors/time_weighted_average_price_twap_new_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Staking

> Source: [Staking](binance/apis/staking.py)

<details>
<summary><code>def eth_staking_account_v2_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2EthStakingAccountResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.staking.eth_staking_account_v2_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2EthStakingAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EthStakingAccountV2UserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.staking.eth_staking_account_v2_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV2EthStakingAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EthStakingAccountV2UserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2EthStakingAccountResponse](binance/models/sapi_v2_eth_staking_account_response.py)</code> -- ETH Staking account

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[EthStakingAccountV2UserDataErrorBody](binance/errors/eth_staking_account_v2_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_beth_rewards_distribution_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1EthStakingEthHistoryRewardsHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- The time between startTime and endTime cannot be longer than 3 months.
- If startTime and endTime are both not sent, then the last 30 days' data will be returned.
- If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be returned.
- If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.staking.get_beth_rewards_distribution_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingEthHistoryRewardsHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBethRewardsDistributionHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.staking.get_beth_rewards_distribution_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingEthHistoryRewardsHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBethRewardsDistributionHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1EthStakingEthHistoryRewardsHistoryResponse](binance/models/sapi_v1_eth_staking_eth_history_rewards_history_response.py)</code> -- BETH rewards distribution history

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetBethRewardsDistributionHistoryUserDataErrorBody](binance/errors/get_beth_rewards_distribution_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_eth_redemption_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1EthStakingEthHistoryRedemptionHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- The time between startTime and endTime cannot be longer than 3 months.
- If startTime and endTime are both not sent, then the last 30 days' data will be returned.
- If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be returned.
- If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.staking.get_eth_redemption_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingEthHistoryRedemptionHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEthRedemptionHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.staking.get_eth_redemption_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingEthHistoryRedemptionHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEthRedemptionHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1EthStakingEthHistoryRedemptionHistoryResponse](binance/models/sapi_v1_eth_staking_eth_history_redemption_history_response.py)</code> -- ETH redemption history

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetEthRedemptionHistoryUserDataErrorBody](binance/errors/get_eth_redemption_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_eth_staking_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1EthStakingEthHistoryStakingHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- The time between startTime and endTime cannot be longer than 3 months.
- If startTime and endTime are both not sent, then the last 30 days' data will be returned.
- If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be returned.
- If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.staking.get_eth_staking_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingEthHistoryStakingHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEthStakingHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.staking.get_eth_staking_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingEthHistoryStakingHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEthStakingHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1EthStakingEthHistoryStakingHistoryResponse](binance/models/sapi_v1_eth_staking_eth_history_staking_history_response.py)</code> -- ETH staking history

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetEthStakingHistoryUserDataErrorBody](binance/errors/get_eth_staking_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_wbeth_rate_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1EthStakingEthHistoryRateHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- The time between startTime and endTime cannot be longer than 3 months.
- If startTime and endTime are both not sent, then the last 30 days' data will be returned.
- If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be returned.
- If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.staking.get_wbeth_rate_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingEthHistoryRateHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetWbethRateHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.staking.get_wbeth_rate_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingEthHistoryRateHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetWbethRateHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1EthStakingEthHistoryRateHistoryResponse](binance/models/sapi_v1_eth_staking_eth_history_rate_history_response.py)</code> -- WBETH Rate History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetWbethRateHistoryUserDataErrorBody](binance/errors/get_wbeth_rate_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_wbeth_rewards_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- The time between startTime and endTime cannot be longer than 3 months.
- If startTime and endTime are both not sent, then the last 30 days' data will be returned.
- If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be returned.
- If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.staking.get_wbeth_rewards_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetWbethRewardsHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.staking.get_wbeth_rewards_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetWbethRewardsHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1EthStakingEthHistoryWbethRewardsHistoryResponse](binance/models/sapi_v1_eth_staking_eth_history_wbeth_rewards_history_response.py)</code> -- WBETH rewards history

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetWbethRewardsHistoryUserDataErrorBody](binance/errors/get_wbeth_rewards_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_wbeth_unwrap_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1EthStakingWbethHistoryUnwrapHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- The time between startTime and endTime cannot be longer than 3 months.
- If startTime and endTime are both not sent, then the last 30 days' data will be returned.
- If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be returned.
- If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.staking.get_wbeth_unwrap_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingWbethHistoryUnwrapHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetWbethUnwrapHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.staking.get_wbeth_unwrap_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingWbethHistoryUnwrapHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetWbethUnwrapHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1EthStakingWbethHistoryUnwrapHistoryResponse](binance/models/sapi_v1_eth_staking_wbeth_history_unwrap_history_response.py)</code> -- WBETH unwrap history

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetWbethUnwrapHistoryUserDataErrorBody](binance/errors/get_wbeth_unwrap_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_wbeth_wrap_history_user_data(timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1EthStakingWbethHistoryWrapHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- The time between startTime and endTime cannot be longer than 3 months.
- If startTime and endTime are both not sent, then the last 30 days' data will be returned.
- If startTime is sent but endTime is not sent, the next 30 days' data beginning from startTime will be returned.
- If endTime is sent but startTime is not sent, the 30 days' data before endTime will be returned.

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.staking.get_wbeth_wrap_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingWbethHistoryWrapHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetWbethWrapHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.staking.get_wbeth_wrap_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingWbethHistoryWrapHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetWbethWrapHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1EthStakingWbethHistoryWrapHistoryResponse](binance/models/sapi_v1_eth_staking_wbeth_history_wrap_history_response.py)</code> -- WBETH wrap history

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetWbethWrapHistoryUserDataErrorBody](binance/errors/get_wbeth_wrap_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_current_eth_staking_quota_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1EthStakingEthQuotaResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.staking.get_current_eth_staking_quota_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingEthQuotaResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCurrentEthStakingQuotaUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.staking.get_current_eth_staking_quota_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingEthQuotaResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCurrentEthStakingQuotaUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1EthStakingEthQuotaResponse](binance/models/sapi_v1_eth_staking_eth_quota_response.py)</code> -- Eth staking quota

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetCurrentEthStakingQuotaUserDataErrorBody](binance/errors/get_current_eth_staking_quota_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def redeem_eth_trade(amount: float, timestamp: int, signature: str, *, asset: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1EthStakingEthRedeemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Redeem WBETH or BETH and get ETH

- You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.staking.redeem_eth_trade(amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingEthRedeemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RedeemEthTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.staking.redeem_eth_trade(amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingEthRedeemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RedeemEthTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>amount</code> | <code>float</code> | Amount in BETH, limit 8 decimals |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | WBETH or BETH, default to BETH<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1EthStakingEthRedeemResponse](binance/models/sapi_v1_eth_staking_eth_redeem_response.py)</code> -- Returned ETH

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RedeemEthTradeErrorBody](binance/errors/redeem_eth_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def subscribe_eth_staking_v2_trade(amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2EthStakingEthStakeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Stake ETH to get WBETH

- You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.staking.subscribe_eth_staking_v2_trade(amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV2EthStakingEthStakeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubscribeEthStakingV2TradeErrorBody
```

**Async**

```python
try:
    response = await async_client.staking.subscribe_eth_staking_v2_trade(amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV2EthStakingEthStakeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubscribeEthStakingV2TradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>amount</code> | <code>float</code> | Amount in ETH, limit 4 decimals |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2EthStakingEthStakeResponse](binance/models/sapi_v2_eth_staking_eth_stake_response.py)</code> -- Subscribed WBETH

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SubscribeEthStakingV2TradeErrorBody](binance/errors/subscribe_eth_staking_v2_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wrap_beth_trade(amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1EthStakingWbethWrapResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.

Weight(IP): 150

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.staking.wrap_beth_trade(amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingWbethWrapResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type WrapBethTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.staking.wrap_beth_trade(amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1EthStakingWbethWrapResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type WrapBethTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>amount</code> | <code>float</code> | Amount in BETH, limit 4 decimals |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1EthStakingWbethWrapResponse](binance/models/sapi_v1_eth_staking_wbeth_wrap_response.py)</code> -- Wrap BETH

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[WrapBethTradeErrorBody](binance/errors/wrap_beth_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Stream

> Source: [Stream](binance/apis/stream.py)

<details>
<summary><code>def close_a_listen_key_user_stream(*, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Close out a user data stream.

Weight: 2

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.stream.close_a_listen_key_user_stream()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CloseAListenKeyUserStreamErrorBody
```

**Async**

```python
try:
    response = await async_client.stream.close_a_listen_key_user_stream()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CloseAListenKeyUserStreamErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>listen_key</code> | <code>str \| None</code> | User websocket listen key<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CloseAListenKeyUserStreamErrorBody](binance/errors/close_a_listen_key_user_stream_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_a_listen_key_user_stream(*, request_options: RequestOptionsOrDict | None = None) -> ApiV3UserDataStreamResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Start a new user data stream.
The stream will close after 60 minutes unless a keepalive is sent. If the account has an active `listenKey`, that `listenKey` will be returned and its validity will be extended for 60 minutes.

Weight: 2

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.stream.create_a_listen_key_user_stream()
    # TODO: Handle 'response' of type ApiV3UserDataStreamResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.stream.create_a_listen_key_user_stream()
    # TODO: Handle 'response' of type ApiV3UserDataStreamResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3UserDataStreamResponse](binance/models/api_v3_user_data_stream_response.py)</code> -- Listen key

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RawError](binance/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def ping_keep_alive_a_listen_key_user_stream(*, listen_key: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 30 minutes.

Weight: 2

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.stream.ping_keep_alive_a_listen_key_user_stream()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PingKeepAliveAListenKeyUserStreamApiErrorBody
```

**Async**

```python
try:
    response = await async_client.stream.ping_keep_alive_a_listen_key_user_stream()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PingKeepAliveAListenKeyUserStreamApiErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>listen_key</code> | <code>str \| None</code> | User websocket listen key<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[PingKeepAliveAListenKeyUserStreamApiErrorBody](binance/errors/ping_keep_alive_a_listen_key_user_stream_api_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SubAccountApi

> Source: [SubAccountApi](binance/apis/sub_account_api.py)

<details>
<summary><code>def create_a_virtual_sub_account_for_master_account(sub_account_string: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountVirtualSubAccountResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- This request will generate a virtual sub account under your master account.
- You need to enable "trade" option for the api key which requests this endpoint.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.create_a_virtual_sub_account_for_master_account(
        sub_account_string, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountVirtualSubAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateAVirtualSubAccountForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.create_a_virtual_sub_account_for_master_account(
        sub_account_string, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountVirtualSubAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateAVirtualSubAccountForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sub_account_string</code> | <code>str</code> | Please input a string. We will create a virtual email using that string for you to register |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountVirtualSubAccountResponse](binance/models/sapi_v1_sub_account_virtual_sub_account_response.py)</code> -- Return the created virtual email

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CreateAVirtualSubAccountForMasterAccountErrorBody](binance/errors/create_a_virtual_sub_account_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_ip_list_for_a_sub_account_api_key_for_master_account(email: str, sub_account_api_key: str, timestamp: int, signature: str, *, ip_address: str | None = None, third_party_name: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountSubAccountApiIpRestrictionIpListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.delete_ip_list_for_a_sub_account_api_key_for_master_account(
        email, sub_account_api_key, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountSubAccountApiIpRestrictionIpListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteIpListForASubAccountApiKeyForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.delete_ip_list_for_a_sub_account_api_key_for_master_account(
        email, sub_account_api_key, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountSubAccountApiIpRestrictionIpListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteIpListForASubAccountApiKeyForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>sub_account_api_key</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>ip_address</code> | <code>str \| None</code> | Can be added in batches, separated by commas<br>**Default**: <code>None</code> |
| <code>third_party_name</code> | <code>str \| None</code> | third party IP list name<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountSubAccountApiIpRestrictionIpListResponse](binance/models/sapi_v1_sub_account_sub_account_api_ip_restriction_ip_list_response.py)</code> -- Delete IP information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[DeleteIpListForASubAccountApiKeyForMasterAccountErrorBody](binance/errors/delete_ip_list_for_a_sub_account_api_key_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deposit_assets_into_the_managed_sub_account_for_investor_master_account(to_email: str, asset: str, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ManagedSubaccountDepositResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.deposit_assets_into_the_managed_sub_account_for_investor_master_account(
        to_email, asset, amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountDepositResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DepositAssetsIntoTheManagedSubAccountForInvestorMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.deposit_assets_into_the_managed_sub_account_for_investor_master_account(
        to_email, asset, amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountDepositResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DepositAssetsIntoTheManagedSubAccountForInvestorMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>to_email</code> | <code>str</code> | Recipient email |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ManagedSubaccountDepositResponse](binance/models/sapi_v1_managed_subaccount_deposit_response.py)</code> -- Transfer id

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[DepositAssetsIntoTheManagedSubAccountForInvestorMasterAccountErrorBody](binance/errors/deposit_assets_into_the_managed_sub_account_for_investor_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def detail_on_sub_account_s_futures_account_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountFuturesAccountResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.detail_on_sub_account_s_futures_account_for_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountFuturesAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DetailOnSubAccountSFuturesAccountForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.detail_on_sub_account_s_futures_account_for_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountFuturesAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DetailOnSubAccountSFuturesAccountForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountFuturesAccountResponse](binance/models/sapi_v1_sub_account_futures_account_response.py)</code> -- Futures account details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[DetailOnSubAccountSFuturesAccountForMasterAccountErrorBody](binance/errors/detail_on_sub_account_s_futures_account_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def detail_on_sub_account_s_futures_account_v2_for_master_account(email: str, futures_type: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2SubAccountFuturesAccountResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.detail_on_sub_account_s_futures_account_v2_for_master_account(
        email, futures_type, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV2SubAccountFuturesAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DetailOnSubAccountSFuturesAccountV2ForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.detail_on_sub_account_s_futures_account_v2_for_master_account(
        email, futures_type, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV2SubAccountFuturesAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DetailOnSubAccountSFuturesAccountV2ForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>futures_type</code> | <code>int</code> | * `1` - USDT Margined Futures<br>* `2` - COIN Margined Futures |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2SubAccountFuturesAccountResponse](binance/models/unions/sapi_v2_sub_account_futures_account_response.py)</code> -- USDT or COIN Margined Futures Details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[DetailOnSubAccountSFuturesAccountV2ForMasterAccountErrorBody](binance/errors/detail_on_sub_account_s_futures_account_v2_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def detail_on_sub_account_s_margin_account_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountMarginAccountResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.detail_on_sub_account_s_margin_account_for_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountMarginAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DetailOnSubAccountSMarginAccountForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.detail_on_sub_account_s_margin_account_for_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountMarginAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DetailOnSubAccountSMarginAccountForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountMarginAccountResponse](binance/models/sapi_v1_sub_account_margin_account_response.py)</code> -- Margin sub-account details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[DetailOnSubAccountSMarginAccountForMasterAccountErrorBody](binance/errors/detail_on_sub_account_s_margin_account_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_futures_for_sub_account_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountFuturesEnableResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.enable_futures_for_sub_account_for_master_account(email, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SubAccountFuturesEnableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableFuturesForSubAccountForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.enable_futures_for_sub_account_for_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountFuturesEnableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableFuturesForSubAccountForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountFuturesEnableResponse](binance/models/sapi_v1_sub_account_futures_enable_response.py)</code> -- Futures status

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[EnableFuturesForSubAccountForMasterAccountErrorBody](binance/errors/enable_futures_for_sub_account_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_leverage_token_for_sub_account_for_master_account(email: str, enable_blvt: bool, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountBlvtEnableResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.enable_leverage_token_for_sub_account_for_master_account(
        email, enable_blvt, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountBlvtEnableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableLeverageTokenForSubAccountForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.enable_leverage_token_for_sub_account_for_master_account(
        email, enable_blvt, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountBlvtEnableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableLeverageTokenForSubAccountForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>enable_blvt</code> | <code>bool</code> | Only true for now |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountBlvtEnableResponse](binance/models/sapi_v1_sub_account_blvt_enable_response.py)</code> -- BLVT status

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[EnableLeverageTokenForSubAccountForMasterAccountErrorBody](binance/errors/enable_leverage_token_for_sub_account_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_margin_for_sub_account_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountMarginEnableResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.enable_margin_for_sub_account_for_master_account(email, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SubAccountMarginEnableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableMarginForSubAccountForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.enable_margin_for_sub_account_for_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountMarginEnableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableMarginForSubAccountForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountMarginEnableResponse](binance/models/sapi_v1_sub_account_margin_enable_response.py)</code> -- Margin status

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[EnableMarginForSubAccountForMasterAccountErrorBody](binance/errors/enable_margin_for_sub_account_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_options_for_sub_account_for_master_account_user_data(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountEoptionsEnableResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enable Options for Sub-account (For Master Account).

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.enable_options_for_sub_account_for_master_account_user_data(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountEoptionsEnableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableOptionsForSubAccountForMasterAccountUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.enable_options_for_sub_account_for_master_account_user_data(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountEoptionsEnableResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableOptionsForSubAccountForMasterAccountUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountEoptionsEnableResponse](binance/models/sapi_v1_sub_account_eoptions_enable_response.py)</code> -- Sub account EOptions status

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[EnableOptionsForSubAccountForMasterAccountUserDataErrorBody](binance/errors/enable_options_for_sub_account_for_master_account_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def futures_position_risk_of_sub_account_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1SubAccountFuturesPositionRiskResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.futures_position_risk_of_sub_account_for_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1SubAccountFuturesPositionRiskResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FuturesPositionRiskOfSubAccountForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.futures_position_risk_of_sub_account_for_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1SubAccountFuturesPositionRiskResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FuturesPositionRiskOfSubAccountForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1SubAccountFuturesPositionRiskResponse](binance/models/sapi_v1_sub_account_futures_position_risk_response.py)&#93;</code> -- Futures account summary

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[FuturesPositionRiskOfSubAccountForMasterAccountErrorBody](binance/errors/futures_position_risk_of_sub_account_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def futures_position_risk_of_sub_account_v2_for_master_account(email: str, futures_type: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2SubAccountFuturesPositionRiskResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.futures_position_risk_of_sub_account_v2_for_master_account(
        email, futures_type, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV2SubAccountFuturesPositionRiskResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FuturesPositionRiskOfSubAccountV2ForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.futures_position_risk_of_sub_account_v2_for_master_account(
        email, futures_type, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV2SubAccountFuturesPositionRiskResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FuturesPositionRiskOfSubAccountV2ForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>futures_type</code> | <code>int</code> | * `1` - USDT Margined Futures<br>* `2` - COIN Margined Futures |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2SubAccountFuturesPositionRiskResponse](binance/models/unions/sapi_v2_sub_account_futures_position_risk_response.py)</code> -- USDT or COIN Margined Futures Position Risk

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[FuturesPositionRiskOfSubAccountV2ForMasterAccountErrorBody](binance/errors/futures_position_risk_of_sub_account_v2_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_ip_restriction_for_a_sub_account_api_key_for_master_account(email: str, sub_account_api_key: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountSubAccountApiIpRestrictionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.get_ip_restriction_for_a_sub_account_api_key_for_master_account(
        email, sub_account_api_key, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountSubAccountApiIpRestrictionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetIpRestrictionForASubAccountApiKeyForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.get_ip_restriction_for_a_sub_account_api_key_for_master_account(
        email, sub_account_api_key, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountSubAccountApiIpRestrictionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetIpRestrictionForASubAccountApiKeyForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>sub_account_api_key</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountSubAccountApiIpRestrictionResponse](binance/models/sapi_v1_sub_account_sub_account_api_ip_restriction_response.py)</code> -- IP Restriction information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetIpRestrictionForASubAccountApiKeyForMasterAccountErrorBody](binance/errors/get_ip_restriction_for_a_sub_account_api_key_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_managed_sub_account_deposit_address_for_investor_master_account(email: str, coin: str, timestamp: int, signature: str, *, network: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ManagedSubaccountDepositAddressResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get investor's managed sub-account deposit address

Weight(UID): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.get_managed_sub_account_deposit_address_for_investor_master_account(
        email, coin, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountDepositAddressResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetManagedSubAccountDepositAddressForInvestorMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.get_managed_sub_account_deposit_address_for_investor_master_account(
        email, coin, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountDepositAddressResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetManagedSubAccountDepositAddressForInvestorMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Value sent with the request. |
| <code>coin</code> | <code>str</code> | Coin name |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>network</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ManagedSubaccountDepositAddressResponse](binance/models/sapi_v1_managed_subaccount_deposit_address_response.py)</code> -- Managed sub deposit address

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetManagedSubAccountDepositAddressForInvestorMasterAccountErrorBody](binance/errors/get_managed_sub_account_deposit_address_for_investor_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def managed_sub_account_asset_details_for_investor_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1ManagedSubaccountAssetResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.managed_sub_account_asset_details_for_investor_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1ManagedSubaccountAssetResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ManagedSubAccountAssetDetailsForInvestorMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.managed_sub_account_asset_details_for_investor_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1ManagedSubaccountAssetResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ManagedSubAccountAssetDetailsForInvestorMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1ManagedSubaccountAssetResponse](binance/models/sapi_v1_managed_subaccount_asset_response.py)&#93;</code> -- List of asset details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[ManagedSubAccountAssetDetailsForInvestorMasterAccountErrorBody](binance/errors/managed_sub_account_asset_details_for_investor_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def managed_sub_account_snapshot_for_investor_master_account(email: str, type_: str, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ManagedSubaccountAccountSnapshotResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- The query time period must be less then 30 days
- Support query within the last one month only
- If `startTime` and `endTime` not sent, return records of the last 7 days by default

Weight(IP): 2400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.managed_sub_account_snapshot_for_investor_master_account(
        email, type_, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountAccountSnapshotResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ManagedSubAccountSnapshotForInvestorMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.managed_sub_account_snapshot_for_investor_master_account(
        email, type_, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountAccountSnapshotResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ManagedSubAccountSnapshotForInvestorMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>type_</code> | <code>str</code> | "SPOT", "MARGIN"(cross), "FUTURES"(UM) |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | min 7, max 30, default 7<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ManagedSubaccountAccountSnapshotResponse](binance/models/sapi_v1_managed_subaccount_account_snapshot_response.py)</code> -- Sub-account spot snapshot

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[ManagedSubAccountSnapshotForInvestorMasterAccountErrorBody](binance/errors/managed_sub_account_snapshot_for_investor_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def margin_transfer_for_sub_account_for_master_account(email: str, asset: str, amount: float, type_: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountMarginTransferResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.margin_transfer_for_sub_account_for_master_account(
        email, asset, amount, type_, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountMarginTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginTransferForSubAccountForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.margin_transfer_for_sub_account_for_master_account(
        email, asset, amount, type_, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountMarginTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MarginTransferForSubAccountForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>type_</code> | <code>int</code> | * `1` - transfer from subaccount's spot account to margin account<br>* `2` - transfer from subaccount's margin account to its spot account |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountMarginTransferResponse](binance/models/sapi_v1_sub_account_margin_transfer_response.py)</code> -- Transfer id

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[MarginTransferForSubAccountForMasterAccountErrorBody](binance/errors/margin_transfer_for_sub_account_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_managed_sub_account_transfer_log_for_investor_master_account(email: str, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, page: int | None = None, limit: int | None = None, transfers: str | None = None, transfer_function_account_type: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ManagedSubaccountQueryTransLogForInvestorResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Investor can use this api to query managed sub account transfer log. This endpoint is available for investor of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in asset allocation and account application, while delegating trades to a professional trading team.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.query_managed_sub_account_transfer_log_for_investor_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountQueryTransLogForInvestorResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryManagedSubAccountTransferLogForInvestorMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.query_managed_sub_account_transfer_log_for_investor_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountQueryTransLogForInvestorResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryManagedSubAccountTransferLogForInvestorMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>transfers</code> | <code>str \| None</code> | Transfer Direction (FROM/TO)<br>**Default**: <code>None</code> |
| <code>transfer_function_account_type</code> | <code>str \| None</code> | Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ManagedSubaccountQueryTransLogForInvestorResponse](binance/models/sapi_v1_managed_subaccount_query_trans_log_for_investor_response.py)</code> -- Managed sub account transfer logs (for invest account)

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryManagedSubAccountTransferLogForInvestorMasterAccountErrorBody](binance/errors/query_managed_sub_account_transfer_log_for_investor_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_managed_sub_account_transfer_log_for_trading_team_master_account(email: str, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, page: int | None = None, limit: int | None = None, transfers: str | None = None, transfer_function_account_type: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Trading team can use this api to query managed sub account transfer log. This endpoint is available for trading team of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in asset allocation and account application, while delegating trades to a professional trading team

Weight(IP): 60

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.query_managed_sub_account_transfer_log_for_trading_team_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryManagedSubAccountTransferLogForTradingTeamMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.query_managed_sub_account_transfer_log_for_trading_team_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryManagedSubAccountTransferLogForTradingTeamMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>transfers</code> | <code>str \| None</code> | Transfer Direction (FROM/TO)<br>**Default**: <code>None</code> |
| <code>transfer_function_account_type</code> | <code>str \| None</code> | Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ManagedSubaccountQueryTransLogForTradeParentResponse](binance/models/sapi_v1_managed_subaccount_query_trans_log_for_trade_parent_response.py)</code> -- Managed sub account transfer logs (for trading team)

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryManagedSubAccountTransferLogForTradingTeamMasterAccountErrorBody](binance/errors/query_managed_sub_account_transfer_log_for_trading_team_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data(transfers: TransfersOrStr, transfer_function_account_type: TransferFunctionAccountTypeOrStr, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, page: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ManagedSubaccountQueryTransLogResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query Managed Sub Account Transfer Log (For Trading Team Sub Account)

Weight(UID): 60

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data(
        transfers, transfer_function_account_type, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountQueryTransLogResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryManagedSubAccountTransferLogForTradingTeamSubAccountUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data(
        transfers, transfer_function_account_type, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountQueryTransLogResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryManagedSubAccountTransferLogForTradingTeamSubAccountUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>transfers</code> | <code>[TransfersOrStr](binance/models/enums/transfers.py)</code> | Transfer Direction |
| <code>transfer_function_account_type</code> | <code>[TransferFunctionAccountTypeOrStr](binance/models/enums/transfer_function_account_type.py)</code> | Transfer function account type |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ManagedSubaccountQueryTransLogResponse](binance/models/sapi_v1_managed_subaccount_query_trans_log_response.py)</code> -- Managed sub deposit address

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryManagedSubAccountTransferLogForTradingTeamSubAccountUserDataErrorBody](binance/errors/query_managed_sub_account_transfer_log_for_trading_team_sub_account_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_managed_sub_account_futures_asset_details_for_investor_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ManagedSubaccountFetchFutureAssetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Investor can use this api to query managed sub account futures asset details

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.query_managed_sub_account_futures_asset_details_for_investor_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountFetchFutureAssetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryManagedSubAccountFuturesAssetDetailsForInvestorMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.query_managed_sub_account_futures_asset_details_for_investor_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountFetchFutureAssetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryManagedSubAccountFuturesAssetDetailsForInvestorMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ManagedSubaccountFetchFutureAssetResponse](binance/models/sapi_v1_managed_subaccount_fetch_future_asset_response.py)</code> -- Sub account futures assset details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryManagedSubAccountFuturesAssetDetailsForInvestorMasterAccountErrorBody](binance/errors/query_managed_sub_account_futures_asset_details_for_investor_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_managed_sub_account_list_for_investor(email: str, timestamp: int, signature: str, *, page: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ManagedSubaccountInfoResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get investor's managed sub-account list.

Weight(UID): 60

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.query_managed_sub_account_list_for_investor(email, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryManagedSubAccountListForInvestorErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.query_managed_sub_account_list_for_investor(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryManagedSubAccountListForInvestorErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ManagedSubaccountInfoResponse](binance/models/sapi_v1_managed_subaccount_info_response.py)</code> -- Managed sub account list

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryManagedSubAccountListForInvestorErrorBody](binance/errors/query_managed_sub_account_list_for_investor_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_managed_sub_account_margin_asset_details_for_investor_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ManagedSubaccountMarginAssetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Investor can use this api to query managed sub account margin asset details

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.query_managed_sub_account_margin_asset_details_for_investor_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountMarginAssetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryManagedSubAccountMarginAssetDetailsForInvestorMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.query_managed_sub_account_margin_asset_details_for_investor_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountMarginAssetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryManagedSubAccountMarginAssetDetailsForInvestorMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ManagedSubaccountMarginAssetResponse](binance/models/sapi_v1_managed_subaccount_margin_asset_response.py)</code> -- Sub account margin assset details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryManagedSubAccountMarginAssetDetailsForInvestorMasterAccountErrorBody](binance/errors/query_managed_sub_account_margin_asset_details_for_investor_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_sub_account_assets_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV4SubAccountAssetsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch sub-account assets

Weight(UID): 60

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.query_sub_account_assets_for_master_account(email, timestamp, signature)
    # TODO: Handle 'response' of type SapiV4SubAccountAssetsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySubAccountAssetsForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.query_sub_account_assets_for_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV4SubAccountAssetsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySubAccountAssetsForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV4SubAccountAssetsResponse](binance/models/sapi_v4_sub_account_assets_response.py)</code> -- Sub account balances

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QuerySubAccountAssetsForMasterAccountErrorBody](binance/errors/query_sub_account_assets_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_sub_account_list_for_master_account(timestamp: int, signature: str, *, email: str | None = None, is_freeze: IsFreezeOrStr | None = None, page: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.query_sub_account_list_for_master_account(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SubAccountListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySubAccountListForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.query_sub_account_list_for_master_account(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SubAccountListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySubAccountListForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>email</code> | <code>str \| None</code> | Sub-account email<br>**Default**: <code>None</code> |
| <code>is_freeze</code> | <code>[IsFreezeOrStr](binance/models/enums/is_freeze.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 1; max 200<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountListResponse](binance/models/sapi_v1_sub_account_list_response.py)</code> -- List of sub-accounts

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QuerySubAccountListForMasterAccountErrorBody](binance/errors/query_sub_account_list_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_sub_account_transaction_statistics_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountTransactionStatisticsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query Sub-account Transaction statistics (For Master Account).

Weight(UID): 60

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.query_sub_account_transaction_statistics_for_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountTransactionStatisticsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySubAccountTransactionStatisticsForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.query_sub_account_transaction_statistics_for_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountTransactionStatisticsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QuerySubAccountTransactionStatisticsForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountTransactionStatisticsResponse](binance/models/sapi_v1_sub_account_transaction_statistics_response.py)</code> -- Sub account transaction statistics

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QuerySubAccountTransactionStatisticsForMasterAccountErrorBody](binance/errors/query_sub_account_transaction_statistics_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sub_account_assets_for_master_account(email: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV3SubAccountAssetsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch sub-account assets

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.sub_account_assets_for_master_account(email, timestamp, signature)
    # TODO: Handle 'response' of type SapiV3SubAccountAssetsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountAssetsForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.sub_account_assets_for_master_account(email, timestamp, signature)
    # TODO: Handle 'response' of type SapiV3SubAccountAssetsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountAssetsForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV3SubAccountAssetsResponse](binance/models/sapi_v3_sub_account_assets_response.py)</code> -- List of assets balances

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SubAccountAssetsForMasterAccountErrorBody](binance/errors/sub_account_assets_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sub_account_deposit_history_for_master_account(email: str, timestamp: int, signature: str, *, coin: str | None = None, status: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, offset: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1CapitalDepositSubHisrecResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch sub-account deposit history

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.sub_account_deposit_history_for_master_account(email, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1CapitalDepositSubHisrecResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountDepositHistoryForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.sub_account_deposit_history_for_master_account(
        email, timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1CapitalDepositSubHisrecResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountDepositHistoryForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>coin</code> | <code>str \| None</code> | Coin name<br>**Default**: <code>None</code> |
| <code>status</code> | <code>int \| None</code> | 0(0:pending,6: credited but cannot withdraw, 1:success)<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1CapitalDepositSubHisrecResponse](binance/models/sapi_v1_capital_deposit_sub_hisrec_response.py)&#93;</code> -- Sub-account deposit history

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SubAccountDepositHistoryForMasterAccountErrorBody](binance/errors/sub_account_deposit_history_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sub_account_futures_asset_transfer_for_master_account(from_email: str, to_email: str, futures_type: int, asset: str, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountFuturesInternalTransferResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- Master account can transfer max 2000 times a minute

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.sub_account_futures_asset_transfer_for_master_account(
        from_email, to_email, futures_type, asset, amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountFuturesInternalTransferResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountFuturesAssetTransferForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.sub_account_futures_asset_transfer_for_master_account(
        from_email, to_email, futures_type, asset, amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountFuturesInternalTransferResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountFuturesAssetTransferForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>from_email</code> | <code>str</code> | Sender email |
| <code>to_email</code> | <code>str</code> | Recipient email |
| <code>futures_type</code> | <code>int</code> | 1:USDT-margined Futures,2: Coin-margined Futures |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountFuturesInternalTransferResponse1](binance/models/sapi_v1_sub_account_futures_internal_transfer_response1.py)</code> -- Futures Asset Transfer Info

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SubAccountFuturesAssetTransferForMasterAccountErrorBody](binance/errors/sub_account_futures_asset_transfer_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sub_account_futures_asset_transfer_history_for_master_account(email: str, futures_type: int, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, page: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountFuturesInternalTransferResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.sub_account_futures_asset_transfer_history_for_master_account(
        email, futures_type, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountFuturesInternalTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountFuturesAssetTransferHistoryForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.sub_account_futures_asset_transfer_history_for_master_account(
        email, futures_type, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountFuturesInternalTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountFuturesAssetTransferHistoryForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>futures_type</code> | <code>int</code> | 1:USDT-margined Futures, 2: Coin-margined Futures |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default value: 50, Max value: 500<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountFuturesInternalTransferResponse](binance/models/sapi_v1_sub_account_futures_internal_transfer_response.py)</code> -- Sub-account Futures Asset Transfer History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SubAccountFuturesAssetTransferHistoryForMasterAccountErrorBody](binance/errors/sub_account_futures_asset_transfer_history_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sub_account_spot_asset_transfer_history_for_master_account(timestamp: int, signature: str, *, from_email: str | None = None, to_email: str | None = None, start_time: int | None = None, end_time: int | None = None, page: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1SubAccountSubTransferHistoryResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- fromEmail and toEmail cannot be sent at the same time.
- Return fromEmail equal master account email by default.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.sub_account_spot_asset_transfer_history_for_master_account(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1SubAccountSubTransferHistoryResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountSpotAssetTransferHistoryForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.sub_account_spot_asset_transfer_history_for_master_account(
        timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1SubAccountSubTransferHistoryResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountSpotAssetTransferHistoryForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>from_email</code> | <code>str \| None</code> | Sub-account email<br>**Default**: <code>None</code> |
| <code>to_email</code> | <code>str \| None</code> | Sub-account email<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1SubAccountSubTransferHistoryResponse](binance/models/sapi_v1_sub_account_sub_transfer_history_response.py)&#93;</code> -- Sub-account Spot Asset Transfer History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SubAccountSpotAssetTransferHistoryForMasterAccountErrorBody](binance/errors/sub_account_spot_asset_transfer_history_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sub_account_spot_assets_summary_for_master_account(timestamp: int, signature: str, *, email: str | None = None, page: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountSpotSummaryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get BTC valued asset summary of subaccounts.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.sub_account_spot_assets_summary_for_master_account(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SubAccountSpotSummaryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountSpotAssetsSummaryForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.sub_account_spot_assets_summary_for_master_account(
        timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountSpotSummaryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountSpotAssetsSummaryForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>email</code> | <code>str \| None</code> | Sub-account email<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:20<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountSpotSummaryResponse](binance/models/sapi_v1_sub_account_spot_summary_response.py)</code> -- Summary of Sub-account Spot Assets

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SubAccountSpotAssetsSummaryForMasterAccountErrorBody](binance/errors/sub_account_spot_assets_summary_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sub_account_spot_assets_summary_for_master_account_2(email: str, coin: str, timestamp: int, signature: str, *, network: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1CapitalDepositSubAddressResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch sub-account deposit address

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.sub_account_spot_assets_summary_for_master_account_2(
        email, coin, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1CapitalDepositSubAddressResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountSpotAssetsSummaryForMasterAccount2ErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.sub_account_spot_assets_summary_for_master_account_2(
        email, coin, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1CapitalDepositSubAddressResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountSpotAssetsSummaryForMasterAccount2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>coin</code> | <code>str</code> | Coin name |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>network</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1CapitalDepositSubAddressResponse](binance/models/sapi_v1_capital_deposit_sub_address_response.py)</code> -- Deposit address info

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SubAccountSpotAssetsSummaryForMasterAccount2ErrorBody](binance/errors/sub_account_spot_assets_summary_for_master_account2_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sub_account_transfer_history_for_sub_account(timestamp: int, signature: str, *, asset: str | None = None, type_: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1SubAccountTransferSubUserHistoryResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If `type` is not sent, the records of type 2: transfer out will be returned by default.
- If `startTime` and `endTime` are not sent, the recent 30-day data will be returned.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.sub_account_transfer_history_for_sub_account(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1SubAccountTransferSubUserHistoryResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountTransferHistoryForSubAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.sub_account_transfer_history_for_sub_account(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1SubAccountTransferSubUserHistoryResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountTransferHistoryForSubAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>type_</code> | <code>int \| None</code> | * `1` - transfer in<br>* `2` - transfer out<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1SubAccountTransferSubUserHistoryResponse](binance/models/sapi_v1_sub_account_transfer_sub_user_history_response.py)&#93;</code> -- Transfer id

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SubAccountTransferHistoryForSubAccountErrorBody](binance/errors/sub_account_transfer_history_for_sub_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sub_account_s_status_on_margin_futures_for_master_account(timestamp: int, signature: str, *, email: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1SubAccountStatusResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- If no `email` sent, all sub-accounts' information will be returned.

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.sub_account_s_status_on_margin_futures_for_master_account(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1SubAccountStatusResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountSStatusOnMarginFuturesForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.sub_account_s_status_on_margin_futures_for_master_account(
        timestamp, signature
    )
    # TODO: Handle 'response' of type list[SapiV1SubAccountStatusResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubAccountSStatusOnMarginFuturesForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>email</code> | <code>str \| None</code> | Sub-account email<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1SubAccountStatusResponse](binance/models/sapi_v1_sub_account_status_response.py)&#93;</code> -- Status on Margin/Futures

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SubAccountSStatusOnMarginFuturesForMasterAccountErrorBody](binance/errors/sub_account_s_status_on_margin_futures_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def summary_of_sub_account_s_futures_account_for_master_account(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountFuturesAccountSummaryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.summary_of_sub_account_s_futures_account_for_master_account(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SubAccountFuturesAccountSummaryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SummaryOfSubAccountSFuturesAccountForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.summary_of_sub_account_s_futures_account_for_master_account(
        timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountFuturesAccountSummaryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SummaryOfSubAccountSFuturesAccountForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountFuturesAccountSummaryResponse](binance/models/sapi_v1_sub_account_futures_account_summary_response.py)</code> -- Futures account summary

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SummaryOfSubAccountSFuturesAccountForMasterAccountErrorBody](binance/errors/summary_of_sub_account_s_futures_account_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def summary_of_sub_account_s_futures_account_v2_for_master_account(futures_type: int, timestamp: int, signature: str, *, page: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2SubAccountFuturesAccountSummaryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.summary_of_sub_account_s_futures_account_v2_for_master_account(
        futures_type, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV2SubAccountFuturesAccountSummaryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SummaryOfSubAccountSFuturesAccountV2ForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.summary_of_sub_account_s_futures_account_v2_for_master_account(
        futures_type, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV2SubAccountFuturesAccountSummaryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SummaryOfSubAccountSFuturesAccountV2ForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>futures_type</code> | <code>int</code> | * `1` - USDT Margined Futures<br>* `2` - COIN Margined Futures |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 10, Max 20<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2SubAccountFuturesAccountSummaryResponse](binance/models/unions/sapi_v2_sub_account_futures_account_summary_response.py)</code> -- USDT or COIN Margined Futures Summary

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SummaryOfSubAccountSFuturesAccountV2ForMasterAccountErrorBody](binance/errors/summary_of_sub_account_s_futures_account_v2_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def summary_of_sub_account_s_margin_account_for_master_account(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountMarginAccountSummaryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.summary_of_sub_account_s_margin_account_for_master_account(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SubAccountMarginAccountSummaryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SummaryOfSubAccountSMarginAccountForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.summary_of_sub_account_s_margin_account_for_master_account(
        timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountMarginAccountSummaryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SummaryOfSubAccountSMarginAccountForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountMarginAccountSummaryResponse](binance/models/sapi_v1_sub_account_margin_account_summary_response.py)</code> -- Margin sub-account details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SummaryOfSubAccountSMarginAccountForMasterAccountErrorBody](binance/errors/summary_of_sub_account_s_margin_account_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_for_sub_account_for_master_account(email: str, asset: str, amount: float, type_: int, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountFuturesTransferResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.transfer_for_sub_account_for_master_account(
        email, asset, amount, type_, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountFuturesTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TransferForSubAccountForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.transfer_for_sub_account_for_master_account(
        email, asset, amount, type_, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountFuturesTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TransferForSubAccountForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>type_</code> | <code>int</code> | * `1` - transfer from subaccount's spot account to its USDT-margined futures account<br>* `2` - transfer from subaccount's USDT-margined futures account to its spot account<br>* `3` - transfer from subaccount's spot account to its COIN-margined futures account<br>* `4` - transfer from subaccount's COIN-margined futures account to its spot account |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountFuturesTransferResponse](binance/models/sapi_v1_sub_account_futures_transfer_response.py)</code> -- Transfer id

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[TransferForSubAccountForMasterAccountErrorBody](binance/errors/transfer_for_sub_account_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_to_master_for_sub_account(asset: str, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountTransferSubToMasterResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.transfer_to_master_for_sub_account(asset, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1SubAccountTransferSubToMasterResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TransferToMasterForSubAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.transfer_to_master_for_sub_account(
        asset, amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountTransferSubToMasterResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TransferToMasterForSubAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountTransferSubToMasterResponse](binance/models/sapi_v1_sub_account_transfer_sub_to_master_response.py)</code> -- Transfer id

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[TransferToMasterForSubAccountErrorBody](binance/errors/transfer_to_master_for_sub_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_to_sub_account_of_same_master_for_sub_account(to_email: str, asset: str, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountTransferSubToSubResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.transfer_to_sub_account_of_same_master_for_sub_account(
        to_email, asset, amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountTransferSubToSubResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TransferToSubAccountOfSameMasterForSubAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.transfer_to_sub_account_of_same_master_for_sub_account(
        to_email, asset, amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountTransferSubToSubResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TransferToSubAccountOfSameMasterForSubAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>to_email</code> | <code>str</code> | Recipient email |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountTransferSubToSubResponse](binance/models/sapi_v1_sub_account_transfer_sub_to_sub_response.py)</code> -- Transfer id

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[TransferToSubAccountOfSameMasterForSubAccountErrorBody](binance/errors/transfer_to_sub_account_of_same_master_for_sub_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def universal_transfer_for_master_account(from_account_type: FromAccountTypeOrStr, to_account_type: ToAccountTypeOrStr, asset: str, amount: float, timestamp: int, signature: str, *, from_email: str | None = None, to_email: str | None = None, client_tran_id: str | None = None, symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1SubAccountUniversalTransferResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- You need to enable "internal transfer" option for the api key which requests this endpoint.
- Transfer from master account by default if fromEmail is not sent.
- Transfer to master account by default if toEmail is not sent.
- Supported transfer scenarios:
  - Master account SPOT transfer to sub-account SPOT,USDT_FUTURE,COIN_FUTURE,MARGIN(Cross),ISOLATED_MARGIN
  - Sub-account SPOT,USDT_FUTURE,COIN_FUTURE,MARGIN(Cross),ISOLATED_MARGIN transfer to master account SPOT
  - Transfer between two sub-account SPOT accounts

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.universal_transfer_for_master_account(
        from_account_type, to_account_type, asset, amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountUniversalTransferResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UniversalTransferForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.universal_transfer_for_master_account(
        from_account_type, to_account_type, asset, amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1SubAccountUniversalTransferResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UniversalTransferForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>from_account_type</code> | <code>[FromAccountTypeOrStr](binance/models/enums/from_account_type.py)</code> | Value sent with the request. |
| <code>to_account_type</code> | <code>[ToAccountTypeOrStr](binance/models/enums/to_account_type.py)</code> | Value sent with the request. |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>from_email</code> | <code>str \| None</code> | Sub-account email<br>**Default**: <code>None</code> |
| <code>to_email</code> | <code>str \| None</code> | Sub-account email<br>**Default**: <code>None</code> |
| <code>client_tran_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>symbol</code> | <code>str \| None</code> | Only supported under ISOLATED_MARGIN type<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SubAccountUniversalTransferResponse1](binance/models/sapi_v1_sub_account_universal_transfer_response1.py)</code> -- Transfer id

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[UniversalTransferForMasterAccountErrorBody](binance/errors/universal_transfer_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def universal_transfer_history_for_master_account(timestamp: int, signature: str, *, from_email: str | None = None, to_email: str | None = None, client_tran_id: str | None = None, start_time: int | None = None, end_time: int | None = None, page: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1SubAccountUniversalTransferResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- `fromEmail` and `toEmail` cannot be sent at the same time.
- Return `fromEmail` equal master account email by default.
- The query time period must be less then 30 days.
- If startTime and endTime not sent, return records of the last 30 days by default.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.universal_transfer_history_for_master_account(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1SubAccountUniversalTransferResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UniversalTransferHistoryForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.universal_transfer_history_for_master_account(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1SubAccountUniversalTransferResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UniversalTransferHistoryForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>from_email</code> | <code>str \| None</code> | Sub-account email<br>**Default**: <code>None</code> |
| <code>to_email</code> | <code>str \| None</code> | Sub-account email<br>**Default**: <code>None</code> |
| <code>client_tran_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Default 1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500, Max 500<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1SubAccountUniversalTransferResponse](binance/models/sapi_v1_sub_account_universal_transfer_response.py)&#93;</code> -- Transfer History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[UniversalTransferHistoryForMasterAccountErrorBody](binance/errors/universal_transfer_history_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_ip_restriction_for_sub_account_api_key_for_master_account(email: str, sub_account_api_key: str, status: str, timestamp: int, signature: str, *, third_party_name: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV2SubAccountSubAccountApiIpRestrictionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update IP Restriction for Sub-Account API key

Weight(UID): 3000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.update_ip_restriction_for_sub_account_api_key_for_master_account(
        email, sub_account_api_key, status, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV2SubAccountSubAccountApiIpRestrictionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateIpRestrictionForSubAccountApiKeyForMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.update_ip_restriction_for_sub_account_api_key_for_master_account(
        email, sub_account_api_key, status, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV2SubAccountSubAccountApiIpRestrictionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateIpRestrictionForSubAccountApiKeyForMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Sub-account email |
| <code>sub_account_api_key</code> | <code>str</code> | Value sent with the request. |
| <code>status</code> | <code>str</code> | IP Restriction status. 1 = IP Unrestricted. 2 = Restrict access to trusted IPs only. 3 = Restrict access to users' trusted third party IPs only |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>third_party_name</code> | <code>str \| None</code> | third party IP list name<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV2SubAccountSubAccountApiIpRestrictionResponse](binance/models/sapi_v2_sub_account_sub_account_api_ip_restriction_response.py)</code> -- Update IP Restriction

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[UpdateIpRestrictionForSubAccountApiKeyForMasterAccountErrorBody](binance/errors/update_ip_restriction_for_sub_account_api_key_for_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def withdrawl_assets_from_the_managed_sub_account_for_investor_master_account(from_email: str, asset: str, amount: float, timestamp: int, signature: str, *, transfer_date: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1ManagedSubaccountWithdrawResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sub_account_api.withdrawl_assets_from_the_managed_sub_account_for_investor_master_account(
        from_email, asset, amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountWithdrawResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type WithdrawlAssetsFromTheManagedSubAccountForInvestorMasterAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sub_account_api.withdrawl_assets_from_the_managed_sub_account_for_investor_master_account(
        from_email, asset, amount, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1ManagedSubaccountWithdrawResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type WithdrawlAssetsFromTheManagedSubAccountForInvestorMasterAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>from_email</code> | <code>str</code> | Sender email |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>transfer_date</code> | <code>int \| None</code> | Withdrawals is automatically occur on the transfer date(UTC0). If a date is not selected, the withdrawal occurs right now<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1ManagedSubaccountWithdrawResponse](binance/models/sapi_v1_managed_subaccount_withdraw_response.py)</code> -- Transfer id

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[WithdrawlAssetsFromTheManagedSubAccountForInvestorMasterAccountErrorBody](binance/errors/withdrawl_assets_from_the_managed_sub_account_for_investor_master_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## TradeApi

> Source: [TradeApi](binance/apis/trade_api.py)

<details>
<summary><code>def account_information_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Account</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get current account information.

Weight(IP): 20

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.account_information_user_data(timestamp, signature)
    # TODO: Handle 'response' of type Account
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AccountInformationUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.account_information_user_data(timestamp, signature)
    # TODO: Handle 'response' of type Account
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AccountInformationUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Account](binance/models/account.py)</code> -- Account details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AccountInformationUserDataErrorBody](binance/errors/account_information_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def account_trade_list_user_data(symbol: str, timestamp: int, signature: str, *, order_id: int | None = None, start_time: int | None = None, end_time: int | None = None, from_id: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[MyTrade]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get trades for a specific account and symbol.

If `fromId` is set, it will get id >= that `fromId`. Otherwise most recent orders are returned.

The time between startTime and endTime can't be longer than 24 hours.
These are the supported combinations of all parameters:

  symbol

  symbol + orderId

  symbol + startTime

  symbol + endTime

  symbol + fromId

  symbol + startTime + endTime

  symbol+ orderId + fromId

Weight(IP): 20

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.account_trade_list_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[MyTrade]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AccountTradeListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.account_trade_list_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[MyTrade]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AccountTradeListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>int \| None</code> | This can only be used in combination with symbol.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>from_id</code> | <code>int \| None</code> | Trade id to fetch from. Default gets most recent trades.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[MyTrade](binance/models/my_trade.py)&#93;</code> -- List of trades

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AccountTradeListUserDataErrorBody](binance/errors/account_trade_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def all_orders_user_data(symbol: str, timestamp: int, signature: str, *, order_id: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[OrderDetails]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get all account orders; active, canceled, or filled..

- If `orderId` is set, it will get orders >= that `orderId`. Otherwise most recent orders are returned.
- For some historical orders `cummulativeQuoteQty` will be < 0, meaning the data is not available at this time.
- If `startTime` and/or `endTime` provided, `orderId` is not required

Weight(IP): 20

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.all_orders_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[OrderDetails]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AllOrdersUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.all_orders_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[OrderDetails]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AllOrdersUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>int \| None</code> | Order id<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[OrderDetails](binance/models/order_details.py)&#93;</code> -- Current open orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AllOrdersUserDataErrorBody](binance/errors/all_orders_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_oco_trade(symbol: str, timestamp: int, signature: str, *, order_list_id: int | None = None, list_client_order_id: str | None = None, new_client_order_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> OcoOrder</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancel an entire Order List

Canceling an individual leg will cancel the entire OCO

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.cancel_oco_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type OcoOrder
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelOcoTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.cancel_oco_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type OcoOrder
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelOcoTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_list_id</code> | <code>int \| None</code> | Order list id<br>**Default**: <code>None</code> |
| <code>list_client_order_id</code> | <code>str \| None</code> | A unique Id for the entire orderList<br>**Default**: <code>None</code> |
| <code>new_client_order_id</code> | <code>str \| None</code> | Used to uniquely identify this cancel. Automatically generated by default<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[OcoOrder](binance/models/oco_order.py)</code> -- Report on deleted OCO

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CancelOcoTradeErrorBody](binance/errors/cancel_oco_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_order_trade(symbol: str, timestamp: int, signature: str, *, order_id: int | None = None, orig_client_order_id: str | None = None, new_client_order_id: str | None = None, cancel_restrictions: CancelRestrictionsOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Order</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancel an active order.

Either `orderId` or `origClientOrderId` must be sent.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.cancel_order_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type Order
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelOrderTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.cancel_order_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type Order
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelOrderTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>int \| None</code> | Order id<br>**Default**: <code>None</code> |
| <code>orig_client_order_id</code> | <code>str \| None</code> | Order id from client<br>**Default**: <code>None</code> |
| <code>new_client_order_id</code> | <code>str \| None</code> | Used to uniquely identify this cancel. Automatically generated by default<br>**Default**: <code>None</code> |
| <code>cancel_restrictions</code> | <code>[CancelRestrictionsOrStr](binance/models/enums/cancel_restrictions.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Order](binance/models/order.py)</code> -- Cancelled order

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CancelOrderTradeErrorBody](binance/errors/cancel_order_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_all_open_orders_on_a_symbol_trade(symbol: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[ApiV3OpenOrdersResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels all active orders on a symbol.
This includes OCO orders.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.cancel_all_open_orders_on_a_symbol_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[ApiV3OpenOrdersResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelAllOpenOrdersOnASymbolTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.cancel_all_open_orders_on_a_symbol_trade(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[ApiV3OpenOrdersResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelAllOpenOrdersOnASymbolTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ApiV3OpenOrdersResponse](binance/models/unions/api_v3_open_orders_response.py)&#93;</code> -- Cancelled orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CancelAllOpenOrdersOnASymbolTradeErrorBody](binance/errors/cancel_all_open_orders_on_a_symbol_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_an_existing_order_and_send_a_new_order_trade(symbol: str, side: SideOrStr, type_: Type1OrStr, cancel_replace_mode: str, timestamp: int, signature: str, *, cancel_restrictions: CancelRestrictionsOrStr | None = None, time_in_force: TimeInForceOrStr | None = None, quantity: float | None = None, quote_order_qty: float | None = None, price: float | None = None, cancel_new_client_order_id: str | None = None, cancel_orig_client_order_id: str | None = None, cancel_order_id: int | None = None, new_client_order_id: str | None = None, strategy_id: int | None = None, strategy_type: int | None = None, stop_price: float | None = None, trailing_delta: float | None = None, iceberg_qty: float | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiV3OrderCancelReplaceResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels an existing order and places a new order on the same symbol.

Filters and Order Count are evaluated before the processing of the cancellation and order placement occurs.

A new order that was not attempted (i.e. when newOrderResult: NOT_ATTEMPTED), will still increase the order count by 1.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.cancel_an_existing_order_and_send_a_new_order_trade(
        symbol, side, type_, cancel_replace_mode, timestamp, signature
    )
    # TODO: Handle 'response' of type ApiV3OrderCancelReplaceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelAnExistingOrderAndSendANewOrderTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.cancel_an_existing_order_and_send_a_new_order_trade(
        symbol, side, type_, cancel_replace_mode, timestamp, signature
    )
    # TODO: Handle 'response' of type ApiV3OrderCancelReplaceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelAnExistingOrderAndSendANewOrderTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>side</code> | <code>[SideOrStr](binance/models/enums/side.py)</code> | Value sent with the request. |
| <code>type_</code> | <code>[Type1OrStr](binance/models/enums/type1.py)</code> | Order type |
| <code>cancel_replace_mode</code> | <code>str</code> | - `STOP_ON_FAILURE` If the cancel request fails, the new order placement will not be attempted.<br>- `ALLOW_FAILURES` If new order placement will be attempted even if cancel request fails. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>cancel_restrictions</code> | <code>[CancelRestrictionsOrStr](binance/models/enums/cancel_restrictions.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>time_in_force</code> | <code>[TimeInForceOrStr](binance/models/enums/time_in_force.py) \| None</code> | Order time in force<br>**Default**: <code>None</code> |
| <code>quantity</code> | <code>float \| None</code> | Order quantity<br>**Default**: <code>None</code> |
| <code>quote_order_qty</code> | <code>float \| None</code> | Quote quantity<br>**Default**: <code>None</code> |
| <code>price</code> | <code>float \| None</code> | Order price<br>**Default**: <code>None</code> |
| <code>cancel_new_client_order_id</code> | <code>str \| None</code> | Used to uniquely identify this cancel. Automatically generated by default<br>**Default**: <code>None</code> |
| <code>cancel_orig_client_order_id</code> | <code>str \| None</code> | Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both are provided, cancelOrderId takes precedence.<br>**Default**: <code>None</code> |
| <code>cancel_order_id</code> | <code>int \| None</code> | Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both are provided, cancelOrderId takes precedence.<br>**Default**: <code>None</code> |
| <code>new_client_order_id</code> | <code>str \| None</code> | Used to uniquely identify this cancel. Automatically generated by default<br>**Default**: <code>None</code> |
| <code>strategy_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>strategy_type</code> | <code>int \| None</code> | The value cannot be less than 1000000.<br>**Default**: <code>None</code> |
| <code>stop_price</code> | <code>float \| None</code> | Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.<br>**Default**: <code>None</code> |
| <code>trailing_delta</code> | <code>float \| None</code> | Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.<br>**Default**: <code>None</code> |
| <code>iceberg_qty</code> | <code>float \| None</code> | Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.<br>**Default**: <code>None</code> |
| <code>new_order_resp_type</code> | <code>[NewOrderRespTypeOrStr](binance/models/enums/new_order_resp_type.py) \| None</code> | Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK.<br>**Default**: <code>None</code> |
| <code>self_trade_prevention_mode</code> | <code>[SelfTradePreventionModeOrStr](binance/models/enums/self_trade_prevention_mode.py) \| None</code> | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3OrderCancelReplaceResponse](binance/models/api_v3_order_cancel_replace_response.py)</code> -- Operation details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CancelAnExistingOrderAndSendANewOrderTradeErrorBody](binance/errors/cancel_an_existing_order_and_send_a_new_order_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def current_open_orders_user_data(timestamp: int, signature: str, *, symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[OrderDetails]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get all open orders on a symbol. Careful when accessing this with no symbol.

Weight(IP):
- `6` for a single symbol;
- `80` when the symbol parameter is omitted;

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.current_open_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[OrderDetails]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CurrentOpenOrdersUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.current_open_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[OrderDetails]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CurrentOpenOrdersUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>symbol</code> | <code>str \| None</code> | Trading symbol, e.g. BNBUSDT<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[OrderDetails](binance/models/order_details.py)&#93;</code> -- Current open orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CurrentOpenOrdersUserDataErrorBody](binance/errors/current_open_orders_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def new_order_trade(symbol: str, side: SideOrStr, type_: Type1OrStr, timestamp: int, signature: str, *, time_in_force: TimeInForceOrStr | None = None, quantity: float | None = None, quote_order_qty: float | None = None, price: float | None = None, new_client_order_id: str | None = None, strategy_id: int | None = None, strategy_type: int | None = None, stop_price: float | None = None, trailing_delta: float | None = None, iceberg_qty: float | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiV3OrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send in a new order.

- `LIMIT_MAKER` are `LIMIT` orders that will be rejected if they would immediately match and trade as a taker.
- `STOP_LOSS` and `TAKE_PROFIT` will execute a `MARKET` order when the `stopPrice` is reached.
- Any `LIMIT` or `LIMIT_MAKER` type order can be made an iceberg order by sending an `icebergQty`.
- Any order with an `icebergQty` MUST have `timeInForce` set to `GTC`.
- `MARKET` orders using `quantity` specifies how much a user wants to buy or sell based on the market price.
- `MARKET` orders using `quoteOrderQty` specifies the amount the user wants to spend (when buying) or receive (when selling) of the quote asset; the correct quantity will be determined based on the market liquidity and `quoteOrderQty`.
- `MARKET` orders using `quoteOrderQty` will not break `LOT_SIZE` filter rules; the order will execute a quantity that will have the notional value as close as possible to `quoteOrderQty`.
- same `newClientOrderId` can be accepted only when the previous one is filled, otherwise the order will be rejected.

Trigger order price rules against market price for both `MARKET` and `LIMIT` versions:

- Price above market price: `STOP_LOSS` `BUY`, `TAKE_PROFIT` `SELL`
- Price below market price: `STOP_LOSS` `SELL`, `TAKE_PROFIT` `BUY`


Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.new_order_trade(symbol, side, type_, timestamp, signature)
    # TODO: Handle 'response' of type ApiV3OrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type NewOrderTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.new_order_trade(symbol, side, type_, timestamp, signature)
    # TODO: Handle 'response' of type ApiV3OrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type NewOrderTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>side</code> | <code>[SideOrStr](binance/models/enums/side.py)</code> | Value sent with the request. |
| <code>type_</code> | <code>[Type1OrStr](binance/models/enums/type1.py)</code> | Order type |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>time_in_force</code> | <code>[TimeInForceOrStr](binance/models/enums/time_in_force.py) \| None</code> | Order time in force<br>**Default**: <code>None</code> |
| <code>quantity</code> | <code>float \| None</code> | Order quantity<br>**Default**: <code>None</code> |
| <code>quote_order_qty</code> | <code>float \| None</code> | Quote quantity<br>**Default**: <code>None</code> |
| <code>price</code> | <code>float \| None</code> | Order price<br>**Default**: <code>None</code> |
| <code>new_client_order_id</code> | <code>str \| None</code> | Used to uniquely identify this cancel. Automatically generated by default<br>**Default**: <code>None</code> |
| <code>strategy_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>strategy_type</code> | <code>int \| None</code> | The value cannot be less than 1000000.<br>**Default**: <code>None</code> |
| <code>stop_price</code> | <code>float \| None</code> | Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.<br>**Default**: <code>None</code> |
| <code>trailing_delta</code> | <code>float \| None</code> | Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.<br>**Default**: <code>None</code> |
| <code>iceberg_qty</code> | <code>float \| None</code> | Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.<br>**Default**: <code>None</code> |
| <code>new_order_resp_type</code> | <code>[NewOrderRespTypeOrStr](binance/models/enums/new_order_resp_type.py) \| None</code> | Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK.<br>**Default**: <code>None</code> |
| <code>self_trade_prevention_mode</code> | <code>[SelfTradePreventionModeOrStr](binance/models/enums/self_trade_prevention_mode.py) \| None</code> | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3OrderResponse](binance/models/unions/api_v3_order_response.py)</code> -- Order result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[NewOrderTradeErrorBody](binance/errors/new_order_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def new_order_list_oto_trade(symbol: str, working_type: WorkingTypeOrStr, working_side: WorkingSideOrStr, working_price: float, working_quantity: float, working_iceberg_qty: float, pending_type: PendingTypeOrStr, pending_side: PendingSideOrStr, pending_quantity: float, timestamp: int, signature: str, *, list_client_order_id: str | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, working_client_order_id: str | None = None, working_time_in_force: WorkingTimeInForceOrStr | None = None, working_strategy_id: float | None = None, working_strategy_type: int | None = None, pending_client_order_id: str | None = None, pending_price: float | None = None, pending_stop_price: float | None = None, pending_trailing_delta: float | None = None, pending_iceberg_qty: float | None = None, pending_time_in_force: PendingTimeInForceOrStr | None = None, pending_strategy_id: float | None = None, pending_strategy_type: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiV3OrderListOtoResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Places an `OTO`.
- An `OTO` (One-Triggers-the-Other) is an order list comprised of 2 orders.
- The first order is called the working order and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the working order goes on the order book.
- The second order is called the pending order. It can be any order type except for `MARKET` orders using parameter `quoteOrderQty`. The pending order is only placed on the order book when the working order gets fully filled.
- If either the working order or the pending order is cancelled individually, the other order in the order list will also be canceled or expired.
- When the order list is placed, if the working order gets immediately fully filled, the placement response will show the working order as `FILLED` but the pending order will still appear as `PENDING_NEW`. You need to query the status of the pending order again to see its updated status.
- OTOs add 2 orders to the unfilled order count, `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.

Weight: 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.new_order_list_oto_trade(
        symbol,
        working_type,
        working_side,
        working_price,
        working_quantity,
        working_iceberg_qty,
        pending_type,
        pending_side,
        pending_quantity,
        timestamp,
        signature,
    )
    # TODO: Handle 'response' of type ApiV3OrderListOtoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type NewOrderListOtoTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.new_order_list_oto_trade(
        symbol,
        working_type,
        working_side,
        working_price,
        working_quantity,
        working_iceberg_qty,
        pending_type,
        pending_side,
        pending_quantity,
        timestamp,
        signature,
    )
    # TODO: Handle 'response' of type ApiV3OrderListOtoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type NewOrderListOtoTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>working_type</code> | <code>[WorkingTypeOrStr](binance/models/enums/working_type.py)</code> | Supported values: LIMIT,LIMIT_MAKER |
| <code>working_side</code> | <code>[WorkingSideOrStr](binance/models/enums/working_side.py)</code> | BUY,SELL |
| <code>working_price</code> | <code>float</code> | Value sent with the request. |
| <code>working_quantity</code> | <code>float</code> | Sets the quantity for the working order. |
| <code>working_iceberg_qty</code> | <code>float</code> | This can only be used if workingTimeInForce is GTC. |
| <code>pending_type</code> | <code>[PendingTypeOrStr](binance/models/enums/pending_type.py)</code> | Supported values: Order Types Note that MARKET orders using quoteOrderQty are not supported. |
| <code>pending_side</code> | <code>[PendingSideOrStr](binance/models/enums/pending_side.py)</code> | BUY,SELL |
| <code>pending_quantity</code> | <code>float</code> | Sets the quantity for the pending order. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>list_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open order lists. Automatically generated if not sent.<br>A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired.<br>`listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.<br>**Default**: <code>None</code> |
| <code>new_order_resp_type</code> | <code>[NewOrderRespTypeOrStr](binance/models/enums/new_order_resp_type.py) \| None</code> | Set the response JSON.<br>**Default**: <code>None</code> |
| <code>self_trade_prevention_mode</code> | <code>[SelfTradePreventionModeOrStr](binance/models/enums/self_trade_prevention_mode.py) \| None</code> | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.<br>**Default**: <code>None</code> |
| <code>working_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.<br>**Default**: <code>None</code> |
| <code>working_time_in_force</code> | <code>[WorkingTimeInForceOrStr](binance/models/enums/working_time_in_force.py) \| None</code> | GTC, IOC, FOK<br>**Default**: <code>None</code> |
| <code>working_strategy_id</code> | <code>float \| None</code> | Arbitrary numeric value identifying the working order within an order strategy.<br>**Default**: <code>None</code> |
| <code>working_strategy_type</code> | <code>int \| None</code> | Arbitrary numeric value identifying the working order strategy.<br>Values smaller than 1000000 are reserved and cannot be used.<br>**Default**: <code>None</code> |
| <code>pending_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent.<br>**Default**: <code>None</code> |
| <code>pending_price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_stop_price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_trailing_delta</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_iceberg_qty</code> | <code>float \| None</code> | This can only be used if pendingTimeInForce is GTC.<br>**Default**: <code>None</code> |
| <code>pending_time_in_force</code> | <code>[PendingTimeInForceOrStr](binance/models/enums/pending_time_in_force.py) \| None</code> | GTC, IOC, FOK<br>**Default**: <code>None</code> |
| <code>pending_strategy_id</code> | <code>float \| None</code> | Arbitrary numeric value identifying the pending order within an order strategy.<br>**Default**: <code>None</code> |
| <code>pending_strategy_type</code> | <code>int \| None</code> | Arbitrary numeric value identifying the pending order strategy.<br>Values smaller than 1000000 are reserved and cannot be used.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3OrderListOtoResponse](binance/models/api_v3_order_list_oto_response.py)</code> -- New OTO details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[NewOrderListOtoTradeErrorBody](binance/errors/new_order_list_oto_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def new_order_list_otoco_trade(symbol: str, working_type: WorkingTypeOrStr, working_side: WorkingSideOrStr, working_price: float, working_quantity: float, working_iceberg_qty: float, pending_side: PendingSideOrStr, pending_quantity: float, pending_above_type: PendingAboveTypeOrStr, timestamp: int, signature: str, *, list_client_order_id: str | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, working_client_order_id: str | None = None, working_time_in_force: WorkingTimeInForceOrStr | None = None, working_strategy_id: float | None = None, working_strategy_type: int | None = None, pending_above_client_order_id: str | None = None, pending_above_price: float | None = None, pending_above_stop_price: float | None = None, pending_above_trailing_delta: float | None = None, pending_above_iceberg_qty: float | None = None, pending_above_time_in_force: PendingAboveTimeInForceOrStr | None = None, pending_above_strategy_id: float | None = None, pending_above_strategy_type: int | None = None, pending_below_type: PendingBelowTypeOrStr | None = None, pending_below_client_order_id: str | None = None, pending_below_price: float | None = None, pending_below_stop_price: float | None = None, pending_below_trailing_delta: float | None = None, pending_below_iceberg_qty: float | None = None, pending_below_time_in_force: PendingBelowTimeInForceOrStr | None = None, pending_below_strategy_id: float | None = None, pending_below_strategy_type: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiV3OrderListOtocoResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Place an `OTOCO`.
- An `OTOCO` (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.
- The first order is called the working order and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the working order goes on the order book.
  - The behavior of the working order is the same as the `OTO`.
- `OTOCO` has 2 pending orders (pending above and pending below), forming an `OCO` pair. The pending orders are only placed on the order book when the working order gets fully filled.
  - The rules of the pending above and pending below follow the same rules as the Order List `OCO`.
- OTOCOs add 3 orders against the unfilled order count, `EXCHANGE_MAX_NUM_ORDERS` filter, and `MAX_NUM_ORDERS` filter.

Weight: 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.new_order_list_otoco_trade(
        symbol,
        working_type,
        working_side,
        working_price,
        working_quantity,
        working_iceberg_qty,
        pending_side,
        pending_quantity,
        pending_above_type,
        timestamp,
        signature,
    )
    # TODO: Handle 'response' of type ApiV3OrderListOtocoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type NewOrderListOtocoTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.new_order_list_otoco_trade(
        symbol,
        working_type,
        working_side,
        working_price,
        working_quantity,
        working_iceberg_qty,
        pending_side,
        pending_quantity,
        pending_above_type,
        timestamp,
        signature,
    )
    # TODO: Handle 'response' of type ApiV3OrderListOtocoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type NewOrderListOtocoTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>working_type</code> | <code>[WorkingTypeOrStr](binance/models/enums/working_type.py)</code> | Supported values: LIMIT,LIMIT_MAKER |
| <code>working_side</code> | <code>[WorkingSideOrStr](binance/models/enums/working_side.py)</code> | BUY,SELL |
| <code>working_price</code> | <code>float</code> | Value sent with the request. |
| <code>working_quantity</code> | <code>float</code> | Sets the quantity for the working order. |
| <code>working_iceberg_qty</code> | <code>float</code> | This can only be used if workingTimeInForce is GTC. |
| <code>pending_side</code> | <code>[PendingSideOrStr](binance/models/enums/pending_side.py)</code> | BUY,SELL |
| <code>pending_quantity</code> | <code>float</code> | Sets the quantity for the pending order. |
| <code>pending_above_type</code> | <code>[PendingAboveTypeOrStr](binance/models/enums/pending_above_type.py)</code> | Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>list_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open order lists. Automatically generated if not sent.<br>A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired.<br>`listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.<br>**Default**: <code>None</code> |
| <code>new_order_resp_type</code> | <code>[NewOrderRespTypeOrStr](binance/models/enums/new_order_resp_type.py) \| None</code> | Set the response JSON.<br>**Default**: <code>None</code> |
| <code>self_trade_prevention_mode</code> | <code>[SelfTradePreventionModeOrStr](binance/models/enums/self_trade_prevention_mode.py) \| None</code> | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.<br>**Default**: <code>None</code> |
| <code>working_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.<br>**Default**: <code>None</code> |
| <code>working_time_in_force</code> | <code>[WorkingTimeInForceOrStr](binance/models/enums/working_time_in_force.py) \| None</code> | GTC, IOC, FOK<br>**Default**: <code>None</code> |
| <code>working_strategy_id</code> | <code>float \| None</code> | Arbitrary numeric value identifying the working order within an order strategy.<br>**Default**: <code>None</code> |
| <code>working_strategy_type</code> | <code>int \| None</code> | Arbitrary numeric value identifying the working order strategy.<br>Values smaller than 1000000 are reserved and cannot be used.<br>**Default**: <code>None</code> |
| <code>pending_above_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent.<br>**Default**: <code>None</code> |
| <code>pending_above_price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_above_stop_price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_above_trailing_delta</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_above_iceberg_qty</code> | <code>float \| None</code> | This can only be used if pendingAboveTimeInForce is GTC.<br>**Default**: <code>None</code> |
| <code>pending_above_time_in_force</code> | <code>[PendingAboveTimeInForceOrStr](binance/models/enums/pending_above_time_in_force.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_above_strategy_id</code> | <code>float \| None</code> | Arbitrary numeric value identifying the pending above order within an order strategy.<br>**Default**: <code>None</code> |
| <code>pending_above_strategy_type</code> | <code>int \| None</code> | Arbitrary numeric value identifying the pending above order strategy.<br>Values smaller than 1000000 are reserved and cannot be used.<br>**Default**: <code>None</code> |
| <code>pending_below_type</code> | <code>[PendingBelowTypeOrStr](binance/models/enums/pending_below_type.py) \| None</code> | Supported values: LIMIT_MAKER, STOP_LOSS, and STOP_LOSS_LIMIT<br>**Default**: <code>None</code> |
| <code>pending_below_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent.<br>**Default**: <code>None</code> |
| <code>pending_below_price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_below_stop_price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_below_trailing_delta</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_below_iceberg_qty</code> | <code>float \| None</code> | This can only be used if pendingBelowTimeInForce is GTC.<br>**Default**: <code>None</code> |
| <code>pending_below_time_in_force</code> | <code>[PendingBelowTimeInForceOrStr](binance/models/enums/pending_below_time_in_force.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pending_below_strategy_id</code> | <code>float \| None</code> | Arbitrary numeric value identifying the pending below order within an order strategy.<br>**Default**: <code>None</code> |
| <code>pending_below_strategy_type</code> | <code>int \| None</code> | Arbitrary numeric value identifying the pending below order strategy.<br>Values smaller than 1000000 are reserved and cannot be used.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3OrderListOtocoResponse](binance/models/api_v3_order_list_otoco_response.py)</code> -- New OTOCO details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[NewOrderListOtocoTradeErrorBody](binance/errors/new_order_list_otoco_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def new_order_list_oco_trade(symbol: str, side: SideOrStr, quantity: float, above_type: str, below_type: str, timestamp: int, signature: str, *, list_client_order_id: str | None = None, above_client_order_id: str | None = None, above_iceberg_qty: float | None = None, above_price: float | None = None, above_stop_price: float | None = None, above_trailing_delta: float | None = None, above_time_in_force: AboveTimeInForceOrStr | None = None, above_strategy_id: float | None = None, above_strategy_type: int | None = None, below_client_order_id: str | None = None, below_iceberg_qty: float | None = None, below_price: float | None = None, below_stop_price: float | None = None, below_trailing_delta: float | None = None, below_time_in_force: BelowTimeInForceOrStr | None = None, below_strategy_id: float | None = None, below_strategy_type: int | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiV3OrderListOcoResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.

- An `OCO` has 2 orders called the above order and below order.
- One of the orders must be a `LIMIT_MAKER` order and the other must be `STOP_LOSS` or`STOP_LOSS_LIMIT` order.
- Price restrictions:
    - If the `OCO` is on the `SELL` side: `LIMIT_MAKER` price > Last Traded Price > stopPrice
    - If the `OCO` is on the `BUY` side: `LIMIT_MAKER` price < Last Traded Price < stopPrice
- OCOs add 2 orders to the unfilled order count, `EXCHANGE_MAX_ORDERS` filter, and the `MAX_NUM_ORDERS` filter.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.new_order_list_oco_trade(
        symbol, side, quantity, above_type, below_type, timestamp, signature
    )
    # TODO: Handle 'response' of type ApiV3OrderListOcoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type NewOrderListOcoTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.new_order_list_oco_trade(
        symbol, side, quantity, above_type, below_type, timestamp, signature
    )
    # TODO: Handle 'response' of type ApiV3OrderListOcoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type NewOrderListOcoTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>side</code> | <code>[SideOrStr](binance/models/enums/side.py)</code> | Value sent with the request. |
| <code>quantity</code> | <code>float</code> | Value sent with the request. |
| <code>above_type</code> | <code>str</code> | Supported values : `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER` |
| <code>below_type</code> | <code>str</code> | Supported values : `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER` |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>list_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open order lists. Automatically generated if not sent.<br>A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired.<br>`listClientOrderId` is distinct from the `aboveClientOrderId` and the `belowCLientOrderId`.<br>**Default**: <code>None</code> |
| <code>above_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open orders for the above order. Automatically generated if not sent<br>**Default**: <code>None</code> |
| <code>above_iceberg_qty</code> | <code>float \| None</code> | Note that this can only be used if `aboveTimeInForce` is `GTC`.<br>**Default**: <code>None</code> |
| <code>above_price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>above_stop_price</code> | <code>float \| None</code> | Can be used if `aboveType` is `STOP_LOSS` or `STOP_LOSS_LIMIT`.<br>Either `aboveStopPrice` or `aboveTrailingDelta` or both, must be specified.<br>**Default**: <code>None</code> |
| <code>above_trailing_delta</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>above_time_in_force</code> | <code>[AboveTimeInForceOrStr](binance/models/enums/above_time_in_force.py) \| None</code> | Required if the `aboveType` is `STOP_LOSS_LIMIT`.<br>**Default**: <code>None</code> |
| <code>above_strategy_id</code> | <code>float \| None</code> | Arbitrary numeric value identifying the above order within an order strategy.<br>**Default**: <code>None</code> |
| <code>above_strategy_type</code> | <code>int \| None</code> | Arbitrary numeric value identifying the above order strategy.<br>Values smaller than 1000000 are reserved and cannot be used.<br>**Default**: <code>None</code> |
| <code>below_client_order_id</code> | <code>str \| None</code> | Arbitrary unique ID among open orders for the below order. Automatically generated if not sent<br>**Default**: <code>None</code> |
| <code>below_iceberg_qty</code> | <code>float \| None</code> | Note that this can only be used if `belowTimeInForce` is `GTC`.<br>**Default**: <code>None</code> |
| <code>below_price</code> | <code>float \| None</code> | Can be used if `belowType` is `STOP_LOSS_LIMIT` or `LIMIT_MAKER` to specify the limit price.<br>**Default**: <code>None</code> |
| <code>below_stop_price</code> | <code>float \| None</code> | Can be used if `belowType` is `STOP_LOSS` or `STOP_LOSS_LIMIT`.<br>Either `belowStopPrice` or `belowTrailingDelta` or both, must be specified.<br>**Default**: <code>None</code> |
| <code>below_trailing_delta</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>below_time_in_force</code> | <code>[BelowTimeInForceOrStr](binance/models/enums/below_time_in_force.py) \| None</code> | Required if the `belowType` is `STOP_LOSS_LIMIT`.<br>**Default**: <code>None</code> |
| <code>below_strategy_id</code> | <code>float \| None</code> | Arbitrary numeric value identifying the below order within an order strategy.<br>**Default**: <code>None</code> |
| <code>below_strategy_type</code> | <code>int \| None</code> | Arbitrary numeric value identifying the below order strategy.<br>Values smaller than 1000000 are reserved and cannot be used.<br>**Default**: <code>None</code> |
| <code>new_order_resp_type</code> | <code>[NewOrderRespTypeOrStr](binance/models/enums/new_order_resp_type.py) \| None</code> | Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK.<br>**Default**: <code>None</code> |
| <code>self_trade_prevention_mode</code> | <code>[SelfTradePreventionModeOrStr](binance/models/enums/self_trade_prevention_mode.py) \| None</code> | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3OrderListOcoResponse](binance/models/api_v3_order_list_oco_response.py)</code> -- New OCO details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[NewOrderListOcoTradeErrorBody](binance/errors/new_order_list_oco_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def new_order_using_sor_trade(symbol: str, side: SideOrStr, type_: Type1OrStr, quantity: float, timestamp: int, signature: str, *, time_in_force: TimeInForceOrStr | None = None, price: float | None = None, new_client_order_id: str | None = None, strategy_id: int | None = None, strategy_type: int | None = None, iceberg_qty: float | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiV3SorOrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 6

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.new_order_using_sor_trade(symbol, side, type_, quantity, timestamp, signature)
    # TODO: Handle 'response' of type ApiV3SorOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type NewOrderUsingSorTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.new_order_using_sor_trade(
        symbol, side, type_, quantity, timestamp, signature
    )
    # TODO: Handle 'response' of type ApiV3SorOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type NewOrderUsingSorTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>side</code> | <code>[SideOrStr](binance/models/enums/side.py)</code> | Value sent with the request. |
| <code>type_</code> | <code>[Type1OrStr](binance/models/enums/type1.py)</code> | Order type |
| <code>quantity</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>time_in_force</code> | <code>[TimeInForceOrStr](binance/models/enums/time_in_force.py) \| None</code> | Order time in force<br>**Default**: <code>None</code> |
| <code>price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>new_client_order_id</code> | <code>str \| None</code> | Used to uniquely identify this cancel. Automatically generated by default<br>**Default**: <code>None</code> |
| <code>strategy_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>strategy_type</code> | <code>int \| None</code> | The value cannot be less than 1000000.<br>**Default**: <code>None</code> |
| <code>iceberg_qty</code> | <code>float \| None</code> | Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.<br>**Default**: <code>None</code> |
| <code>new_order_resp_type</code> | <code>[NewOrderRespTypeOrStr](binance/models/enums/new_order_resp_type.py) \| None</code> | Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK.<br>**Default**: <code>None</code> |
| <code>self_trade_prevention_mode</code> | <code>[SelfTradePreventionModeOrStr](binance/models/enums/self_trade_prevention_mode.py) \| None</code> | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3SorOrderResponse](binance/models/api_v3_sor_order_response.py)</code> -- New order details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[NewOrderUsingSorTradeErrorBody](binance/errors/new_order_using_sor_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_allocations_user_data(symbol: str, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, from_allocation_id: int | None = None, limit: int | None = None, order_id: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[ApiV3MyAllocationsResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves allocations resulting from SOR order placement.

Weight: 20

Supported parameter combinations:
Parameters                               Response
symbol                                   allocations from oldest to newest
symbol + startTime                       oldest allocations since startTime
symbol + endTime                         newest allocations until endTime
symbol + startTime + endTime             allocations within the time range
symbol + fromAllocationId               allocations by allocation ID
symbol + orderId                         allocations related to an order starting with oldest
symbol + orderId + fromAllocationId     allocations related to an order by allocation ID

Note: The time between startTime and endTime can't be longer than 24 hours.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.query_allocations_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[ApiV3MyAllocationsResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryAllocationsUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.query_allocations_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[ApiV3MyAllocationsResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryAllocationsUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>from_allocation_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>order_id</code> | <code>int \| None</code> | Order id<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ApiV3MyAllocationsResponse](binance/models/api_v3_my_allocations_response.py)&#93;</code> -- Allocations resulting from SOR order placement

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryAllocationsUserDataErrorBody](binance/errors/query_allocations_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_commission_rates_user_data(symbol: str, timestamp: int, signature: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiV3AccountCommissionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get current account commission rates.

Weight: 20

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.query_commission_rates_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type ApiV3AccountCommissionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryCommissionRatesUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.query_commission_rates_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type ApiV3AccountCommissionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryCommissionRatesUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3AccountCommissionResponse](binance/models/api_v3_account_commission_response.py)</code> -- Current account commission rates.

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryCommissionRatesUserDataErrorBody](binance/errors/query_commission_rates_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_current_order_count_usage_trade(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[ApiV3RateLimitOrderResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Displays the user's current order count usage for all intervals.

Weight(IP): 40

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.query_current_order_count_usage_trade(timestamp, signature)
    # TODO: Handle 'response' of type list[ApiV3RateLimitOrderResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryCurrentOrderCountUsageTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.query_current_order_count_usage_trade(timestamp, signature)
    # TODO: Handle 'response' of type list[ApiV3RateLimitOrderResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryCurrentOrderCountUsageTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ApiV3RateLimitOrderResponse](binance/models/api_v3_rate_limit_order_response.py)&#93;</code> -- Order rate limits

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryCurrentOrderCountUsageTradeErrorBody](binance/errors/query_current_order_count_usage_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_oco_user_data(timestamp: int, signature: str, *, order_list_id: int | None = None, orig_client_order_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiV3OrderListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a specific OCO based on provided optional parameters

Weight(IP): 4

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.query_oco_user_data(timestamp, signature)
    # TODO: Handle 'response' of type ApiV3OrderListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryOcoUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.query_oco_user_data(timestamp, signature)
    # TODO: Handle 'response' of type ApiV3OrderListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryOcoUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_list_id</code> | <code>int \| None</code> | Order list id<br>**Default**: <code>None</code> |
| <code>orig_client_order_id</code> | <code>str \| None</code> | Order id from client<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiV3OrderListResponse](binance/models/api_v3_order_list_response.py)</code> -- OCO details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryOcoUserDataErrorBody](binance/errors/query_oco_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_open_oco_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[ApiV3OpenOrderListResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 6

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.query_open_oco_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[ApiV3OpenOrderListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryOpenOcoUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.query_open_oco_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[ApiV3OpenOrderListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryOpenOcoUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ApiV3OpenOrderListResponse](binance/models/api_v3_open_order_list_response.py)&#93;</code> -- List of OCO orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryOpenOcoUserDataErrorBody](binance/errors/query_open_oco_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_order_user_data(symbol: str, timestamp: int, signature: str, *, order_id: int | None = None, orig_client_order_id: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> OrderDetails</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check an order's status.

- Either `orderId` or `origClientOrderId` must be sent.
- For some historical orders `cummulativeQuoteQty` will be < 0, meaning the data is not available at this time.

Weight(IP): 4

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.query_order_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type OrderDetails
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryOrderUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.query_order_user_data(symbol, timestamp, signature)
    # TODO: Handle 'response' of type OrderDetails
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryOrderUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>int \| None</code> | Order id<br>**Default**: <code>None</code> |
| <code>orig_client_order_id</code> | <code>str \| None</code> | Order id from client<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[OrderDetails](binance/models/order_details.py)</code> -- Order details

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryOrderUserDataErrorBody](binance/errors/query_order_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_prevented_matches(symbol: str, timestamp: int, signature: str, *, prevented_match_id: int | None = None, order_id: int | None = None, from_prevented_match_id: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[ApiV3MyPreventedMatchesResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Displays the list of orders that were expired because of STP.

For additional information on what a Prevented match is, as well as Self Trade Prevention (STP), please refer to our STP FAQ page.

These are the combinations supported:

* symbol + preventedMatchId
* symbol + orderId
* symbol + orderId + fromPreventedMatchId (limit will default to 500)
* symbol + orderId + fromPreventedMatchId + limit

Weight(IP):

Case                               Weight
If symbol is invalid:             2
Querying by preventedMatchId:     2
Querying by orderId:               20

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.query_prevented_matches(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[ApiV3MyPreventedMatchesResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryPreventedMatchesErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.query_prevented_matches(symbol, timestamp, signature)
    # TODO: Handle 'response' of type list[ApiV3MyPreventedMatchesResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryPreventedMatchesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>prevented_match_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>order_id</code> | <code>int \| None</code> | Order id<br>**Default**: <code>None</code> |
| <code>from_prevented_match_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ApiV3MyPreventedMatchesResponse](binance/models/api_v3_my_prevented_matches_response.py)&#93;</code> -- Order list that were expired due to STP

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryPreventedMatchesErrorBody](binance/errors/query_prevented_matches_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_all_oco_user_data(timestamp: int, signature: str, *, from_id: int | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[ApiV3AllOrderListResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves all OCO based on provided optional parameters

Weight(IP): 20

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.query_all_oco_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[ApiV3AllOrderListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryAllOcoUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.query_all_oco_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[ApiV3AllOrderListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryAllOcoUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>from_id</code> | <code>int \| None</code> | Trade id to fetch from. Default gets most recent trades.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ApiV3AllOrderListResponse](binance/models/api_v3_all_order_list_response.py)&#93;</code> -- List of OCO orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryAllOcoUserDataErrorBody](binance/errors/query_all_oco_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def test_new_order_trade(symbol: str, side: SideOrStr, type_: Type1OrStr, timestamp: int, signature: str, *, time_in_force: TimeInForceOrStr | None = None, quantity: float | None = None, quote_order_qty: float | None = None, price: float | None = None, new_client_order_id: str | None = None, strategy_id: int | None = None, strategy_type: int | None = None, stop_price: float | None = None, trailing_delta: float | None = None, iceberg_qty: float | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, recv_window: int | None = None, compute_commission_rates: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Test new order creation and signature/recvWindow long.
Creates and validates a new order but does not send it into the matching engine.

Weight(IP):
  - Without computeCommissionRates: `1`
  - With computeCommissionRates: `20`

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.test_new_order_trade(symbol, side, type_, timestamp, signature)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TestNewOrderTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.test_new_order_trade(symbol, side, type_, timestamp, signature)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TestNewOrderTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>side</code> | <code>[SideOrStr](binance/models/enums/side.py)</code> | Value sent with the request. |
| <code>type_</code> | <code>[Type1OrStr](binance/models/enums/type1.py)</code> | Order type |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>time_in_force</code> | <code>[TimeInForceOrStr](binance/models/enums/time_in_force.py) \| None</code> | Order time in force<br>**Default**: <code>None</code> |
| <code>quantity</code> | <code>float \| None</code> | Order quantity<br>**Default**: <code>None</code> |
| <code>quote_order_qty</code> | <code>float \| None</code> | Quote quantity<br>**Default**: <code>None</code> |
| <code>price</code> | <code>float \| None</code> | Order price<br>**Default**: <code>None</code> |
| <code>new_client_order_id</code> | <code>str \| None</code> | Used to uniquely identify this cancel. Automatically generated by default<br>**Default**: <code>None</code> |
| <code>strategy_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>strategy_type</code> | <code>int \| None</code> | The value cannot be less than 1000000.<br>**Default**: <code>None</code> |
| <code>stop_price</code> | <code>float \| None</code> | Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.<br>**Default**: <code>None</code> |
| <code>trailing_delta</code> | <code>float \| None</code> | Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.<br>**Default**: <code>None</code> |
| <code>iceberg_qty</code> | <code>float \| None</code> | Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.<br>**Default**: <code>None</code> |
| <code>new_order_resp_type</code> | <code>[NewOrderRespTypeOrStr](binance/models/enums/new_order_resp_type.py) \| None</code> | Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>compute_commission_rates</code> | <code>bool \| None</code> | Default: false<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[TestNewOrderTradeErrorBody](binance/errors/test_new_order_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def test_new_order_using_sor_trade(symbol: str, side: SideOrStr, type_: Type1OrStr, quantity: float, timestamp: int, signature: str, *, time_in_force: TimeInForceOrStr | None = None, price: float | None = None, new_client_order_id: str | None = None, strategy_id: int | None = None, strategy_type: int | None = None, iceberg_qty: float | None = None, new_order_resp_type: NewOrderRespTypeOrStr | None = None, self_trade_prevention_mode: SelfTradePreventionModeOrStr | None = None, compute_commission_rates: bool | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Test new order creation and signature/recvWindow using smart order routing (SOR).
Creates and validates a new order but does not send it into the matching engine.

Weight(IP):
  - Without computeCommissionRates: `1`
  - With computeCommissionRates: `20`

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trade_api.test_new_order_using_sor_trade(symbol, side, type_, quantity, timestamp, signature)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TestNewOrderUsingSorTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.trade_api.test_new_order_using_sor_trade(
        symbol, side, type_, quantity, timestamp, signature
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TestNewOrderUsingSorTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Trading symbol, e.g. BNBUSDT |
| <code>side</code> | <code>[SideOrStr](binance/models/enums/side.py)</code> | Value sent with the request. |
| <code>type_</code> | <code>[Type1OrStr](binance/models/enums/type1.py)</code> | Order type |
| <code>quantity</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>time_in_force</code> | <code>[TimeInForceOrStr](binance/models/enums/time_in_force.py) \| None</code> | Order time in force<br>**Default**: <code>None</code> |
| <code>price</code> | <code>float \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>new_client_order_id</code> | <code>str \| None</code> | Used to uniquely identify this cancel. Automatically generated by default<br>**Default**: <code>None</code> |
| <code>strategy_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>strategy_type</code> | <code>int \| None</code> | The value cannot be less than 1000000.<br>**Default**: <code>None</code> |
| <code>iceberg_qty</code> | <code>float \| None</code> | Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.<br>**Default**: <code>None</code> |
| <code>new_order_resp_type</code> | <code>[NewOrderRespTypeOrStr](binance/models/enums/new_order_resp_type.py) \| None</code> | Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK.<br>**Default**: <code>None</code> |
| <code>self_trade_prevention_mode</code> | <code>[SelfTradePreventionModeOrStr](binance/models/enums/self_trade_prevention_mode.py) \| None</code> | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE.<br>**Default**: <code>None</code> |
| <code>compute_commission_rates</code> | <code>bool \| None</code> | Default: false<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Test new order

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[TestNewOrderUsingSorTradeErrorBody](binance/errors/test_new_order_using_sor_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## VipLoans

> Source: [VipLoans](binance/apis/vip_loans.py)

<details>
<summary><code>def check_locked_value_of_vip_collateral_account_user_data(timestamp: int, signature: str, *, order_id: int | None = None, collateral_account_id: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanVipCollateralAccountResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

VIP loan is available for VIP users only.

Weight(IP): 6000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vip_loans.check_locked_value_of_vip_collateral_account_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipCollateralAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckLockedValueOfVipCollateralAccountUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.vip_loans.check_locked_value_of_vip_collateral_account_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipCollateralAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckLockedValueOfVipCollateralAccountUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>int \| None</code> | Order id<br>**Default**: <code>None</code> |
| <code>collateral_account_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanVipCollateralAccountResponse](binance/models/sapi_v1_loan_vip_collateral_account_response.py)</code> -- VIP Locked Value

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[CheckLockedValueOfVipCollateralAccountUserDataErrorBody](binance/errors/check_locked_value_of_vip_collateral_account_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_borrow_interest_rate_user_data(timestamp: int, signature: str, *, loan_coin: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1LoanVipRequestInterestRateResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get borrow interest rate.

Weight(UID): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vip_loans.get_borrow_interest_rate_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1LoanVipRequestInterestRateResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBorrowInterestRateUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.vip_loans.get_borrow_interest_rate_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1LoanVipRequestInterestRateResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBorrowInterestRateUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>loan_coin</code> | <code>str \| None</code> | Max 10 assets, Multiple split by ","<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1LoanVipRequestInterestRateResponse](binance/models/sapi_v1_loan_vip_request_interest_rate_response.py)&#93;</code> -- Borrow interest rate

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetBorrowInterestRateUserDataErrorBody](binance/errors/get_borrow_interest_rate_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_collateral_asset_data_user_data(timestamp: int, signature: str, *, collateral_coin: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanVipCollateralDataResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get collateral asset data.

Weight(IP): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vip_loans.get_collateral_asset_data_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipCollateralDataResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCollateralAssetDataUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.vip_loans.get_collateral_asset_data_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipCollateralDataResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCollateralAssetDataUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanVipCollateralDataResponse](binance/models/sapi_v1_loan_vip_collateral_data_response.py)</code> -- Collateral Asset Data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetCollateralAssetDataUserDataErrorBody](binance/errors/get_collateral_asset_data_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_loanable_assets_data(timestamp: int, signature: str, *, loan_coin: str | None = None, vip_level: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanVipLoanableDataResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get interest rate and borrow limit of loanable assets. The borrow limit is shown in USD value.

Weight(IP): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vip_loans.get_loanable_assets_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipLoanableDataResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLoanableAssetsDataErrorBody
```

**Async**

```python
try:
    response = await async_client.vip_loans.get_loanable_assets_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipLoanableDataResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLoanableAssetsDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>vip_level</code> | <code>int \| None</code> | Defaults to user's vip level<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanVipLoanableDataResponse](binance/models/sapi_v1_loan_vip_loanable_data_response.py)</code> -- Loanable Assets Data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetLoanableAssetsDataErrorBody](binance/errors/get_loanable_assets_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_vip_loan_ongoing_orders_user_data(timestamp: int, signature: str, *, order_id: int | None = None, collateral_account_id: int | None = None, loan_coin: str | None = None, collateral_coin: str | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanVipOngoingOrdersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

VIP loan is available for VIP users only.

Weight(IP): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vip_loans.get_vip_loan_ongoing_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipOngoingOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVipLoanOngoingOrdersUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.vip_loans.get_vip_loan_ongoing_orders_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipOngoingOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVipLoanOngoingOrdersUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>int \| None</code> | Order id<br>**Default**: <code>None</code> |
| <code>collateral_account_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>collateral_coin</code> | <code>str \| None</code> | Coin used as collateral<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 10; max 100.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanVipOngoingOrdersResponse](binance/models/sapi_v1_loan_vip_ongoing_orders_response.py)</code> -- Ongoing VIP Loan Orders

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetVipLoanOngoingOrdersUserDataErrorBody](binance/errors/get_vip_loan_ongoing_orders_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_vip_loan_repayment_history_user_data(timestamp: int, signature: str, *, order_id: int | None = None, loan_coin: str | None = None, start_time: int | None = None, end_time: int | None = None, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanVipRepayHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

VIP loan is available for VIP users only.

Weight(IP): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vip_loans.get_vip_loan_repayment_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipRepayHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVipLoanRepaymentHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.vip_loans.get_vip_loan_repayment_history_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipRepayHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetVipLoanRepaymentHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>int \| None</code> | Order id<br>**Default**: <code>None</code> |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 10; max 100.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanVipRepayHistoryResponse](binance/models/sapi_v1_loan_vip_repay_history_response.py)</code> -- VIP Loan Repayment History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetVipLoanRepaymentHistoryUserDataErrorBody](binance/errors/get_vip_loan_repayment_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_application_status_user_data(timestamp: int, signature: str, *, current: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanVipRequestDataResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Application Status

Weight(UID): 400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vip_loans.query_application_status_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipRequestDataResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryApplicationStatusUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.vip_loans.query_application_status_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipRequestDataResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryApplicationStatusUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanVipRequestDataResponse](binance/models/sapi_v1_loan_vip_request_data_response.py)</code> -- Application Status

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryApplicationStatusUserDataErrorBody](binance/errors/query_application_status_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def vip_loan_borrow(loan_account_id: int, loan_amount: float, collateral_account_id: str, collateral_coin: str, is_flexible_rate: IsFlexibleRateOrStr, timestamp: int, signature: str, *, loan_coin: str | None = None, loan_term: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanVipBorrowResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

VIP loan is available for VIP users only.

Weight(UID): 6000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vip_loans.vip_loan_borrow(
        loan_account_id, loan_amount, collateral_account_id, collateral_coin, is_flexible_rate, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LoanVipBorrowResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VipLoanBorrowErrorBody
```

**Async**

```python
try:
    response = await async_client.vip_loans.vip_loan_borrow(
        loan_account_id, loan_amount, collateral_account_id, collateral_coin, is_flexible_rate, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1LoanVipBorrowResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VipLoanBorrowErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>loan_account_id</code> | <code>int</code> | Value sent with the request. |
| <code>loan_amount</code> | <code>float</code> | Value sent with the request. |
| <code>collateral_account_id</code> | <code>str</code> | Value sent with the request. |
| <code>collateral_coin</code> | <code>str</code> | Value sent with the request. |
| <code>is_flexible_rate</code> | <code>[IsFlexibleRateOrStr](binance/models/enums/is_flexible_rate.py)</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>loan_coin</code> | <code>str \| None</code> | Coin loaned<br>**Default**: <code>None</code> |
| <code>loan_term</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanVipBorrowResponse](binance/models/sapi_v1_loan_vip_borrow_response.py)</code> -- Collateral Assets Data

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[VipLoanBorrowErrorBody](binance/errors/vip_loan_borrow_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def vip_loan_renew(timestamp: int, signature: str, *, order_id: int | None = None, loan_term: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanVipRenewResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

VIP loan is available for VIP users only.

Weight(UID): 6000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vip_loans.vip_loan_renew(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipRenewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VipLoanRenewErrorBody
```

**Async**

```python
try:
    response = await async_client.vip_loans.vip_loan_renew(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipRenewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VipLoanRenewErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>int \| None</code> | Order id<br>**Default**: <code>None</code> |
| <code>loan_term</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanVipRenewResponse](binance/models/sapi_v1_loan_vip_renew_response.py)</code> -- Loan renew result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[VipLoanRenewErrorBody](binance/errors/vip_loan_renew_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def vip_loan_repay_trade(amount: float, timestamp: int, signature: str, *, order_id: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1LoanVipRepayResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

VIP loan is available for VIP users only.

Weight(UID): 6000

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vip_loans.vip_loan_repay_trade(amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipRepayResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VipLoanRepayTradeErrorBody
```

**Async**

```python
try:
    response = await async_client.vip_loans.vip_loan_repay_trade(amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1LoanVipRepayResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VipLoanRepayTradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>order_id</code> | <code>int \| None</code> | Order id<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1LoanVipRepayResponse](binance/models/sapi_v1_loan_vip_repay_response.py)</code> -- VIP Loan Repayment

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[VipLoanRepayTradeErrorBody](binance/errors/vip_loan_repay_trade_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Wallet

> Source: [Wallet](binance/apis/wallet.py)

<details>
<summary><code>def account_api_trading_status_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AccountApiTradingStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch account API trading status with details.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.account_api_trading_status_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AccountApiTradingStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AccountApiTradingStatusUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.account_api_trading_status_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AccountApiTradingStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AccountApiTradingStatusUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AccountApiTradingStatusResponse](binance/models/sapi_v1_account_api_trading_status_response.py)</code> -- Account API trading status

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AccountApiTradingStatusUserDataErrorBody](binance/errors/account_api_trading_status_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def account_status_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AccountStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch account status detail.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.account_status_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AccountStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AccountStatusUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.account_status_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AccountStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AccountStatusUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AccountStatusResponse](binance/models/sapi_v1_account_status_response.py)</code> -- OK

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AccountStatusUserDataErrorBody](binance/errors/account_status_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def account_info_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AccountInfoResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch account info detail.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.account_info_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AccountInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AccountInfoUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.account_info_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AccountInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AccountInfoUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AccountInfoResponse](binance/models/sapi_v1_account_info_response.py)</code> -- Account info detail

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AccountInfoUserDataErrorBody](binance/errors/account_info_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def all_coins_information_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1CapitalConfigGetallResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get information of coins (available for deposit and withdraw) for user.

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.all_coins_information_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1CapitalConfigGetallResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AllCoinsInformationUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.all_coins_information_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1CapitalConfigGetallResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AllCoinsInformationUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1CapitalConfigGetallResponse](binance/models/sapi_v1_capital_config_getall_response.py)&#93;</code> -- All coins details information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AllCoinsInformationUserDataErrorBody](binance/errors/all_coins_information_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_detail_user_data(timestamp: int, signature: str, *, asset: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AssetAssetDetailResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch details of assets supported on Binance.

- Please get network and other deposit or withdraw details from `GET /sapi/v1/capital/config/getall`.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.asset_detail_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetAssetDetailResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AssetDetailUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.asset_detail_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetAssetDetailResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AssetDetailUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AssetAssetDetailResponse](binance/models/sapi_v1_asset_asset_detail_response.py)</code> -- Asset detail

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AssetDetailUserDataErrorBody](binance/errors/asset_detail_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_dividend_record_user_data(timestamp: int, signature: str, *, asset: str | None = None, start_time: int | None = None, end_time: int | None = None, limit: int | None = 20, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AssetAssetDividendResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query asset Dividend Record

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.asset_dividend_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetAssetDividendResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AssetDividendRecordUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.asset_dividend_record_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetAssetDividendResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AssetDividendRecordUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>20</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AssetAssetDividendResponse](binance/models/sapi_v1_asset_asset_dividend_response.py)</code> -- Records of asset devidend

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[AssetDividendRecordUserDataErrorBody](binance/errors/asset_dividend_record_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def convert_transfer_user_data(client_tran_id: str, asset: str, amount: float, target_asset: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AssetConvertTransferResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Convert transfer, convert between BUSD and stablecoins.
If the clientId has been used before, will not do the convert transfer, the original transfer will be returned.

Weight(UID): 5

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.convert_transfer_user_data(
        client_tran_id, asset, amount, target_asset, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1AssetConvertTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConvertTransferUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.convert_transfer_user_data(
        client_tran_id, asset, amount, target_asset, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1AssetConvertTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConvertTransferUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>client_tran_id</code> | <code>str</code> | The unique flag, the min length is 20 |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>target_asset</code> | <code>str</code> | Target asset you want to convert |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AssetConvertTransferResponse](binance/models/sapi_v1_asset_convert_transfer_response.py)</code> -- Conversion Information

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[ConvertTransferUserDataErrorBody](binance/errors/convert_transfer_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def daily_account_snapshot_user_data(type_: Type6OrStr, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, limit: int | None = 7, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AccountSnapshotResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- The query time period must be less than 30 days
- Support query within the last one month only
- If startTimeand endTime not sent, return records of the last 7 days by default

Weight(IP): 2400

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.daily_account_snapshot_user_data(type_, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AccountSnapshotResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DailyAccountSnapshotUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.daily_account_snapshot_user_data(type_, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AccountSnapshotResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DailyAccountSnapshotUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[Type6OrStr](binance/models/enums/type6.py)</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>7</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AccountSnapshotResponse](binance/models/unions/sapi_v1_account_snapshot_response.py)</code> -- Account Snapshot

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[DailyAccountSnapshotUserDataErrorBody](binance/errors/daily_account_snapshot_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deposit_address_supporting_network_user_data(coin: str, timestamp: int, signature: str, *, network: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1CapitalDepositAddressResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch deposit address with network.

- If network is not send, return with default network of the coin.
- You can get network and isDefault in networkList in the response of Get /sapi/v1/capital/config/getall (HMAC SHA256).

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.deposit_address_supporting_network_user_data(coin, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1CapitalDepositAddressResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DepositAddressSupportingNetworkUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.deposit_address_supporting_network_user_data(coin, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1CapitalDepositAddressResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DepositAddressSupportingNetworkUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>coin</code> | <code>str</code> | Coin name |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>network</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1CapitalDepositAddressResponse](binance/models/sapi_v1_capital_deposit_address_response.py)</code> -- Deposit address info

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[DepositAddressSupportingNetworkUserDataErrorBody](binance/errors/deposit_address_supporting_network_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deposit_history_supporting_network_user_data(timestamp: int, signature: str, *, coin: str | None = None, status: int | None = None, start_time: int | None = None, end_time: int | None = None, offset: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1CapitalDepositHisrecResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch deposit history.

- Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days.
- If both `startTime` and `endTime` are sent, time between `startTime` and `endTime` must be less than 90 days.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.deposit_history_supporting_network_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1CapitalDepositHisrecResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DepositHistorySupportingNetworkUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.deposit_history_supporting_network_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1CapitalDepositHisrecResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DepositHistorySupportingNetworkUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>coin</code> | <code>str \| None</code> | Coin name<br>**Default**: <code>None</code> |
| <code>status</code> | <code>int \| None</code> | * `0` - pending<br>* `6` - credited but cannot withdraw<br>* `1` - success<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1CapitalDepositHisrecResponse](binance/models/sapi_v1_capital_deposit_hisrec_response.py)&#93;</code> -- List of deposits

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[DepositHistorySupportingNetworkUserDataErrorBody](binance/errors/deposit_history_supporting_network_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def disable_fast_withdraw_switch_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- This request will disable fastwithdraw switch under your account.
- You need to enable "trade" option for the api key which requests this endpoint.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.disable_fast_withdraw_switch_user_data(timestamp, signature)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DisableFastWithdrawSwitchUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.disable_fast_withdraw_switch_user_data(timestamp, signature)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DisableFastWithdrawSwitchUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[DisableFastWithdrawSwitchUserDataErrorBody](binance/errors/disable_fast_withdraw_switch_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def dust_transfer_user_data(asset: list[str], timestamp: int, signature: str, *, account_type: AccountTypeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AssetDustResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Convert dust assets to BNB.

Weight(UID): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.dust_transfer_user_data(asset, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetDustResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DustTransferUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.dust_transfer_user_data(asset, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetDustResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DustTransferUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset</code> | <code>list&#91;str&#93;</code> | The asset being converted. For example, asset=BTC&asset=USDT |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>account_type</code> | <code>[AccountTypeOrStr](binance/models/enums/account_type.py) \| None</code> | SPOT or MARGIN, default SPOT<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AssetDustResponse](binance/models/sapi_v1_asset_dust_response.py)</code> -- Dust log records

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[DustTransferUserDataErrorBody](binance/errors/dust_transfer_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def dust_log_user_data(timestamp: int, signature: str, *, account_type: AccountTypeOrStr | None = None, start_time: int | None = None, end_time: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AssetDribbletResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.dust_log_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetDribbletResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DustLogUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.dust_log_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetDribbletResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DustLogUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>account_type</code> | <code>[AccountTypeOrStr](binance/models/enums/account_type.py) \| None</code> | SPOT or MARGIN, default SPOT<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AssetDribbletResponse](binance/models/sapi_v1_asset_dribblet_response.py)</code> -- Dust log records

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[DustLogUserDataErrorBody](binance/errors/dust_log_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_fast_withdraw_switch_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- This request will enable fastwithdraw switch under your account. You need to enable "trade" option for the api key which requests this endpoint.
- When Fast Withdraw Switch is on, transferring funds to a Binance account will be done instantly. There is no on-chain transaction, no transaction ID and no withdrawal fee.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.enable_fast_withdraw_switch_user_data(timestamp, signature)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableFastWithdrawSwitchUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.enable_fast_withdraw_switch_user_data(timestamp, signature)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableFastWithdrawSwitchUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[EnableFastWithdrawSwitchUserDataErrorBody](binance/errors/enable_fast_withdraw_switch_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fetch_deposit_address_list_with_network_user_data(coin: str, timestamp: int, signature: str, *, network: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1CapitalDepositAddressListResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch deposit address list with network.

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.fetch_deposit_address_list_with_network_user_data(coin, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1CapitalDepositAddressListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FetchDepositAddressListWithNetworkUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.fetch_deposit_address_list_with_network_user_data(coin, timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1CapitalDepositAddressListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FetchDepositAddressListWithNetworkUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>coin</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>network</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1CapitalDepositAddressListResponse](binance/models/sapi_v1_capital_deposit_address_list_response.py)&#93;</code> -- Coin address

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[FetchDepositAddressListWithNetworkUserDataErrorBody](binance/errors/fetch_deposit_address_list_with_network_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fetch_withdraw_address_list_user_data(*, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1CapitalWithdrawAddressListResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch withdraw address list

Weight(IP): 10

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.fetch_withdraw_address_list_user_data()
    # TODO: Handle 'response' of type list[SapiV1CapitalWithdrawAddressListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FetchWithdrawAddressListUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.fetch_withdraw_address_list_user_data()
    # TODO: Handle 'response' of type list[SapiV1CapitalWithdrawAddressListResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FetchWithdrawAddressListUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1CapitalWithdrawAddressListResponse](binance/models/sapi_v1_capital_withdraw_address_list_response.py)&#93;</code> -- Withdraw address list

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[FetchWithdrawAddressListUserDataErrorBody](binance/errors/fetch_withdraw_address_list_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def funding_wallet_user_data(timestamp: int, signature: str, *, asset: str | None = None, need_btc_valuation: NeedBtcValuationOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1AssetGetFundingAssetResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- Currently supports querying the following business assets：Binance Pay, Binance Card, Binance Gift Card, Stock Token

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.funding_wallet_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1AssetGetFundingAssetResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FundingWalletUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.funding_wallet_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1AssetGetFundingAssetResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FundingWalletUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>need_btc_valuation</code> | <code>[NeedBtcValuationOrStr](binance/models/enums/need_btc_valuation.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1AssetGetFundingAssetResponse](binance/models/sapi_v1_asset_get_funding_asset_response.py)&#93;</code> -- Funding asset detail

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[FundingWalletUserDataErrorBody](binance/errors/funding_wallet_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_api_key_permission_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AccountApiRestrictionsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.get_api_key_permission_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AccountApiRestrictionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetApiKeyPermissionUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.get_api_key_permission_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AccountApiRestrictionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetApiKeyPermissionUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AccountApiRestrictionsResponse](binance/models/sapi_v1_account_api_restrictions_response.py)</code> -- API Key permissions

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetApiKeyPermissionUserDataErrorBody](binance/errors/get_api_key_permission_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_assets_that_can_be_converted_into_bnb_user_data(timestamp: int, signature: str, *, account_type: AccountTypeOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AssetDustBtcResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.get_assets_that_can_be_converted_into_bnb_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetDustBtcResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAssetsThatCanBeConvertedIntoBnbUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.get_assets_that_can_be_converted_into_bnb_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetDustBtcResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAssetsThatCanBeConvertedIntoBnbUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>account_type</code> | <code>[AccountTypeOrStr](binance/models/enums/account_type.py) \| None</code> | SPOT or MARGIN, default SPOT<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AssetDustBtcResponse](binance/models/sapi_v1_asset_dust_btc_response.py)</code> -- Account assets available to be converted to BNB

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetAssetsThatCanBeConvertedIntoBnbUserDataErrorBody](binance/errors/get_assets_that_can_be_converted_into_bnb_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_cloud_mining_payment_and_refund_history_user_data(start_time: int, end_time: int, timestamp: int, signature: str, *, tran_id: int | None = None, client_tran_id: str | None = None, asset: str | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The query of Cloud-Mining payment and refund history

Weight(UID): 600

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.get_cloud_mining_payment_and_refund_history_user_data(
        start_time, end_time, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCloudMiningPaymentAndRefundHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.get_cloud_mining_payment_and_refund_history_user_data(
        start_time, end_time, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCloudMiningPaymentAndRefundHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>start_time</code> | <code>int</code> | UTC timestamp in ms |
| <code>end_time</code> | <code>int</code> | UTC timestamp in ms |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>tran_id</code> | <code>int \| None</code> | The transaction id<br>**Default**: <code>None</code> |
| <code>client_tran_id</code> | <code>str \| None</code> | The unique flag<br>**Default**: <code>None</code> |
| <code>asset</code> | <code>str \| None</code> | If it is blank, we will query all assets<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AssetLedgerTransferCloudMiningQueryByPageResponse](binance/models/sapi_v1_asset_ledger_transfer_cloud_mining_query_by_page_response.py)</code> -- Cloud Mining Payment and Refund History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetCloudMiningPaymentAndRefundHistoryUserDataErrorBody](binance/errors/get_cloud_mining_payment_and_refund_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_symbols_delist_schedule_for_spot_market_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1SpotDelistScheduleResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get symbols delist schedule for spot

Weight(IP): 100

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.get_symbols_delist_schedule_for_spot_market_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1SpotDelistScheduleResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSymbolsDelistScheduleForSpotMarketDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.get_symbols_delist_schedule_for_spot_market_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1SpotDelistScheduleResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSymbolsDelistScheduleForSpotMarketDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1SpotDelistScheduleResponse](binance/models/sapi_v1_spot_delist_schedule_response.py)&#93;</code> -- Symbols delist schedule

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[GetSymbolsDelistScheduleForSpotMarketDataErrorBody](binance/errors/get_symbols_delist_schedule_for_spot_market_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def one_click_arrival_deposit_apply_user_data(timestamp: int, signature: str, *, deposit_id: int | None = None, tx_id: str | None = None, sub_account_id: int | None = None, sub_user_id: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1CapitalDepositCreditApplyResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Apply deposit credit for expired address (One click arrival)

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.one_click_arrival_deposit_apply_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1CapitalDepositCreditApplyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OneClickArrivalDepositApplyUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.one_click_arrival_deposit_apply_user_data(timestamp, signature)
    # TODO: Handle 'response' of type SapiV1CapitalDepositCreditApplyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OneClickArrivalDepositApplyUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>deposit_id</code> | <code>int \| None</code> | Deposit record Id, priority use<br>**Default**: <code>None</code> |
| <code>tx_id</code> | <code>str \| None</code> | Deposit txId, used when depositId is not specified<br>**Default**: <code>None</code> |
| <code>sub_account_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>sub_user_id</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1CapitalDepositCreditApplyResponse](binance/models/sapi_v1_capital_deposit_credit_apply_response.py)</code> -- deposit result

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[OneClickArrivalDepositApplyUserDataErrorBody](binance/errors/one_click_arrival_deposit_apply_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_convert_transfer_user_data(start_time: int, end_time: int, timestamp: int, signature: str, *, tran_id: int | None = None, asset: str | None = None, account_type: AccountType3OrStr | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AssetConvertTransferQueryByPageResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Weight(UID): 5

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.query_convert_transfer_user_data(start_time, end_time, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetConvertTransferQueryByPageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryConvertTransferUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.query_convert_transfer_user_data(start_time, end_time, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetConvertTransferQueryByPageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryConvertTransferUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>start_time</code> | <code>int</code> | UTC timestamp in ms |
| <code>end_time</code> | <code>int</code> | UTC timestamp in ms |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>tran_id</code> | <code>int \| None</code> | The transaction id<br>**Default**: <code>None</code> |
| <code>asset</code> | <code>str \| None</code> | If it is blank, we will match deducted asset and target asset.<br>**Default**: <code>None</code> |
| <code>account_type</code> | <code>[AccountType3OrStr](binance/models/enums/account_type3.py) \| None</code> | MAIN: main account. CARD: funding account. If it is blank, we will query spot and card wallet, otherwise, we just query the corresponding wallet<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AssetConvertTransferQueryByPageResponse](binance/models/sapi_v1_asset_convert_transfer_query_by_page_response.py)</code> -- Query Convert Transfer

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryConvertTransferUserDataErrorBody](binance/errors/query_convert_transfer_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_user_delegation_history_for_master_account_user_data(email: str, start_time: int, end_time: int, asset: str, timestamp: int, signature: str, *, type_: str | None = None, current: int | None = None, size: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AssetCustodyTransferHistoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query User Delegation History

Weight(IP): 60

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.query_user_delegation_history_for_master_account_user_data(
        email, start_time, end_time, asset, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1AssetCustodyTransferHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryUserDelegationHistoryForMasterAccountUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.query_user_delegation_history_for_master_account_user_data(
        email, start_time, end_time, asset, timestamp, signature
    )
    # TODO: Handle 'response' of type SapiV1AssetCustodyTransferHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryUserDelegationHistoryForMasterAccountUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>email</code> | <code>str</code> | Value sent with the request. |
| <code>start_time</code> | <code>int</code> | Value sent with the request. |
| <code>end_time</code> | <code>int</code> | Value sent with the request. |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>type_</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AssetCustodyTransferHistoryResponse](binance/models/sapi_v1_asset_custody_transfer_history_response.py)</code> -- Delegation History

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryUserDelegationHistoryForMasterAccountUserDataErrorBody](binance/errors/query_user_delegation_history_for_master_account_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_user_universal_transfer_history_user_data(type_: Type7OrStr, timestamp: int, signature: str, *, start_time: int | None = None, end_time: int | None = None, current: int | None = None, size: int | None = None, from_symbol: str | None = None, to_symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AssetTransferResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

- `fromSymbol` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
- `toSymbol` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
- Support query within the last 6 months only
- If `startTime` and `endTime` not sent, return records of the last 7 days by default

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.query_user_universal_transfer_history_user_data(type_, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryUserUniversalTransferHistoryUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.query_user_universal_transfer_history_user_data(type_, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetTransferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryUserUniversalTransferHistoryUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[Type7OrStr](binance/models/enums/type7.py)</code> | Universal transfer type |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>current</code> | <code>int \| None</code> | Current querying page. Start from 1. Default:1<br>**Default**: <code>None</code> |
| <code>size</code> | <code>int \| None</code> | Default:10 Max:100<br>**Default**: <code>None</code> |
| <code>from_symbol</code> | <code>str \| None</code> | Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN<br>**Default**: <code>None</code> |
| <code>to_symbol</code> | <code>str \| None</code> | Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AssetTransferResponse](binance/models/sapi_v1_asset_transfer_response.py)</code> -- Universal transfer history

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryUserUniversalTransferHistoryUserDataErrorBody](binance/errors/query_user_universal_transfer_history_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_user_wallet_balance_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1AssetWalletBalanceResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query User Wallet Balance

Weight(IP): 60

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.query_user_wallet_balance_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1AssetWalletBalanceResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryUserWalletBalanceUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.query_user_wallet_balance_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1AssetWalletBalanceResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryUserWalletBalanceUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1AssetWalletBalanceResponse](binance/models/sapi_v1_asset_wallet_balance_response.py)&#93;</code> -- wallet balance

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryUserWalletBalanceUserDataErrorBody](binance/errors/query_user_wallet_balance_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_auto_converting_stable_coins_user_data(*, request_options: RequestOptionsOrDict | None = None) -> SapiV1CapitalContractConvertibleCoinsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a user's auto-conversion settings in deposit/withdrawal

Weight(UID): 600'

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.query_auto_converting_stable_coins_user_data()
    # TODO: Handle 'response' of type SapiV1CapitalContractConvertibleCoinsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryAutoConvertingStableCoinsUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.query_auto_converting_stable_coins_user_data()
    # TODO: Handle 'response' of type SapiV1CapitalContractConvertibleCoinsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryAutoConvertingStableCoinsUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1CapitalContractConvertibleCoinsResponse](binance/models/sapi_v1_capital_contract_convertible_coins_response.py)</code> -- User's auto-conversion settings i

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[QueryAutoConvertingStableCoinsUserDataErrorBody](binance/errors/query_auto_converting_stable_coins_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def switch_on_off_busd_and_stable_coins_conversion_user_data_user_data(coin: str, enable: bool, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

User can use it to turn on or turn off the BUSD auto-conversion from/to a specific stable coin.

Weight(UID): 600'

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.switch_on_off_busd_and_stable_coins_conversion_user_data_user_data(coin, enable)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SwitchOnOffBusdAndStableCoinsConversionUserDataUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.switch_on_off_busd_and_stable_coins_conversion_user_data_user_data(
        coin, enable
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SwitchOnOffBusdAndStableCoinsConversionUserDataUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>coin</code> | <code>str</code> | Must be USDC, USDP or TUSD |
| <code>enable</code> | <code>bool</code> | true: turn on the auto-conversion. false: turn off the auto-conversion |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[SwitchOnOffBusdAndStableCoinsConversionUserDataUserDataErrorBody](binance/errors/switch_on_off_busd_and_stable_coins_conversion_user_data_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def system_status_system(*, request_options: RequestOptionsOrDict | None = None) -> SapiV1SystemStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch system status.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.system_status_system()
    # TODO: Handle 'response' of type SapiV1SystemStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.wallet.system_status_system()
    # TODO: Handle 'response' of type SapiV1SystemStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1SystemStatusResponse](binance/models/sapi_v1_system_status_response.py)</code> -- OK

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[RawError](binance/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def trade_fee_user_data(timestamp: int, signature: str, *, symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1AssetTradeFeeResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch trade fee

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.trade_fee_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1AssetTradeFeeResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TradeFeeUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.trade_fee_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1AssetTradeFeeResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type TradeFeeUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>symbol</code> | <code>str \| None</code> | Trading symbol, e.g. BNBUSDT<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1AssetTradeFeeResponse](binance/models/sapi_v1_asset_trade_fee_response.py)&#93;</code> -- Trade fee info per symbol

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[TradeFeeUserDataErrorBody](binance/errors/trade_fee_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_asset_user_data(timestamp: int, signature: str, *, asset: str | None = None, need_btc_valuation: NeedBtcValuationOrStr | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV3AssetGetUserAssetResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get user assets, just for positive data.

Weight(IP): 5

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.user_asset_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV3AssetGetUserAssetResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UserAssetUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.user_asset_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV3AssetGetUserAssetResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UserAssetUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>asset</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>need_btc_valuation</code> | <code>[NeedBtcValuationOrStr](binance/models/enums/need_btc_valuation.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV3AssetGetUserAssetResponse](binance/models/sapi_v3_asset_get_user_asset_response.py)&#93;</code> -- User assets

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[UserAssetUserDataErrorBody](binance/errors/user_asset_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def user_universal_transfer_user_data(type_: Type7OrStr, asset: str, amount: float, timestamp: int, signature: str, *, from_symbol: str | None = None, to_symbol: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1AssetTransferResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

You need to enable `Permits Universal Transfer` option for the api key which requests this endpoint.

- `fromSymbol` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
- `toSymbol` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN

ENUM of transfer types:
  - MAIN_UMFUTURE Spot account transfer to USDⓈ-M Futures account
  - MAIN_CMFUTURE Spot account transfer to COIN-M Futures account
  - MAIN_MARGIN Spot account transfer to Margin(cross)account
  - UMFUTURE_MAIN USDⓈ-M Futures account transfer to Spot account
  - UMFUTURE_MARGIN USDⓈ-M Futures account transfer to Margin(cross)account
  - CMFUTURE_MAIN COIN-M Futures account transfer to Spot account
  - CMFUTURE_MARGIN COIN-M Futures account transfer to Margin(cross) account
  - MARGIN_MAIN Margin(cross)account transfer to Spot account
  - MARGIN_UMFUTURE Margin(cross)account transfer to USDⓈ-M Futures
  - MARGIN_CMFUTURE Margin(cross)account transfer to COIN-M Futures
  - ISOLATEDMARGIN_MARGIN Isolated margin account transfer to Margin(cross) account
  - MARGIN_ISOLATEDMARGIN Margin(cross) account transfer to Isolated margin account
  - ISOLATEDMARGIN_ISOLATEDMARGIN Isolated margin account transfer to Isolated margin account
  - MAIN_FUNDING Spot account transfer to Funding account
  - FUNDING_MAIN Funding account transfer to Spot account
  - FUNDING_UMFUTURE Funding account transfer to UMFUTURE account
  - UMFUTURE_FUNDING UMFUTURE account transfer to Funding account
  - MARGIN_FUNDING MARGIN account transfer to Funding account
  - FUNDING_MARGIN Funding account transfer to Margin account
  - FUNDING_CMFUTURE Funding account transfer to CMFUTURE account
  - CMFUTURE_FUNDING CMFUTURE account transfer to Funding account
  - MAIN_OPTION Spot account transfer to Options account
  - OPTION_MAIN Options account transfer to Spot account
  - UMFUTURE_OPTION USDⓈ-M Futures account transfer to Options account
  - OPTION_UMFUTURE Options account transfer to USDⓈ-M Futures account
  - MARGIN_OPTION Margin(cross)account transfer to Options account
  - OPTION_MARGIN Options account transfer to Margin(cross)account
  - FUNDING_OPTION Funding account transfer to Options account
  - OPTION_FUNDING Options account transfer to Funding account
  - MAIN_PORTFOLIO_MARGIN Spot account transfer to Portfolio Margin account
  - PORTFOLIO_MARGIN_MAIN Portfolio Margin account transfer to Spot account
  - MAIN_ISOLATED_MARGIN Spot account transfer to Isolated margin account
  - ISOLATED_MARGIN_MAIN Isolated margin account transfer to Spot account

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.user_universal_transfer_user_data(type_, asset, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetTransferResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UserUniversalTransferUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.user_universal_transfer_user_data(type_, asset, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1AssetTransferResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UserUniversalTransferUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>[Type7OrStr](binance/models/enums/type7.py)</code> | Universal transfer type |
| <code>asset</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>from_symbol</code> | <code>str \| None</code> | Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN<br>**Default**: <code>None</code> |
| <code>to_symbol</code> | <code>str \| None</code> | Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1AssetTransferResponse1](binance/models/sapi_v1_asset_transfer_response1.py)</code> -- Transfer id

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[UserUniversalTransferUserDataErrorBody](binance/errors/user_universal_transfer_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def withdraw_user_data(coin: str, address: str, amount: float, timestamp: int, signature: str, *, withdraw_order_id: str | None = None, network: str | None = None, address_tag: str | None = None, transaction_fee_flag: bool | None = False, name: str | None = None, wallet_type: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SapiV1CapitalWithdrawApplyResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Submit a withdraw request.

- If `network` not send, return with default network of the coin.
- You can get `network` and `isDefault` in `networkList` of a coin in the response of `Get /sapi/v1/capital/config/getall (HMAC SHA256)`.

Weight(IP): 1

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.withdraw_user_data(coin, address, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1CapitalWithdrawApplyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type WithdrawUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.withdraw_user_data(coin, address, amount, timestamp, signature)
    # TODO: Handle 'response' of type SapiV1CapitalWithdrawApplyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type WithdrawUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>coin</code> | <code>str</code> | Coin name |
| <code>address</code> | <code>str</code> | Value sent with the request. |
| <code>amount</code> | <code>float</code> | Value sent with the request. |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>withdraw_order_id</code> | <code>str \| None</code> | Client id for withdraw<br>**Default**: <code>None</code> |
| <code>network</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>address_tag</code> | <code>str \| None</code> | Secondary address identifier for coins like XRP,XMR etc.<br>**Default**: <code>None</code> |
| <code>transaction_fee_flag</code> | <code>bool \| None</code> | When making internal transfer<br>- `true` ->  returning the fee to the destination account;<br>- `false` -> returning the fee back to the departure account.<br>**Default**: <code>False</code> |
| <code>name</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>wallet_type</code> | <code>int \| None</code> | The wallet type for withdraw，0-Spot wallet, 1- Funding wallet. Default is Spot wallet<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SapiV1CapitalWithdrawApplyResponse](binance/models/sapi_v1_capital_withdraw_apply_response.py)</code> -- Transafer Id

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[WithdrawUserDataErrorBody](binance/errors/withdraw_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def withdraw_history_supporting_network_user_data(timestamp: int, signature: str, *, coin: str | None = None, withdraw_order_id: str | None = None, status: int | None = None, start_time: int | None = None, end_time: int | None = None, offset: int | None = None, limit: int | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SapiV1CapitalWithdrawHistoryResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch withdraw history.

This endpoint specifically uses per second UID rate limit, user's total second level IP rate limit is 180000/second. Response from the endpoint contains header key X-SAPI-USED-UID-WEIGHT-1S, which defines weight used by the current IP.

- `network` may not be in the response for old withdraw.
- Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days.
- If both `startTime` and `endTime` are sent, time between `startTime` and `endTime` must be less than 90 days
- If withdrawOrderId is sent, time between startTime and endTime must be less than 7 days.
- If withdrawOrderId is sent, startTime and endTime are not sent, will return last 7 days records by default.

Weight(UID): 18000
Request Limit: 10 requests per second

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet.withdraw_history_supporting_network_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1CapitalWithdrawHistoryResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type WithdrawHistorySupportingNetworkUserDataErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet.withdraw_history_supporting_network_user_data(timestamp, signature)
    # TODO: Handle 'response' of type list[SapiV1CapitalWithdrawHistoryResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type WithdrawHistorySupportingNetworkUserDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timestamp</code> | <code>int</code> | UTC timestamp in ms |
| <code>signature</code> | <code>str</code> | Signature |
| <code>coin</code> | <code>str \| None</code> | Coin name<br>**Default**: <code>None</code> |
| <code>withdraw_order_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>int \| None</code> | * `0` - Email Sent<br>* `1` - Cancelled<br>* `2` - Awaiting Approval<br>* `3` - Rejected<br>* `4` - Processing<br>* `5` - Failure<br>* `6` - Completed<br>**Default**: <code>None</code> |
| <code>start_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>int \| None</code> | UTC timestamp in ms<br>**Default**: <code>None</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Default 500; max 1000.<br>**Default**: <code>None</code> |
| <code>recv_window</code> | <code>int \| None</code> | The value cannot be greater than 60000<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](binance/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SapiV1CapitalWithdrawHistoryResponse](binance/models/sapi_v1_capital_withdraw_history_response.py)&#93;</code> -- List of withdraw history

**OnError**: <code>[ApiError](binance/core/exceptions.py)&#91;[WithdrawHistorySupportingNetworkUserDataErrorBody](binance/errors/withdraw_history_supporting_network_user_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[Error](binance/models/error.py)</code> |
| anything unmapped | <code>[RawError](binance/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

