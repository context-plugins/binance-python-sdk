<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — Binance Public Spot API (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | Binance Public Spot API |
| Root package | `binance_public_spot_api` |
| Distribution name | `binance-public-spot-api` |
| Requires | Python 3.10 or later |
| API spec version | `1.0` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from binance_public_spot_api import BinancePublicSpotApiClient

client = BinancePublicSpotApiClient(api_key_auth="YOUR_API_KEY", environment="production")

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with BinancePublicSpotApiClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run

from binance_public_spot_api import AsyncBinancePublicSpotApiClient


async def main() -> None:
    client = AsyncBinancePublicSpotApiClient(api_key_auth="YOUR_API_KEY", environment="production")
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncBinancePublicSpotApiClient(...) as client:` closes the pool on exit.

`AsyncClient` (`binance_public_spot_api/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavor.

`Client` and `AsyncClient` are aliases of `BinancePublicSpotApiClient` and `AsyncBinancePublicSpotApiClient` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.auto_invest`). Every constructor argument is optional and keyword-only. Sources: `binance_public_spot_api/client.py`, `binance_public_spot_api/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `environment` | `Environment` | `Environment` | `"production"` |
| `base_url` | `str \| None` | `str \| None` | `None` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `api_key_auth` | `str \| None` | `str \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `Environment` | `binance_public_spot_api.server` | `Literal` of the Environments table's names |
| `HttpClient` | `binance_public_spot_api.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()` |
| `AsyncHttpClient` | `binance_public_spot_api.core` | protocol — `async send(request: HttpRequest) -> HttpResponse` · `async aclose()` |

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.response`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `binance_public_spot_api/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`binance_public_spot_api/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse`.

Core runtime types (`binance_public_spot_api/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is a Case A alias from `binance_public_spot_api/errors/` or `RawError` | `error: E` · `status_code: int` · `response: HttpResponse` | `binance_public_spot_api/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `response: HttpResponse` (on both) | `binance_public_spot_api/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse` | `binance_public_spot_api/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
from binance_public_spot_api.core import ApiError, RawError
from binance_public_spot_api.models import Error

try:
    response = client.auto_invest.change_plan_status(plan_id, status, timestamp, signature)
except ApiError as e:
    # Case A — typed error: e.error is ChangePlanStatusErrorBody
    if isinstance(e.error, Error):
        # Handle 400, 401
        print(e.error)
    if isinstance(e.error, RawError):
        # Any other error status
        print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **340 operations**, **333 are Case A (typed)** and **7 are Case B (raw)**.

---

## Operations — by controller (29 pages, 340 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every type it names, with the module that declares it.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout or extra headers; every signature ends with it | here (`binance_public_spot_api/core/request_options.py`) |
| **Base URL is the selected environment's** — this SDK's only server, one URL per `environment=`; override it with `base_url="https://…"` | Servers & auth |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Ops | Page |
| --- | --- | --- |
| `client.auto_invest` | 17 | [map/operations/auto_invest.md](map/operations/auto_invest.md) |
| `client.blvt` | 6 | [map/operations/blvt.md](map/operations/blvt.md) |
| `client.c2_c` | 1 | [map/operations/c2_c.md](map/operations/c2_c.md) |
| `client.convert` | 9 | [map/operations/convert.md](map/operations/convert.md) |
| `client.copy_trading` | 2 | [map/operations/copy_trading.md](map/operations/copy_trading.md) |
| `client.crypto_loans` | 21 | [map/operations/crypto_loans.md](map/operations/crypto_loans.md) |
| `client.dual_investment` | 5 | [map/operations/dual_investment.md](map/operations/dual_investment.md) |
| `client.fiat` | 2 | [map/operations/fiat.md](map/operations/fiat.md) |
| `client.futures` | 3 | [map/operations/futures.md](map/operations/futures.md) |
| `client.futures_algo` | 6 | [map/operations/futures_algo.md](map/operations/futures_algo.md) |
| `client.gift_card` | 6 | [map/operations/gift_card.md](map/operations/gift_card.md) |
| `client.isolated_margin_stream` | 3 | [map/operations/isolated_margin_stream.md](map/operations/isolated_margin_stream.md) |
| `client.margin` | 48 | [map/operations/margin.md](map/operations/margin.md) |
| `client.margin_stream` | 3 | [map/operations/margin_stream.md](map/operations/margin_stream.md) |
| `client.market` | 15 | [map/operations/market.md](map/operations/market.md) |
| `client.mining` | 13 | [map/operations/mining.md](map/operations/mining.md) |
| `client.nft` | 4 | [map/operations/nft.md](map/operations/nft.md) |
| `client.pay` | 1 | [map/operations/pay.md](map/operations/pay.md) |
| `client.portfolio_margin` | 14 | [map/operations/portfolio_margin.md](map/operations/portfolio_margin.md) |
| `client.rebate` | 1 | [map/operations/rebate.md](map/operations/rebate.md) |
| `client.savings` | 4 | [map/operations/savings.md](map/operations/savings.md) |
| `client.simple_earn` | 24 | [map/operations/simple_earn.md](map/operations/simple_earn.md) |
| `client.spot_algo` | 5 | [map/operations/spot_algo.md](map/operations/spot_algo.md) |
| `client.staking` | 12 | [map/operations/staking.md](map/operations/staking.md) |
| `client.stream` | 3 | [map/operations/stream.md](map/operations/stream.md) |
| `client.sub_account_api` | 45 | [map/operations/sub_account_api.md](map/operations/sub_account_api.md) |
| `client.trade_api` | 23 | [map/operations/trade_api.md](map/operations/trade_api.md) |
| `client.vip_loans` | 10 | [map/operations/vip_loans.md](map/operations/vip_loans.md) |
| `client.wallet` | 34 | [map/operations/wallet.md](map/operations/wallet.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `binance_public_spot_api/models/` declares one type plus its input companion, and every module under `binance_public_spot_api/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`AccountProfit` ↔ `account_profit.py`; an error alias drops its `Body` suffix: `HrTickerPriceChangeStatistics24ErrorBody` ↔ `hr_ticker_price_change_statistics24_error.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 522 | `binance_public_spot_api/models/` |
| Enums (`Enum` over `str`) — Python member names + wire values | 62 | `binance_public_spot_api/models/enums/` |
| Unions (plain) — `TypeAlias` over the arms | 15 | `binance_public_spot_api/models/unions/` |
| Error aliases (one per Case A operation) | 333 | `binance_public_spot_api/errors/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`type_` ↔ `"type"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model, enum and union also has an **input companion**, exported beside it from the same package (`AccountProfit` ↔ `AccountProfitDict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`AboveTimeInForce` ↔ `AboveTimeInForceOrStr`) and additionally accepts a wire value this SDK version does not know. A union is a `TypeAlias` over its arms.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `binance_public_spot_api` |
| Operation controllers | `binance_public_spot_api.apis` |
| Models | `binance_public_spot_api.models` |
| Enums | `binance_public_spot_api.models.enums` |
| Unions | `binance_public_spot_api.models.unions`, `binance_public_spot_api.models` |
| Error aliases | `binance_public_spot_api.errors` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `binance_public_spot_api.core` |

---

## Servers & auth

**API key (header `X-MBX-APIKEY`).** Pass `api_key_auth="<api_key>"`; sent as the `X-MBX-APIKEY` request header.

Operation blocks name their scheme in an **Auth** bullet; an operation whose spec declares no scheme carries no such bullet.

- `AND` — every scheme listed must be configured for the call to succeed.
- `OR` — any one of the schemes listed can be used; the first one you configured is the one sent, in the order listed.

A scheme you did not configure is skipped silently rather than raising, and the request is sent anyway — so an authentication failure can mean no credential was sent rather than a bad one.

**Environments.** `environment=` selects the target environment (`binance_public_spot_api/server/environment.py`); this SDK's one server (`binance_public_spot_api/server/server_config.py`) has a base URL per environment:

| Environment | Base URL | Hosting | Override point |
| --- | --- | --- | --- |
| `"production"` *(default)* | `https://api.binance.com` | — | `base_url="https://…"` |
| `"environment2"` | `https://testnet.binance.vision` | — | `base_url="https://…"` |

Pick a row with `environment=`.

