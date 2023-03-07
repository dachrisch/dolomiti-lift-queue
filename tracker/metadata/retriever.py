import logging
import sys

from tracker import LogawareMixin, getenv_or_fail
from tracker.fetch import JsonFetcher
from tracker.fetch.online import JsonEndpointFetcher
from tracker.metadata import LiftMetadata


class LiftMetadataRetriever(LogawareMixin):
    def __init__(self, json_fetcher: JsonFetcher):
        super().__init__()
        self.fetcher = json_fetcher

    def lift_metadata(self, page: int):
        lift_data = self.fetcher.fetch(f'{page}?version=V2')
        self._log.debug(f'fetched [{len(lift_data)}] lift data')
        return list(map(LiftMetadata.from_json, lift_data))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s", stream=sys.stdout)
    metadata_retriever = LiftMetadataRetriever(
        JsonEndpointFetcher.lift_metadata_fetcher(getenv_or_fail('DOLOMITI_BEARER')))
    print(metadata_retriever.lift_metadata(4))
