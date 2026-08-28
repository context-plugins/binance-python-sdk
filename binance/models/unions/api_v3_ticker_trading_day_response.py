from __future__ import annotations

from typing import TypeAlias

from ..day_ticker import DayTicker, DayTickerDict

ApiV3TickerTradingDayResponse: TypeAlias = DayTicker | list[DayTicker]

ApiV3TickerTradingDayResponseDict: TypeAlias = DayTickerDict | list[DayTickerDict]
