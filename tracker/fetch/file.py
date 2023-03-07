import json
from typing import Dict, Any, List

from tracker import LogawareMixin
from tracker.fetch import JsonFetcher


class JsonFileFetcher(JsonFetcher, LogawareMixin):

    def __init__(self, json_file):
        super().__init__()
        self.json_file = json_file

    def fetch(self, **kwargs) -> List[Dict[str, Any]]:
        self._log.info(f'loading json from [{self.json_file}]')
        with open(self.json_file) as file:
            return json.load(file)
