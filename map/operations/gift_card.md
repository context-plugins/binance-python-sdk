<!-- Generated file — do not edit; regenerated with the SDK. -->

# GiftCard — operations

Accessor: `client.gift_card` · Source: `binance/apis/gift_card.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.gift_card.buy_a_binance_code_trade

- **Route**: `POST /sapi/v1/giftcard/buyCode`
- **Signature**: `def buy_a_binance_code_trade(base_token: str, face_token: str, base_token_amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `base_token`, `face_token`, `base_token_amount`, `timestamp`, `signature`
- **Params**: `base_token` — query `baseToken` · `face_token` — query `faceToken` · `base_token_amount` — query `baseTokenAmount` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1GiftcardBuyCodeResponse`
- **Returns (raw)**: `ApiResult[SapiV1GiftcardBuyCodeResponse, BuyABinanceCodeTradeErrorBody]`
- **Error**: `BuyABinanceCodeTradeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1GiftcardBuyCodeResponse` | `binance/models/sapi_v1_giftcard_buy_code_response.py` |
| `BuyABinanceCodeTradeErrorBody` | `binance/errors/buy_a_binance_code_trade_error.py` |
| `Error` | `binance/models/error.py` |

### client.gift_card.create_a_binance_code_user_data

- **Route**: `POST /sapi/v1/giftcard/createCode`
- **Signature**: `def create_a_binance_code_user_data(token: str, amount: float, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `amount`, `timestamp`, `signature`
- **Params**: `token` — query · `amount` — query · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1GiftcardCreateCodeResponse`
- **Returns (raw)**: `ApiResult[SapiV1GiftcardCreateCodeResponse, CreateABinanceCodeUserDataErrorBody]`
- **Error**: `CreateABinanceCodeUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1GiftcardCreateCodeResponse` | `binance/models/sapi_v1_giftcard_create_code_response.py` |
| `CreateABinanceCodeUserDataErrorBody` | `binance/errors/create_a_binance_code_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.gift_card.fetch_rsa_public_key_user_data

- **Route**: `GET /sapi/v1/giftcard/cryptography/rsa-public-key`
- **Signature**: `def fetch_rsa_public_key_user_data(timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timestamp`, `signature`
- **Params**: `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1GiftcardCryptographyRsaPublicKeyResponse`
- **Returns (raw)**: `ApiResult[SapiV1GiftcardCryptographyRsaPublicKeyResponse, FetchRsaPublicKeyUserDataErrorBody]`
- **Error**: `FetchRsaPublicKeyUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1GiftcardCryptographyRsaPublicKeyResponse` | `binance/models/sapi_v1_giftcard_cryptography_rsa_public_key_response.py` |
| `FetchRsaPublicKeyUserDataErrorBody` | `binance/errors/fetch_rsa_public_key_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.gift_card.fetch_token_limit_user_data

- **Route**: `GET /sapi/v1/giftcard/buyCode/token-limit`
- **Signature**: `def fetch_token_limit_user_data(base_token: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `base_token`, `timestamp`, `signature`
- **Params**: `base_token` — query `baseToken` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1GiftcardBuyCodeTokenLimitResponse`
- **Returns (raw)**: `ApiResult[SapiV1GiftcardBuyCodeTokenLimitResponse, FetchTokenLimitUserDataErrorBody]`
- **Error**: `FetchTokenLimitUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1GiftcardBuyCodeTokenLimitResponse` | `binance/models/sapi_v1_giftcard_buy_code_token_limit_response.py` |
| `FetchTokenLimitUserDataErrorBody` | `binance/errors/fetch_token_limit_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.gift_card.redeem_a_binance_code_user_data

- **Route**: `POST /sapi/v1/giftcard/redeemCode`
- **Signature**: `def redeem_a_binance_code_user_data(code: str, timestamp: int, signature: str, *, external_uid: str | None = None, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `code`, `timestamp`, `signature`
- **Params**: `code` — query · `timestamp` — query · `signature` — query · `external_uid` — query `externalUid` · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1GiftcardRedeemCodeResponse`
- **Returns (raw)**: `ApiResult[SapiV1GiftcardRedeemCodeResponse, RedeemABinanceCodeUserDataErrorBody]`
- **Error**: `RedeemABinanceCodeUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1GiftcardRedeemCodeResponse` | `binance/models/sapi_v1_giftcard_redeem_code_response.py` |
| `RedeemABinanceCodeUserDataErrorBody` | `binance/errors/redeem_a_binance_code_user_data_error.py` |
| `Error` | `binance/models/error.py` |

### client.gift_card.verify_a_binance_code_user_data

- **Route**: `GET /sapi/v1/giftcard/verify`
- **Signature**: `def verify_a_binance_code_user_data(reference_no: str, timestamp: int, signature: str, *, recv_window: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `reference_no`, `timestamp`, `signature`
- **Params**: `reference_no` — query `referenceNo` · `timestamp` — query · `signature` — query · `recv_window` — query `recvWindow`
- **Returns (parsed)**: `SapiV1GiftcardVerifyResponse`
- **Returns (raw)**: `ApiResult[SapiV1GiftcardVerifyResponse, VerifyABinanceCodeUserDataErrorBody]`
- **Error**: `VerifyABinanceCodeUserDataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SapiV1GiftcardVerifyResponse` | `binance/models/sapi_v1_giftcard_verify_response.py` |
| `VerifyABinanceCodeUserDataErrorBody` | `binance/errors/verify_a_binance_code_user_data_error.py` |
| `Error` | `binance/models/error.py` |

