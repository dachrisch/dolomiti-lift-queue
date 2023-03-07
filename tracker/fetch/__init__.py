from abc import abstractmethod
from typing import Dict, Any, List


class JsonFetcher(object):
    @abstractmethod
    def fetch(self, part: str = '') -> List[Dict[str, Any]]:
        raise NotImplementedError
