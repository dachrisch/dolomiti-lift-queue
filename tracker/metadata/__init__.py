from dataclasses import dataclass, asdict
from types import NoneType
from typing import Dict, Any

from dacite import from_dict


@dataclass
class LiftMetadata:
    name: Dict[str, str]
    type: Dict[str, Any]
    openingTime: str
    closingTime: str
    length: int
    altitude: dict[str, Any]
    capacity: int | NoneType

    @classmethod
    def from_json(cls, lift_data: Dict[str, Any]):
        return from_dict(data_class=LiftMetadata, data=lift_data)

    def to_json(self):
        return asdict(self)
