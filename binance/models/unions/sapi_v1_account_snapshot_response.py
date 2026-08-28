from __future__ import annotations

from typing import TypeAlias

from ..snapshot_futures import SnapshotFutures, SnapshotFuturesDict
from ..snapshot_margin import SnapshotMargin, SnapshotMarginDict
from ..snapshot_spot import SnapshotSpot, SnapshotSpotDict

SapiV1AccountSnapshotResponse: TypeAlias = SnapshotSpot | SnapshotMargin | SnapshotFutures

SapiV1AccountSnapshotResponseDict: TypeAlias = SnapshotSpotDict | SnapshotMarginDict | SnapshotFuturesDict
