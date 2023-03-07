import logging
import sys

from tracker import LogawareMixin, getenv_or_fail
from tracker.fetch.online import JsonEndpointFetcher
from tracker.skiarea.retriever import SkiAreaMetadataRetriever
from tracker.skiarea.store import SkiAreaMetadataDatabaseRecorder


class SkiAreaMetadataInserter(LogawareMixin):
    def __init__(self, ski_area_metadata_retriever: SkiAreaMetadataRetriever,
                 database_client: SkiAreaMetadataDatabaseRecorder):
        super().__init__()
        self.ski_area_metadata_retriever = ski_area_metadata_retriever
        self.database_client = database_client

    def insert(self):
        ski_area_metadata = self.ski_area_metadata_retriever.ski_area_metadata()
        self._log.debug(f'recording lift state snapshot {ski_area_metadata}')
        self.database_client.record_all(ski_area_metadata)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s", stream=sys.stdout)
    recorder = SkiAreaMetadataDatabaseRecorder(getenv_or_fail('MONGODB_PASS'))
    recorder.purge_data()
    snapshot_taker = SkiAreaMetadataInserter(
        SkiAreaMetadataRetriever(JsonEndpointFetcher.ski_area_fetcher(getenv_or_fail('DOLOMITI_BEARER'))),
        recorder
    )
    snapshot_taker.insert()
