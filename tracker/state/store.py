from datetime import datetime
from typing import List, Dict, Any

from tracker.database import DatabaseRecorder, JsonDataclass


class LiftStateDatabaseRecorder(DatabaseRecorder):
    def __init__(self, password):
        super().__init__('dolomiti-ski', 'lift-occupation', password)

    def _map_to_json(self, json_dataclasses: List[JsonDataclass]) -> List[Dict[Any, Any]]:
        now_json = self.now_json()
        return list(map(lambda ls: now_json | ls.to_json(), json_dataclasses))

    def now_json(self) -> Dict[str, datetime]:
        return {'snapshotTime': datetime.now()}
