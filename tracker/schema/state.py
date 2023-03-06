from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class LiftState:
    state: str
    queue: int
    metadata: Dict[str, Any]

    @classmethod
    def from_json(cls, lift_state):
        return LiftState(lift_state['state'], lift_state['queue'], lift_state['slopeOrLift'])

    def to_json(self):
        return asdict(self)
