import json
from os import path
from typing import Dict, Any, List

import requests as requests

from tracker import LogawareMixin
from tracker.fetch import JsonFetcher


class JsonEndpointFetcher(JsonFetcher, LogawareMixin):

    @staticmethod
    def state_fetcher(bearer):
        return JsonEndpointFetcher('https://app.dolomitisuperski.com/api/mobile/slopesLiftsState', bearer)

    @staticmethod
    def lift_metadata_fetcher(bearer):
        return JsonEndpointFetcher('https://app.dolomitisuperski.com/api/mobile/liftsNoState', bearer)

    @staticmethod
    def ski_area_fetcher(bearer):
        return JsonEndpointFetcher('https://app.dolomitisuperski.com/api/mobile/skiAreas', bearer)

    def __init__(self, endpoint, bearer):
        super().__init__()
        self.bearer = bearer
        self.endpoint = endpoint

    def fetch(self, part: str = '') -> List[Dict[str, Any]]:
        final_path = path.join(self.endpoint, part)
        self._log.info(f'loading json from [{final_path}]')
        response = requests.get(final_path, headers={'Authorization': f'Bearer {self.bearer}'})
        assert response.headers.get(
            'content-type') == 'application/json', f"not an JSON response, but [{response.headers.get('content-type')}]. Called the correct endpoint? [{final_path}]"
        assert response.status_code == 200, json.dumps(response.json(), indent=2)
        return response.json()
