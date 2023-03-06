from datetime import datetime
from typing import List, Dict

from pymongo import MongoClient
from pymongo.server_api import ServerApi

from tracker.schema.mixin import LogawareMixin
from tracker.schema.state import LiftState


class SnapshotDatabase(LogawareMixin):
    def __init__(self, password):
        super().__init__()
        self.client = MongoClient(
            f'mongodb+srv://dachrisch:{password}@base1.v0w2j1s.mongodb.net/?retryWrites=true&w=majority',
            server_api=ServerApi('1'))
        # invoke connect
        self.client.server_info()
        self._log.info(f'connecting to {self.client.primary}')

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
