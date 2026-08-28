from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .ctr import Ctr, CtrDict


class SapiV1AssetAssetDetailResponse(SdkBaseModel):
    ctr: Ctr = Field(alias="CTR")


class SapiV1AssetAssetDetailResponseDict(TypedDict):
    ctr: Ctr | CtrDict
