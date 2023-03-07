import logging
import sys

from tracker import LogawareMixin, getenv_or_fail
from tracker.fetch import JsonFetcher
from tracker.fetch.online import JsonEndpointFetcher
from tracker.skiarea import SkiArea


class SkiAreaMetadataRetriever(LogawareMixin):
    def __init__(self, json_fetcher: JsonFetcher):
        super().__init__()
        self.fetcher = json_fetcher

    def ski_area_metadata(self):
        ski_areas = self.fetcher.fetch()
        self._log.debug(f'fetched [{len(ski_areas)}] ski areas')
        return list(map(SkiArea.from_json, ski_areas))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s", stream=sys.stdout)
    ski_area_retriever = SkiAreaMetadataRetriever(
        JsonEndpointFetcher.ski_area_fetcher(getenv_or_fail('DOLOMITI_BEARER')))
    print(ski_area_retriever.ski_area_metadata())
