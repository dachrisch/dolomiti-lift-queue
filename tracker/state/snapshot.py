import logging
import sys

from tracker import LogawareMixin, getenv_or_fail
from tracker.fetch.online import JsonEndpointFetcher
from tracker.state.retriever import LiftStateRetriever
from tracker.state.store import LiftStateDatabaseRecorder


class LiftStateSnapshotTaker(LogawareMixin):
    def __init__(self, lift_state_retriever:LiftStateRetriever, database_client:LiftStateDatabaseRecorder):
        super().__init__()
        self.lift_state_retriever = lift_state_retriever
        self.database_client = database_client

    def record_snapshot(self):
        lift_states = self.lift_state_retriever.current_lift_states()
        self._log.debug(f'recording lift state snapshot {lift_states}')
        self.database_client.record_all(lift_states)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", stream=sys.stdout)
    snapshot_taker = LiftStateSnapshotTaker(
        LiftStateRetriever(JsonEndpointFetcher.state_fetcher(getenv_or_fail('DOLOMITI_BEARER'))),
        LiftStateDatabaseRecorder(getenv_or_fail('MONGODB_PASS'))
    )
    snapshot_taker.record_snapshot()
