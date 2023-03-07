from dataclasses import dataclass
from typing import Dict, List

from tracker.database import JsonDataclass


@dataclass
class SkiArea(JsonDataclass):
    name: Dict[str, str]
    id: str
    boundary: Dict[str, List[Dict[str, float]]]
