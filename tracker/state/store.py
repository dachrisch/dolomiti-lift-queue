from datetime import datetime
from typing import List, Dict

from tracker.database import DatabaseRecorder
from tracker.state import LiftState


class LiftStateDatabaseRecorder(DatabaseRecorder):
    def __init__(self, password):
        super().__init__(password)

    def record(self, lift_state: LiftState) -> str:
        self._log.info(f'recording lift state [{lift_state}]')
        snapshot_data = self.now_json() | lift_state.to_json()
        return self.get_snapshot_collection().insert_one(snapshot_data).inserted_id

    def record_all(self, lift_states: List[LiftState]) -> List[str]:
        self._log.info(f'recording [{len(lift_states)}] lift states')
        now_json = self.now_json()
        snapshot_data = map(lambda ls: now_json | ls.to_json(), lift_states)
        return self.get_snapshot_collection().insert_many(snapshot_data).inserted_ids

    def get_snapshot_collection(self):
        return self.client['dolomiti-ski']['lift-occupation']

    def now_json(self) -> Dict[str, datetime]:
        return {'snapshotTime': datetime.now()}
