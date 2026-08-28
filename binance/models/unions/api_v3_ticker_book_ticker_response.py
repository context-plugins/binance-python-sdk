from __future__ import annotations

from typing import TypeAlias

from ..book_ticker import BookTicker, BookTickerDict

ApiV3TickerBookTickerResponse: TypeAlias = BookTicker | list[BookTicker]

ApiV3TickerBookTickerResponseDict: TypeAlias = BookTickerDict | list[BookTickerDict]
