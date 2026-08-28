from __future__ import annotations

from typing import TypeAlias

from ..price_ticker import PriceTicker, PriceTickerDict

ApiV3TickerPriceResponse: TypeAlias = PriceTicker | list[PriceTicker]

ApiV3TickerPriceResponseDict: TypeAlias = PriceTickerDict | list[PriceTickerDict]
