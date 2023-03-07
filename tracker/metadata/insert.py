import logging
import sys

from tracker import LogawareMixin, getenv_or_fail
from tracker.fetch.online import JsonEndpointFetcher
from tracker.metadata.retriever import LiftMetadataRetriever
from tracker.metadata.store import LiftMetadataDatabaseRecorder


class LiftMetadataInserter(LogawareMixin):
    def __init__(self, lift_metadata_retriever: LiftMetadataRetriever, database_client: LiftMetadataDatabaseRecorder):
        super().__init__()
        self.lift_metadata_retriever = lift_metadata_retriever
        self.database_client = database_client

    def insert(self):
        lift_metadata = []
        for page in range(1, 13):
            lift_metadata.extend(self.lift_metadata_retriever.lift_metadata(page))
        self._log.debug(f'recording lift state snapshot {lift_metadata}')
        self.database_client.record_all(lift_metadata)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s", stream=sys.stdout)
    recorder = LiftMetadataDatabaseRecorder(getenv_or_fail('MONGODB_PASS'))
    recorder.purge_data()
    snapshot_taker = LiftMetadataInserter(
        LiftMetadataRetriever(JsonEndpointFetcher.lift_metadata_fetcher(getenv_or_fail('DOLOMITI_BEARER'))),
        recorder
    )
    snapshot_taker.insert()
