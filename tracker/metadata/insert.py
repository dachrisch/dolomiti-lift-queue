import logging
import sys
from os import getenv

from tracker.fetch.online import JsonEndpointFetcher
from tracker.metadata.retriever import LiftMetadataRetriever
from tracker.metadata.store import LiftMetadataDatabaseRecorder
from tracker import LogawareMixin
from tracker.state.retriever import LiftStateRetriever
from tracker.state.store import LiftStateDatabaseRecorder


class LiftMetadataInserter(LogawareMixin):
    def __init__(self, lift_metadata_retriever:LiftMetadataRetriever, database_client:LiftMetadataDatabaseRecorder):
        super().__init__()
        self.lift_metadata_retriever = lift_metadata_retriever
        self.database_client = database_client

    def insert(self):
        lift_metadata = []
        for page in range(1,12):
            lift_metadata.extend(self.lift_metadata_retriever.lift_metadata(page))
        self._log.debug(f'recording lift state snapshot {lift_metadata}')
        self.database_client.record_all(lift_metadata)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s", stream=sys.stdout)
    snapshot_taker = LiftMetadataInserter(
        LiftMetadataRetriever(JsonEndpointFetcher.metadata_fetcher(getenv('DOLOMITI_BEARER', ''))),
        LiftMetadataDatabaseRecorder(getenv('MONGODB_PASS', ''))
        )
    snapshot_taker.insert()
