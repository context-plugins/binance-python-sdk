from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

PortfolioMarginAccountUserDataErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _PortfolioMarginAccountUserDataError:
    def map(self, response: HttpResponse) -> PortfolioMarginAccountUserDataErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[Error](response)
            case _:
                return RawError(response)


portfolio_margin_account_user_data_error_mapper: Final[
    ErrorMapper[PortfolioMarginAccountUserDataErrorBody]
] = _PortfolioMarginAccountUserDataError()
