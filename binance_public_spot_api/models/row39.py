from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .detail6 import Detail6, Detail6Dict
from .quota import Quota, QuotaDict


class Row39(SdkBaseModel):
    project_id: str = Field(alias="projectId")
    detail: Detail6
    quota: Quota


class Row39Dict(TypedDict):
    project_id: str
    detail: Detail6 | Detail6Dict
    quota: Quota | QuotaDict
