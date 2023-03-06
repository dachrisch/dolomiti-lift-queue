import json
from typing import Dict, Any

from tracker.fetch.base import JsonFetcher
from tracker.schema.mixin import LogawareMixin


class JsonFileFetcher(JsonFetcher, LogawareMixin):

    def __init__(self, json_file):
        super().__init__()
        self.json_file = json_file

    def fetch(self) -> Dict[str, Any]:
        self._log.info(f'loading json from [{self.json_file}]')
        with open(self.json_file) as file:
            return json.load(file)
