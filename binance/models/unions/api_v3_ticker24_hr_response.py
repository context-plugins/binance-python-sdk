from __future__ import annotations

from typing import TypeAlias

from ..ticker import Ticker, TickerDict

ApiV3Ticker24HrResponse: TypeAlias = Ticker | list[Ticker]

ApiV3Ticker24HrResponseDict: TypeAlias = TickerDict | list[TickerDict]
