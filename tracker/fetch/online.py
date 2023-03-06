from typing import Dict, Any

import requests as requests

from tracker.fetch.base import JsonFetcher
from tracker.schema.mixin import LogawareMixin


class JsonEndpointFetcher(JsonFetcher, LogawareMixin):

    def __init__(self, endpoint, bearer):
        super().__init__()
        self.bearer = bearer
        self.endpoint = endpoint

    def fetch(self) -> Dict[str, Any]:
        self._log.info(f'loading json from [{self.endpoint}]')
        response = requests.get(self.endpoint, headers={'Authorization': f'Bearer {self.bearer}'})
        return response.json()
