from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConfigDetail(SdkBaseModel):
    config_id: int = Field(alias="configId")
    """Mining ID"""

    pool_username: str = Field(alias="poolUsername")
    """Transfer out of subaccount"""

    to_pool_username: str = Field(alias="toPoolUsername")
    """Transfer into subaccount"""

    algo_name: str = Field(alias="algoName")
    """Transfer algorithm"""

    hash_rate: int = Field(alias="hashRate")
    """Transferred Hashrate quantity"""

    start_day: int = Field(alias="startDay")
    """Start date"""

    end_day: int = Field(alias="endDay")
    """End date"""

    status: int
    """0 Processing, 1：Cancelled, 2：Terminated"""


class ConfigDetailDict(TypedDict):
    config_id: int
    pool_username: str
    to_pool_username: str
    algo_name: str
    hash_rate: int
    start_day: int
    end_day: int
    status: int
