from dataclasses import dataclass
from types import NoneType
from typing import Dict, Any, List

from tracker.database import JsonDataclass


@dataclass
class LiftMetadata(JsonDataclass):
    id: str
    number: str
    name: Dict[str, str]
    type: Dict[str, Any]
    openingTime: str
    closingTime: str
    length: int
    altitude: dict[str, Any]
    capacity: int | NoneType
    coordinates: List[Dict[str, float]]
