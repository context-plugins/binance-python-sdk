from __future__ import annotations

from typing import Any

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.compressed_aggregate_trades_list_error import (
    CompressedAggregateTradesListErrorBody,
    compressed_aggregate_trades_list_error_mapper,
)
from ..errors.current_average_price_error import CurrentAveragePriceErrorBody, current_average_price_error_mapper
from ..errors.exchange_information_error import ExchangeInformationErrorBody, exchange_information_error_mapper
from ..errors.hr_ticker_price_change_statistics24_error import (
    HrTickerPriceChangeStatistics24ErrorBody,
    hr_ticker_price_change_statistics24_error_mapper,
)
from ..errors.kline_candlestick_data_error import KlineCandlestickDataErrorBody, kline_candlestick_data_error_mapper
from ..errors.order_book_error import OrderBookErrorBody, order_book_error_mapper
from ..errors.recent_trades_list_error import RecentTradesListErrorBody, recent_trades_list_error_mapper
from ..errors.rolling_window_price_change_statistics_error import (
    RollingWindowPriceChangeStatisticsErrorBody,
    rolling_window_price_change_statistics_error_mapper,
)
from ..errors.symbol_order_book_ticker_error import (
    SymbolOrderBookTickerErrorBody,
    symbol_order_book_ticker_error_mapper,
)
from ..errors.symbol_price_ticker_error import SymbolPriceTickerErrorBody, symbol_price_ticker_error_mapper
from ..errors.trading_day_ticker_error import TradingDayTickerErrorBody, trading_day_ticker_error_mapper
from ..errors.uiklines_error import UiklinesErrorBody, uiklines_error_mapper
from ..models.agg_trade import AggTrade
from ..models.api_v3_avg_price_response import ApiV3AvgPriceResponse
from ..models.api_v3_depth_response import ApiV3DepthResponse
from ..models.api_v3_exchange_info_response import ApiV3ExchangeInfoResponse
from ..models.api_v3_ticker_response import ApiV3TickerResponse
from ..models.api_v3_time_response import ApiV3TimeResponse
from ..models.enums.interval import IntervalOrStr
from ..models.enums.type import TypeOrStr
from ..models.trade import Trade
from ..models.unions.api_v3_klines_response import ApiV3KlinesResponse
from ..models.unions.api_v3_ticker24_hr_response import ApiV3Ticker24HrResponse
from ..models.unions.api_v3_ticker_book_ticker_response import ApiV3TickerBookTickerResponse
from ..models.unions.api_v3_ticker_price_response import ApiV3TickerPriceResponse
from ..models.unions.api_v3_ticker_trading_day_response import ApiV3TickerTradingDayResponse
from ..models.unions.api_v3_ui_klines_response import ApiV3UiKlinesResponse
from ..server.server import Server


class Market:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = MarketWithRawResponse(client, server)

    def hr_ticker_price_change_statistics24(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        type_: TypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3Ticker24HrResponse:
        """24 hour rolling window price change statistics. Careful when accessing this with no symbol.

        - If the symbol is not sent, tickers for all symbols will be returned in an array.

        Weight(IP):
        - ``2`` for a single symbol;
        - ``80`` when the symbol parameter is omitted;

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            type_: Supported values: FULL or MINI. If none provided, the default is FULL
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            24hr ticker

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.hr_ticker_price_change_statistics24(
            symbol=symbol, symbols=symbols, type_=type_, request_options=request_options
        ).unwrap()

    def check_server_time(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiV3TimeResponse:
        """Test connectivity to the Rest API and get the current server time.

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Binance server UTC timestamp

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.check_server_time(request_options=request_options).unwrap()

    def compressed_aggregate_trades_list(
        self,
        symbol: str,
        *,
        from_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[AggTrade]:
        """Get compressed, aggregate trades. Trades that fill at the time, from the same order, with the same price will
        have the quantity aggregated.
        - If ``fromId``, ``startTime``, and ``endTime`` are not sent, the most recent aggregate trades will be returned.
        - Note that if a trade has the following values, this was a duplicate aggregate trade and marked as invalid:

        p = '0' // price

          q = '0' // qty

          f = -1 // ﬁrst_trade_id

          l = -1 // last_trade_id

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            from_id: Trade id to fetch from. Default gets most recent trades.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trade list

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.compressed_aggregate_trades_list(
            symbol,
            from_id=from_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            request_options=request_options,
        ).unwrap()

    def current_average_price(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV3AvgPriceResponse:
        """Current average price for a symbol.

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Average price

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.current_average_price(symbol, request_options=request_options).unwrap()

    def exchange_information(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        permissions: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3ExchangeInfoResponse:
        """Current exchange trading rules and symbol information

        - If any symbol provided in either symbol or symbols do not exist, the endpoint will throw an error.
        - All parameters are optional.
        - permissions can support single or multiple values (e.g. SPOT, ["MARGIN","LEVERAGED"])
        - If permissions parameter not provided, the default values will be ["SPOT","MARGIN","LEVERAGED"].
          - To display all permissions you need to specify them explicitly. (e.g. SPOT, MARGIN,...)

        Examples of Symbol Permissions Interpretation from the Response:
        - [["A","B"]] means you may place an order if your account has either permission "A" or permission "B".
        - [["A"],["B"]] means you can place an order if your account has permission "A" and permission "B".
        - [["A"],["B","C"]] means you can place an order if your account has permission "A" and permission "B" or
            permission "C". (Inclusive or is applied here, not exclusive or, so your account may have both permission
            "B" and permission "C".)

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            permissions: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Current exchange trading rules and symbol information

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.exchange_information(
            symbol=symbol, symbols=symbols, permissions=permissions, request_options=request_options
        ).unwrap()

    def kline_candlestick_data(
        self,
        symbol: str,
        interval: IntervalOrStr,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        time_zone: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[list[ApiV3KlinesResponse]]:
        """Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.

        - If ``startTime`` and ``endTime`` are not sent, the most recent klines are returned.

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            interval: kline intervals
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            time_zone: Default: 0 (UTC)
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Kline data

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.kline_candlestick_data(
            symbol,
            interval,
            start_time=start_time,
            end_time=end_time,
            time_zone=time_zone,
            limit=limit,
            request_options=request_options,
        ).unwrap()

    def old_trade_lookup(
        self,
        symbol: str,
        *,
        limit: int | None = None,
        from_id: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Trade]:
        """Get older market trades.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            limit: Default 500; max 1000.
            from_id: Trade id to fetch from. Default gets most recent trades.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trade list

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.old_trade_lookup(
            symbol, limit=limit, from_id=from_id, request_options=request_options
        ).unwrap()

    def order_book(
        self, symbol: str, *, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV3DepthResponse:
        """| Limit | Weight(IP) |
        |---------------------|-------------|
        | 1-100 | 5 |
        | 101-500 | 25 |
        | 501-1000 | 50 |
        | 1001-5000 | 250 |

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            limit: If limit > 5000, then the response will truncate to 5000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Order book

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.order_book(symbol, limit=limit, request_options=request_options).unwrap()

    def recent_trades_list(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[Trade]:
        """Get recent trades.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trade list

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.recent_trades_list(symbol, limit=limit, request_options=request_options).unwrap()

    def rolling_window_price_change_statistics(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        window_size: str | None = None,
        type_: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3TickerResponse:
        """The window used to compute statistics is typically slightly wider than requested windowSize.

        openTime for /api/v3/ticker always starts on a minute, while the closeTime is the current time of the request.
        As such, the effective window might be up to 1 minute wider than requested.

        E.g. If the closeTime is 1641287867099 (January 04, 2022 09:17:47:099 UTC) , and the windowSize is 1d. the
        openTime will be: 1641201420000 (January 3, 2022, 09:17:00 UTC)

        Weight(IP): 4 for each requested symbol regardless of windowSize.

        The weight for this request will cap at 200 once the number of symbols in the request is more than 50.

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            window_size: Defaults to 1d if no parameter provided. Supported windowSize values: 1m,2m....59m for minutes
                1h, 2h....23h - for hours 1d...7d - for days. Units cannot be combined (e.g. 1d2h is not allowed)
            type_: Supported values: FULL or MINI. If none provided, the default is FULL
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Rolling price ticker

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.rolling_window_price_change_statistics(
            symbol=symbol, symbols=symbols, window_size=window_size, type_=type_, request_options=request_options
        ).unwrap()

    def symbol_order_book_ticker(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3TickerBookTickerResponse:
        """Best price/qty on the order book for a symbol or symbols.

        - If the symbol is not sent, bookTickers for all symbols will be returned in an array.

        Weight(IP):
        - ``2`` for a single symbol;
        - ``4`` when the symbol parameter is omitted;

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Order book ticker

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.symbol_order_book_ticker(
            symbol=symbol, symbols=symbols, request_options=request_options
        ).unwrap()

    def symbol_price_ticker(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3TickerPriceResponse:
        """Latest price for a symbol or symbols.

        - If the symbol is not sent, prices for all symbols will be returned in an array.

        Weight(IP):
        - ``2`` for a single symbol;
        - ``4`` when the symbol parameter is omitted;

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Price ticker

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.symbol_price_ticker(
            symbol=symbol, symbols=symbols, request_options=request_options
        ).unwrap()

    def test_connectivity(self, *, request_options: RequestOptionsOrDict | None = None) -> Any:
        """Test connectivity to the Rest API.

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.test_connectivity(request_options=request_options).unwrap()

    def trading_day_ticker(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        time_zone: str | None = None,
        type_: TypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3TickerTradingDayResponse:
        """Price change statistics for a trading day.

        Notes:
        - Supported values for timeZone:
          - Hours and minutes (e.g. -1:00, 05:45)
          - Only hours (e.g. 0, 8, 4)

        Weight:
        - ``4`` for each requested symbol.
        - The weight for this request will cap at ``200`` once the number of symbols in the request is more than ``50``.

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            time_zone: Default: 0 (UTC)
            type_: Supported values: FULL or MINI. If none provided, the default is FULL
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trading day ticker

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.trading_day_ticker(
            symbol=symbol, symbols=symbols, time_zone=time_zone, type_=type_, request_options=request_options
        ).unwrap()

    def ui_klines(
        self,
        symbol: str,
        interval: IntervalOrStr,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        time_zone: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[list[ApiV3UiKlinesResponse]]:
        """The request is similar to klines having the same parameters and response.

        uiKlines return modified kline data, optimized for presentation of candlestick charts.

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            interval: kline intervals
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            time_zone: Default: 0 (UTC)
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            UIKline data

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.ui_klines(
            symbol,
            interval,
            start_time=start_time,
            end_time=end_time,
            time_zone=time_zone,
            limit=limit,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> MarketWithRawResponse:
        return self._with_raw_response


class AsyncMarket:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncMarketWithRawResponse(client, server)

    async def hr_ticker_price_change_statistics24(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        type_: TypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3Ticker24HrResponse:
        """24 hour rolling window price change statistics. Careful when accessing this with no symbol.

        - If the symbol is not sent, tickers for all symbols will be returned in an array.

        Weight(IP):
        - ``2`` for a single symbol;
        - ``80`` when the symbol parameter is omitted;

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            type_: Supported values: FULL or MINI. If none provided, the default is FULL
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            24hr ticker

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.hr_ticker_price_change_statistics24(
                symbol=symbol, symbols=symbols, type_=type_, request_options=request_options
            )
        ).unwrap()

    async def check_server_time(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiV3TimeResponse:
        """Test connectivity to the Rest API and get the current server time.

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Binance server UTC timestamp

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.check_server_time(request_options=request_options)).unwrap()

    async def compressed_aggregate_trades_list(
        self,
        symbol: str,
        *,
        from_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[AggTrade]:
        """Get compressed, aggregate trades. Trades that fill at the time, from the same order, with the same price will
        have the quantity aggregated.
        - If ``fromId``, ``startTime``, and ``endTime`` are not sent, the most recent aggregate trades will be returned.
        - Note that if a trade has the following values, this was a duplicate aggregate trade and marked as invalid:

        p = '0' // price

          q = '0' // qty

          f = -1 // ﬁrst_trade_id

          l = -1 // last_trade_id

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            from_id: Trade id to fetch from. Default gets most recent trades.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trade list

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.compressed_aggregate_trades_list(
                symbol,
                from_id=from_id,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                request_options=request_options,
            )
        ).unwrap()

    async def current_average_price(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV3AvgPriceResponse:
        """Current average price for a symbol.

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Average price

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.current_average_price(symbol, request_options=request_options)).unwrap()

    async def exchange_information(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        permissions: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3ExchangeInfoResponse:
        """Current exchange trading rules and symbol information

        - If any symbol provided in either symbol or symbols do not exist, the endpoint will throw an error.
        - All parameters are optional.
        - permissions can support single or multiple values (e.g. SPOT, ["MARGIN","LEVERAGED"])
        - If permissions parameter not provided, the default values will be ["SPOT","MARGIN","LEVERAGED"].
          - To display all permissions you need to specify them explicitly. (e.g. SPOT, MARGIN,...)

        Examples of Symbol Permissions Interpretation from the Response:
        - [["A","B"]] means you may place an order if your account has either permission "A" or permission "B".
        - [["A"],["B"]] means you can place an order if your account has permission "A" and permission "B".
        - [["A"],["B","C"]] means you can place an order if your account has permission "A" and permission "B" or
            permission "C". (Inclusive or is applied here, not exclusive or, so your account may have both permission
            "B" and permission "C".)

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            permissions: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Current exchange trading rules and symbol information

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.exchange_information(
                symbol=symbol, symbols=symbols, permissions=permissions, request_options=request_options
            )
        ).unwrap()

    async def kline_candlestick_data(
        self,
        symbol: str,
        interval: IntervalOrStr,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        time_zone: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[list[ApiV3KlinesResponse]]:
        """Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.

        - If ``startTime`` and ``endTime`` are not sent, the most recent klines are returned.

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            interval: kline intervals
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            time_zone: Default: 0 (UTC)
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Kline data

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.kline_candlestick_data(
                symbol,
                interval,
                start_time=start_time,
                end_time=end_time,
                time_zone=time_zone,
                limit=limit,
                request_options=request_options,
            )
        ).unwrap()

    async def old_trade_lookup(
        self,
        symbol: str,
        *,
        limit: int | None = None,
        from_id: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Trade]:
        """Get older market trades.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            limit: Default 500; max 1000.
            from_id: Trade id to fetch from. Default gets most recent trades.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trade list

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.old_trade_lookup(
                symbol, limit=limit, from_id=from_id, request_options=request_options
            )
        ).unwrap()

    async def order_book(
        self, symbol: str, *, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV3DepthResponse:
        """| Limit | Weight(IP) |
        |---------------------|-------------|
        | 1-100 | 5 |
        | 101-500 | 25 |
        | 501-1000 | 50 |
        | 1001-5000 | 250 |

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            limit: If limit > 5000, then the response will truncate to 5000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Order book

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.order_book(symbol, limit=limit, request_options=request_options)).unwrap()

    async def recent_trades_list(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[Trade]:
        """Get recent trades.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trade list

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.recent_trades_list(symbol, limit=limit, request_options=request_options)
        ).unwrap()

    async def rolling_window_price_change_statistics(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        window_size: str | None = None,
        type_: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3TickerResponse:
        """The window used to compute statistics is typically slightly wider than requested windowSize.

        openTime for /api/v3/ticker always starts on a minute, while the closeTime is the current time of the request.
        As such, the effective window might be up to 1 minute wider than requested.

        E.g. If the closeTime is 1641287867099 (January 04, 2022 09:17:47:099 UTC) , and the windowSize is 1d. the
        openTime will be: 1641201420000 (January 3, 2022, 09:17:00 UTC)

        Weight(IP): 4 for each requested symbol regardless of windowSize.

        The weight for this request will cap at 200 once the number of symbols in the request is more than 50.

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            window_size: Defaults to 1d if no parameter provided. Supported windowSize values: 1m,2m....59m for minutes
                1h, 2h....23h - for hours 1d...7d - for days. Units cannot be combined (e.g. 1d2h is not allowed)
            type_: Supported values: FULL or MINI. If none provided, the default is FULL
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Rolling price ticker

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.rolling_window_price_change_statistics(
                symbol=symbol, symbols=symbols, window_size=window_size, type_=type_, request_options=request_options
            )
        ).unwrap()

    async def symbol_order_book_ticker(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3TickerBookTickerResponse:
        """Best price/qty on the order book for a symbol or symbols.

        - If the symbol is not sent, bookTickers for all symbols will be returned in an array.

        Weight(IP):
        - ``2`` for a single symbol;
        - ``4`` when the symbol parameter is omitted;

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Order book ticker

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.symbol_order_book_ticker(
                symbol=symbol, symbols=symbols, request_options=request_options
            )
        ).unwrap()

    async def symbol_price_ticker(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3TickerPriceResponse:
        """Latest price for a symbol or symbols.

        - If the symbol is not sent, prices for all symbols will be returned in an array.

        Weight(IP):
        - ``2`` for a single symbol;
        - ``4`` when the symbol parameter is omitted;

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Price ticker

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.symbol_price_ticker(
                symbol=symbol, symbols=symbols, request_options=request_options
            )
        ).unwrap()

    async def test_connectivity(self, *, request_options: RequestOptionsOrDict | None = None) -> Any:
        """Test connectivity to the Rest API.

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.test_connectivity(request_options=request_options)).unwrap()

    async def trading_day_ticker(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        time_zone: str | None = None,
        type_: TypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV3TickerTradingDayResponse:
        """Price change statistics for a trading day.

        Notes:
        - Supported values for timeZone:
          - Hours and minutes (e.g. -1:00, 05:45)
          - Only hours (e.g. 0, 8, 4)

        Weight:
        - ``4`` for each requested symbol.
        - The weight for this request will cap at ``200`` once the number of symbols in the request is more than ``50``.

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            time_zone: Default: 0 (UTC)
            type_: Supported values: FULL or MINI. If none provided, the default is FULL
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trading day ticker

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.trading_day_ticker(
                symbol=symbol, symbols=symbols, time_zone=time_zone, type_=type_, request_options=request_options
            )
        ).unwrap()

    async def ui_klines(
        self,
        symbol: str,
        interval: IntervalOrStr,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        time_zone: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[list[ApiV3UiKlinesResponse]]:
        """The request is similar to klines having the same parameters and response.

        uiKlines return modified kline data, optimized for presentation of candlestick charts.

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            interval: kline intervals
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            time_zone: Default: 0 (UTC)
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            UIKline data

        Raises:
            ApiError: Bad Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.ui_klines(
                symbol,
                interval,
                start_time=start_time,
                end_time=end_time,
                time_zone=time_zone,
                limit=limit,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMarketWithRawResponse:
        return self._with_raw_response


class MarketWithRawResponse(BaseRawResponse[RawClient, Server]):
    def hr_ticker_price_change_statistics24(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        type_: TypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3Ticker24HrResponse, HrTickerPriceChangeStatistics24ErrorBody]:
        """24 hour rolling window price change statistics. Careful when accessing this with no symbol.

        - If the symbol is not sent, tickers for all symbols will be returned in an array.

        Weight(IP):
        - ``2`` for a single symbol;
        - ``80`` when the symbol parameter is omitted;

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            type_: Supported values: FULL or MINI. If none provided, the default is FULL
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/ticker/24hr"),
            query_params=[
                param[str | None]("symbol", symbol),
                param[str | None]("symbols", symbols),
                param[TypeOrStr | None]("type", type_),
            ],
            decoder=json_decoder[ApiV3Ticker24HrResponse],
            error_mapper=hr_ticker_price_change_statistics24_error_mapper,
            request_options=request_options,
        )

    def check_server_time(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV3TimeResponse, RawError]:
        """Test connectivity to the Rest API and get the current server time.

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/time"),
            decoder=json_decoder[ApiV3TimeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def compressed_aggregate_trades_list(
        self,
        symbol: str,
        *,
        from_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[AggTrade], CompressedAggregateTradesListErrorBody]:
        """Get compressed, aggregate trades. Trades that fill at the time, from the same order, with the same price will
        have the quantity aggregated.
        - If ``fromId``, ``startTime``, and ``endTime`` are not sent, the most recent aggregate trades will be returned.
        - Note that if a trade has the following values, this was a duplicate aggregate trade and marked as invalid:

        p = '0' // price

          q = '0' // qty

          f = -1 // ﬁrst_trade_id

          l = -1 // last_trade_id

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            from_id: Trade id to fetch from. Default gets most recent trades.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/aggTrades"),
            query_params=[
                param[str]("symbol", symbol),
                param[int | None]("fromId", from_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
            ],
            decoder=json_decoder[list[AggTrade]],
            error_mapper=compressed_aggregate_trades_list_error_mapper,
            request_options=request_options,
        )

    def current_average_price(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV3AvgPriceResponse, CurrentAveragePriceErrorBody]:
        """Current average price for a symbol.

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/avgPrice"),
            query_params=[param[str]("symbol", symbol)],
            decoder=json_decoder[ApiV3AvgPriceResponse],
            error_mapper=current_average_price_error_mapper,
            request_options=request_options,
        )

    def exchange_information(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        permissions: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3ExchangeInfoResponse, ExchangeInformationErrorBody]:
        """Current exchange trading rules and symbol information

        - If any symbol provided in either symbol or symbols do not exist, the endpoint will throw an error.
        - All parameters are optional.
        - permissions can support single or multiple values (e.g. SPOT, ["MARGIN","LEVERAGED"])
        - If permissions parameter not provided, the default values will be ["SPOT","MARGIN","LEVERAGED"].
          - To display all permissions you need to specify them explicitly. (e.g. SPOT, MARGIN,...)

        Examples of Symbol Permissions Interpretation from the Response:
        - [["A","B"]] means you may place an order if your account has either permission "A" or permission "B".
        - [["A"],["B"]] means you can place an order if your account has permission "A" and permission "B".
        - [["A"],["B","C"]] means you can place an order if your account has permission "A" and permission "B" or
            permission "C". (Inclusive or is applied here, not exclusive or, so your account may have both permission
            "B" and permission "C".)

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            permissions: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/exchangeInfo"),
            query_params=[
                param[str | None]("symbol", symbol),
                param[str | None]("symbols", symbols),
                param[str | None]("permissions", permissions),
            ],
            decoder=json_decoder[ApiV3ExchangeInfoResponse],
            error_mapper=exchange_information_error_mapper,
            request_options=request_options,
        )

    def kline_candlestick_data(
        self,
        symbol: str,
        interval: IntervalOrStr,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        time_zone: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[list[ApiV3KlinesResponse]], KlineCandlestickDataErrorBody]:
        """Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.

        - If ``startTime`` and ``endTime`` are not sent, the most recent klines are returned.

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            interval: kline intervals
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            time_zone: Default: 0 (UTC)
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/klines"),
            query_params=[
                param[str]("symbol", symbol),
                param[IntervalOrStr]("interval", interval),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[str | None]("timeZone", time_zone),
                param[int | None]("limit", limit),
            ],
            decoder=json_decoder[list[list[ApiV3KlinesResponse]]],
            error_mapper=kline_candlestick_data_error_mapper,
            request_options=request_options,
        )

    def old_trade_lookup(
        self,
        symbol: str,
        *,
        limit: int | None = None,
        from_id: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Trade], RawError]:
        """Get older market trades.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            limit: Default 500; max 1000.
            from_id: Trade id to fetch from. Default gets most recent trades.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/historicalTrades"),
            query_params=[
                param[str]("symbol", symbol), param[int | None]("limit", limit), param[int | None]("fromId", from_id)
            ],
            decoder=json_decoder[list[Trade]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def order_book(
        self, symbol: str, *, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV3DepthResponse, OrderBookErrorBody]:
        """| Limit | Weight(IP) |
        |---------------------|-------------|
        | 1-100 | 5 |
        | 101-500 | 25 |
        | 501-1000 | 50 |
        | 1001-5000 | 250 |

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            limit: If limit > 5000, then the response will truncate to 5000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/depth"),
            query_params=[param[str]("symbol", symbol), param[int | None]("limit", limit)],
            decoder=json_decoder[ApiV3DepthResponse],
            error_mapper=order_book_error_mapper,
            request_options=request_options,
        )

    def recent_trades_list(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Trade], RecentTradesListErrorBody]:
        """Get recent trades.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/trades"),
            query_params=[param[str]("symbol", symbol), param[int | None]("limit", limit)],
            decoder=json_decoder[list[Trade]],
            error_mapper=recent_trades_list_error_mapper,
            request_options=request_options,
        )

    def rolling_window_price_change_statistics(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        window_size: str | None = None,
        type_: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3TickerResponse, RollingWindowPriceChangeStatisticsErrorBody]:
        """The window used to compute statistics is typically slightly wider than requested windowSize.

        openTime for /api/v3/ticker always starts on a minute, while the closeTime is the current time of the request.
        As such, the effective window might be up to 1 minute wider than requested.

        E.g. If the closeTime is 1641287867099 (January 04, 2022 09:17:47:099 UTC) , and the windowSize is 1d. the
        openTime will be: 1641201420000 (January 3, 2022, 09:17:00 UTC)

        Weight(IP): 4 for each requested symbol regardless of windowSize.

        The weight for this request will cap at 200 once the number of symbols in the request is more than 50.

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            window_size: Defaults to 1d if no parameter provided. Supported windowSize values: 1m,2m....59m for minutes
                1h, 2h....23h - for hours 1d...7d - for days. Units cannot be combined (e.g. 1d2h is not allowed)
            type_: Supported values: FULL or MINI. If none provided, the default is FULL
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/ticker"),
            query_params=[
                param[str | None]("symbol", symbol),
                param[str | None]("symbols", symbols),
                param[str | None]("windowSize", window_size),
                param[str | None]("type", type_),
            ],
            decoder=json_decoder[ApiV3TickerResponse],
            error_mapper=rolling_window_price_change_statistics_error_mapper,
            request_options=request_options,
        )

    def symbol_order_book_ticker(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3TickerBookTickerResponse, SymbolOrderBookTickerErrorBody]:
        """Best price/qty on the order book for a symbol or symbols.

        - If the symbol is not sent, bookTickers for all symbols will be returned in an array.

        Weight(IP):
        - ``2`` for a single symbol;
        - ``4`` when the symbol parameter is omitted;

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/ticker/bookTicker"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("symbols", symbols)],
            decoder=json_decoder[ApiV3TickerBookTickerResponse],
            error_mapper=symbol_order_book_ticker_error_mapper,
            request_options=request_options,
        )

    def symbol_price_ticker(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3TickerPriceResponse, SymbolPriceTickerErrorBody]:
        """Latest price for a symbol or symbols.

        - If the symbol is not sent, prices for all symbols will be returned in an array.

        Weight(IP):
        - ``2`` for a single symbol;
        - ``4`` when the symbol parameter is omitted;

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/ticker/price"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("symbols", symbols)],
            decoder=json_decoder[ApiV3TickerPriceResponse],
            error_mapper=symbol_price_ticker_error_mapper,
            request_options=request_options,
        )

    def test_connectivity(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, RawError]:
        """Test connectivity to the Rest API.

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/ping"),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def trading_day_ticker(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        time_zone: str | None = None,
        type_: TypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3TickerTradingDayResponse, TradingDayTickerErrorBody]:
        """Price change statistics for a trading day.

        Notes:
        - Supported values for timeZone:
          - Hours and minutes (e.g. -1:00, 05:45)
          - Only hours (e.g. 0, 8, 4)

        Weight:
        - ``4`` for each requested symbol.
        - The weight for this request will cap at ``200`` once the number of symbols in the request is more than ``50``.

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            time_zone: Default: 0 (UTC)
            type_: Supported values: FULL or MINI. If none provided, the default is FULL
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/ticker/tradingDay"),
            query_params=[
                param[str | None]("symbol", symbol),
                param[str | None]("symbols", symbols),
                param[str | None]("timeZone", time_zone),
                param[TypeOrStr | None]("type", type_),
            ],
            decoder=json_decoder[ApiV3TickerTradingDayResponse],
            error_mapper=trading_day_ticker_error_mapper,
            request_options=request_options,
        )

    def ui_klines(
        self,
        symbol: str,
        interval: IntervalOrStr,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        time_zone: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[list[ApiV3UiKlinesResponse]], UiklinesErrorBody]:
        """The request is similar to klines having the same parameters and response.

        uiKlines return modified kline data, optimized for presentation of candlestick charts.

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            interval: kline intervals
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            time_zone: Default: 0 (UTC)
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/uiKlines"),
            query_params=[
                param[str]("symbol", symbol),
                param[IntervalOrStr]("interval", interval),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[str | None]("timeZone", time_zone),
                param[int | None]("limit", limit),
            ],
            decoder=json_decoder[list[list[ApiV3UiKlinesResponse]]],
            error_mapper=uiklines_error_mapper,
            request_options=request_options,
        )


class AsyncMarketWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def hr_ticker_price_change_statistics24(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        type_: TypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3Ticker24HrResponse, HrTickerPriceChangeStatistics24ErrorBody]:
        """24 hour rolling window price change statistics. Careful when accessing this with no symbol.

        - If the symbol is not sent, tickers for all symbols will be returned in an array.

        Weight(IP):
        - ``2`` for a single symbol;
        - ``80`` when the symbol parameter is omitted;

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            type_: Supported values: FULL or MINI. If none provided, the default is FULL
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/ticker/24hr"),
            query_params=[
                param[str | None]("symbol", symbol),
                param[str | None]("symbols", symbols),
                param[TypeOrStr | None]("type", type_),
            ],
            decoder=json_decoder[ApiV3Ticker24HrResponse],
            error_mapper=hr_ticker_price_change_statistics24_error_mapper,
            request_options=request_options,
        )

    async def check_server_time(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV3TimeResponse, RawError]:
        """Test connectivity to the Rest API and get the current server time.

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/time"),
            decoder=json_decoder[ApiV3TimeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def compressed_aggregate_trades_list(
        self,
        symbol: str,
        *,
        from_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[AggTrade], CompressedAggregateTradesListErrorBody]:
        """Get compressed, aggregate trades. Trades that fill at the time, from the same order, with the same price will
        have the quantity aggregated.
        - If ``fromId``, ``startTime``, and ``endTime`` are not sent, the most recent aggregate trades will be returned.
        - Note that if a trade has the following values, this was a duplicate aggregate trade and marked as invalid:

        p = '0' // price

          q = '0' // qty

          f = -1 // ﬁrst_trade_id

          l = -1 // last_trade_id

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            from_id: Trade id to fetch from. Default gets most recent trades.
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/aggTrades"),
            query_params=[
                param[str]("symbol", symbol),
                param[int | None]("fromId", from_id),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[int | None]("limit", limit),
            ],
            decoder=json_decoder[list[AggTrade]],
            error_mapper=compressed_aggregate_trades_list_error_mapper,
            request_options=request_options,
        )

    async def current_average_price(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV3AvgPriceResponse, CurrentAveragePriceErrorBody]:
        """Current average price for a symbol.

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/avgPrice"),
            query_params=[param[str]("symbol", symbol)],
            decoder=json_decoder[ApiV3AvgPriceResponse],
            error_mapper=current_average_price_error_mapper,
            request_options=request_options,
        )

    async def exchange_information(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        permissions: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3ExchangeInfoResponse, ExchangeInformationErrorBody]:
        """Current exchange trading rules and symbol information

        - If any symbol provided in either symbol or symbols do not exist, the endpoint will throw an error.
        - All parameters are optional.
        - permissions can support single or multiple values (e.g. SPOT, ["MARGIN","LEVERAGED"])
        - If permissions parameter not provided, the default values will be ["SPOT","MARGIN","LEVERAGED"].
          - To display all permissions you need to specify them explicitly. (e.g. SPOT, MARGIN,...)

        Examples of Symbol Permissions Interpretation from the Response:
        - [["A","B"]] means you may place an order if your account has either permission "A" or permission "B".
        - [["A"],["B"]] means you can place an order if your account has permission "A" and permission "B".
        - [["A"],["B","C"]] means you can place an order if your account has permission "A" and permission "B" or
            permission "C". (Inclusive or is applied here, not exclusive or, so your account may have both permission
            "B" and permission "C".)

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            permissions: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/exchangeInfo"),
            query_params=[
                param[str | None]("symbol", symbol),
                param[str | None]("symbols", symbols),
                param[str | None]("permissions", permissions),
            ],
            decoder=json_decoder[ApiV3ExchangeInfoResponse],
            error_mapper=exchange_information_error_mapper,
            request_options=request_options,
        )

    async def kline_candlestick_data(
        self,
        symbol: str,
        interval: IntervalOrStr,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        time_zone: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[list[ApiV3KlinesResponse]], KlineCandlestickDataErrorBody]:
        """Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.

        - If ``startTime`` and ``endTime`` are not sent, the most recent klines are returned.

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            interval: kline intervals
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            time_zone: Default: 0 (UTC)
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/klines"),
            query_params=[
                param[str]("symbol", symbol),
                param[IntervalOrStr]("interval", interval),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[str | None]("timeZone", time_zone),
                param[int | None]("limit", limit),
            ],
            decoder=json_decoder[list[list[ApiV3KlinesResponse]]],
            error_mapper=kline_candlestick_data_error_mapper,
            request_options=request_options,
        )

    async def old_trade_lookup(
        self,
        symbol: str,
        *,
        limit: int | None = None,
        from_id: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Trade], RawError]:
        """Get older market trades.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            limit: Default 500; max 1000.
            from_id: Trade id to fetch from. Default gets most recent trades.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/historicalTrades"),
            query_params=[
                param[str]("symbol", symbol), param[int | None]("limit", limit), param[int | None]("fromId", from_id)
            ],
            decoder=json_decoder[list[Trade]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def order_book(
        self, symbol: str, *, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV3DepthResponse, OrderBookErrorBody]:
        """| Limit | Weight(IP) |
        |---------------------|-------------|
        | 1-100 | 5 |
        | 101-500 | 25 |
        | 501-1000 | 50 |
        | 1001-5000 | 250 |

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            limit: If limit > 5000, then the response will truncate to 5000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/depth"),
            query_params=[param[str]("symbol", symbol), param[int | None]("limit", limit)],
            decoder=json_decoder[ApiV3DepthResponse],
            error_mapper=order_book_error_mapper,
            request_options=request_options,
        )

    async def recent_trades_list(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Trade], RecentTradesListErrorBody]:
        """Get recent trades.

        Weight(IP): 10

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/trades"),
            query_params=[param[str]("symbol", symbol), param[int | None]("limit", limit)],
            decoder=json_decoder[list[Trade]],
            error_mapper=recent_trades_list_error_mapper,
            request_options=request_options,
        )

    async def rolling_window_price_change_statistics(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        window_size: str | None = None,
        type_: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3TickerResponse, RollingWindowPriceChangeStatisticsErrorBody]:
        """The window used to compute statistics is typically slightly wider than requested windowSize.

        openTime for /api/v3/ticker always starts on a minute, while the closeTime is the current time of the request.
        As such, the effective window might be up to 1 minute wider than requested.

        E.g. If the closeTime is 1641287867099 (January 04, 2022 09:17:47:099 UTC) , and the windowSize is 1d. the
        openTime will be: 1641201420000 (January 3, 2022, 09:17:00 UTC)

        Weight(IP): 4 for each requested symbol regardless of windowSize.

        The weight for this request will cap at 200 once the number of symbols in the request is more than 50.

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            window_size: Defaults to 1d if no parameter provided. Supported windowSize values: 1m,2m....59m for minutes
                1h, 2h....23h - for hours 1d...7d - for days. Units cannot be combined (e.g. 1d2h is not allowed)
            type_: Supported values: FULL or MINI. If none provided, the default is FULL
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/ticker"),
            query_params=[
                param[str | None]("symbol", symbol),
                param[str | None]("symbols", symbols),
                param[str | None]("windowSize", window_size),
                param[str | None]("type", type_),
            ],
            decoder=json_decoder[ApiV3TickerResponse],
            error_mapper=rolling_window_price_change_statistics_error_mapper,
            request_options=request_options,
        )

    async def symbol_order_book_ticker(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3TickerBookTickerResponse, SymbolOrderBookTickerErrorBody]:
        """Best price/qty on the order book for a symbol or symbols.

        - If the symbol is not sent, bookTickers for all symbols will be returned in an array.

        Weight(IP):
        - ``2`` for a single symbol;
        - ``4`` when the symbol parameter is omitted;

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/ticker/bookTicker"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("symbols", symbols)],
            decoder=json_decoder[ApiV3TickerBookTickerResponse],
            error_mapper=symbol_order_book_ticker_error_mapper,
            request_options=request_options,
        )

    async def symbol_price_ticker(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3TickerPriceResponse, SymbolPriceTickerErrorBody]:
        """Latest price for a symbol or symbols.

        - If the symbol is not sent, prices for all symbols will be returned in an array.

        Weight(IP):
        - ``2`` for a single symbol;
        - ``4`` when the symbol parameter is omitted;

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/ticker/price"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("symbols", symbols)],
            decoder=json_decoder[ApiV3TickerPriceResponse],
            error_mapper=symbol_price_ticker_error_mapper,
            request_options=request_options,
        )

    async def test_connectivity(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Test connectivity to the Rest API.

        Weight(IP): 1

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/ping"),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def trading_day_ticker(
        self,
        *,
        symbol: str | None = None,
        symbols: str | None = None,
        time_zone: str | None = None,
        type_: TypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV3TickerTradingDayResponse, TradingDayTickerErrorBody]:
        """Price change statistics for a trading day.

        Notes:
        - Supported values for timeZone:
          - Hours and minutes (e.g. -1:00, 05:45)
          - Only hours (e.g. 0, 8, 4)

        Weight:
        - ``4`` for each requested symbol.
        - The weight for this request will cap at ``200`` once the number of symbols in the request is more than ``50``.

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            symbols: Value sent with the request.
            time_zone: Default: 0 (UTC)
            type_: Supported values: FULL or MINI. If none provided, the default is FULL
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/ticker/tradingDay"),
            query_params=[
                param[str | None]("symbol", symbol),
                param[str | None]("symbols", symbols),
                param[str | None]("timeZone", time_zone),
                param[TypeOrStr | None]("type", type_),
            ],
            decoder=json_decoder[ApiV3TickerTradingDayResponse],
            error_mapper=trading_day_ticker_error_mapper,
            request_options=request_options,
        )

    async def ui_klines(
        self,
        symbol: str,
        interval: IntervalOrStr,
        *,
        start_time: int | None = None,
        end_time: int | None = None,
        time_zone: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[list[ApiV3UiKlinesResponse]], UiklinesErrorBody]:
        """The request is similar to klines having the same parameters and response.

        uiKlines return modified kline data, optimized for presentation of candlestick charts.

        Weight(IP): 2

        Args:
            symbol: Trading symbol, e.g. BNBUSDT
            interval: kline intervals
            start_time: UTC timestamp in ms
            end_time: UTC timestamp in ms
            time_zone: Default: 0 (UTC)
            limit: Default 500; max 1000.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/v3/uiKlines"),
            query_params=[
                param[str]("symbol", symbol),
                param[IntervalOrStr]("interval", interval),
                param[int | None]("startTime", start_time),
                param[int | None]("endTime", end_time),
                param[str | None]("timeZone", time_zone),
                param[int | None]("limit", limit),
            ],
            decoder=json_decoder[list[list[ApiV3UiKlinesResponse]]],
            error_mapper=uiklines_error_mapper,
            request_options=request_options,
        )
