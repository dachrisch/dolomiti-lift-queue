from dataclasses import dataclass
from typing import Dict, Any

from tracker.database import JsonDataclass


@dataclass
class LiftState(JsonDataclass):
    state: str
    queue: int
    metadata: Dict[str, Any]

    @classmethod
    def from_json(cls, lift_state: Dict[str, Any]):
        modified_lift_state_data = lift_state.copy()
        # rename key for consistency
        modified_lift_state_data['metadata'] = modified_lift_state_data.pop('slopeOrLift')
        # queue is sometimes None instead of 0, fix it
        if not modified_lift_state_data["queue"]:
            modified_lift_state_data["queue"] = 0
        return super().from_json(modified_lift_state_data)
