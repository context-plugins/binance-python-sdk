from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bracket import Bracket, BracketDict


class SapiV1MarginLeverageBracketResponse(SdkBaseModel):
    asset_names: list[str] = Field(alias="assetNames")
    rank: int
    brackets: list[Bracket]


class SapiV1MarginLeverageBracketResponseDict(TypedDict):
    asset_names: list[str]
    rank: int
    brackets: list[Bracket | BracketDict]
