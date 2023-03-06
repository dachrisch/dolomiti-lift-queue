import logging
import sys
from os import getenv

from tracker.fetch import JsonFetcher
from tracker.fetch.online import JsonEndpointFetcher
from tracker.metadata import LiftMetadata
from tracker import LogawareMixin


class LiftMetadataRetriever(LogawareMixin):
    def __init__(self, json_fetcher: JsonFetcher):
        super().__init__()
        self.fetcher = json_fetcher

    def lift_metadata(self, page: int):
        lift_data = self.fetcher.fetch(f'{page}')
        self._log.debug(f'fetched [{len(lift_data)}] lift data')
        mapped_lift_data = list(map(lambda ld: LiftMetadata.from_json(ld), lift_data))
        return mapped_lift_data


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s", stream=sys.stdout)
    metadata_retriever = LiftMetadataRetriever(JsonEndpointFetcher.metadata_fetcher(getenv('DOLOMITI_BEARER', '')))
    print(metadata_retriever.lift_metadata(4))
