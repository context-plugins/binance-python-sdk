from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.get_futures_lead_trader_status_trade_error import (
    GetFuturesLeadTraderStatusTradeErrorBody,
    get_futures_lead_trader_status_trade_error_mapper,
)
from ..errors.get_futures_lead_trading_symbol_whitelist_user_data_error import (
    GetFuturesLeadTradingSymbolWhitelistUserDataErrorBody,
    get_futures_lead_trading_symbol_whitelist_user_data_error_mapper,
)
from ..models.sapi_v1_copy_trading_futures_lead_symbol_response import SapiV1CopyTradingFuturesLeadSymbolResponse
from ..models.sapi_v1_copy_trading_futures_user_status_response import SapiV1CopyTradingFuturesUserStatusResponse
from ..server.server import Server


class CopyTrading:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CopyTradingWithRawResponse(client, server, auth)

    def get_futures_lead_trader_status_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1CopyTradingFuturesUserStatusResponse:
        """Get Futures Lead Trader Status

        Weight(UID): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures Lead Trader Status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_futures_lead_trader_status_trade(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def get_futures_lead_trading_symbol_whitelist_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1CopyTradingFuturesLeadSymbolResponse:
        """Get Futures Lead Trading Symbol Whitelist

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures Lead Trading Symbol Whitelist

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_futures_lead_trading_symbol_whitelist_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> CopyTradingWithRawResponse:
        return self._with_raw_response


class AsyncCopyTrading:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCopyTradingWithRawResponse(client, server, auth)

    async def get_futures_lead_trader_status_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1CopyTradingFuturesUserStatusResponse:
        """Get Futures Lead Trader Status

        Weight(UID): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures Lead Trader Status

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_futures_lead_trader_status_trade(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def get_futures_lead_trading_symbol_whitelist_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1CopyTradingFuturesLeadSymbolResponse:
        """Get Futures Lead Trading Symbol Whitelist

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Futures Lead Trading Symbol Whitelist

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_futures_lead_trading_symbol_whitelist_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCopyTradingWithRawResponse:
        return self._with_raw_response


class CopyTradingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_futures_lead_trader_status_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1CopyTradingFuturesUserStatusResponse, GetFuturesLeadTraderStatusTradeErrorBody]:
        """Get Futures Lead Trader Status

        Weight(UID): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/copyTrading/futures/userStatus"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1CopyTradingFuturesUserStatusResponse],
            error_mapper=get_futures_lead_trader_status_trade_error_mapper,
            request_options=request_options,
        )

    def get_futures_lead_trading_symbol_whitelist_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1CopyTradingFuturesLeadSymbolResponse, GetFuturesLeadTradingSymbolWhitelistUserDataErrorBody]:
        """Get Futures Lead Trading Symbol Whitelist

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/copyTrading/futures/leadSymbol"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1CopyTradingFuturesLeadSymbolResponse],
            error_mapper=get_futures_lead_trading_symbol_whitelist_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncCopyTradingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_futures_lead_trader_status_trade(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1CopyTradingFuturesUserStatusResponse, GetFuturesLeadTraderStatusTradeErrorBody]:
        """Get Futures Lead Trader Status

        Weight(UID): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/copyTrading/futures/userStatus"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1CopyTradingFuturesUserStatusResponse],
            error_mapper=get_futures_lead_trader_status_trade_error_mapper,
            request_options=request_options,
        )

    async def get_futures_lead_trading_symbol_whitelist_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1CopyTradingFuturesLeadSymbolResponse, GetFuturesLeadTradingSymbolWhitelistUserDataErrorBody]:
        """Get Futures Lead Trading Symbol Whitelist

        Weight(IP): 20

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/copyTrading/futures/leadSymbol"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1CopyTradingFuturesLeadSymbolResponse],
            error_mapper=get_futures_lead_trading_symbol_whitelist_user_data_error_mapper,
            request_options=request_options,
        )
