from datetime import datetime
from typing import List, Dict

from tracker.database import DatabaseRecorder
from tracker.metadata import LiftMetadata
from tracker.state import LiftState


class LiftMetadataDatabaseRecorder(DatabaseRecorder):
    def __init__(self, password):
        super().__init__(password)

    def record(self, lift_metadata: LiftMetadata) -> str:
        self._log.info(f'recording lift data [{lift_metadata}]')
        return self.get_metadata_collection().insert_one(lift_metadata.to_json()).inserted_id

    def record_all(self, lift_metadata: List[LiftMetadata]) -> List[str]:
        self._log.info(f'recording [{len(lift_metadata)}] lift metadata')
        snapshot_data = map(lambda lm: lm.to_json(), lift_metadata)
        return self.get_metadata_collection().insert_many(snapshot_data).inserted_ids

    def get_metadata_collection(self):
        return self.client['dolomiti-ski']['lift-metadata']

    def purge_data(self):
        self._log.debug(f'deleting all data in collection [{self.get_metadata_collection().name}]')
        self.get_metadata_collection().delete_many({})

