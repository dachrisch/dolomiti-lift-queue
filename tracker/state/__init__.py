from dataclasses import dataclass, asdict
from typing import Dict, Any

from dacite import from_dict


@dataclass
class LiftState:
    state: str
    queue: int
    metadata: Dict[str, Any]

    @classmethod
    def from_json(cls, lift_state: Dict[str, Any]):
        modified_lift_state_data = lift_state.copy()
        modified_lift_state_data['metadata'] = modified_lift_state_data.pop('slopeOrLift')
        return from_dict(data_class=LiftState, data=modified_lift_state_data)

    def to_json(self):
        return asdict(self)
