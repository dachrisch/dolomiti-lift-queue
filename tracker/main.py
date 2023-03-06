import logging
import sys
from os import getenv, getcwd
from pathlib import Path

from tracker.fetch.file import JsonFileFetcher
from tracker.retriever import LiftStateRetriever
from tracker.store.database import SnapshotDatabase

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s", stream=sys.stdout)
    lift_states = LiftStateRetriever(
        JsonFileFetcher(Path(getcwd()).parent / 'json' / 'slopesLiftsState.json')).current_lift_states()
    print(lift_states)
    client = SnapshotDatabase(getenv('MONGODB_PASS', ''))
    client.record_all(lift_states)
