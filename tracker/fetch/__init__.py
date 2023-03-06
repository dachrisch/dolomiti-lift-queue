from abc import abstractmethod
from typing import Dict, Any


class JsonFetcher(object):
    @abstractmethod
    def fetch(self, part: str = '') -> Dict[str, Any]:
        raise NotImplementedError
