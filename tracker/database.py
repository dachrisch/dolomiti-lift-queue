from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Protocol

from dacite import from_dict
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from tracker import LogawareMixin


@dataclass
class JsonDataclass(Protocol):
    @classmethod
    def from_json(cls, json_class_data: Dict[str, Any]):
        return from_dict(data_class=cls, data=json_class_data)

    def to_json(self):
        return asdict(self)


class DatabaseRecorder(LogawareMixin):
    def __init__(self, database, collection, password):
        super().__init__()
        self.database = database
        self.collection = collection
        self.client = MongoClient(
            f'mongodb+srv://dachrisch:{password}@base1.v0w2j1s.mongodb.net/?retryWrites=true&w=majority',
            server_api=ServerApi('1'))
        # invoke connect
        self.client.server_info()
        self._log.info(f'connecting to {self.client.primary}')

    def record_all(self, json_dataclasses: List[JsonDataclass]) -> List[str]:
        self._log.info(f'recording [{len(json_dataclasses)}] entries')
        json_data = self._map_to_json(json_dataclasses)
        return self._get_collection().insert_many(json_data).inserted_ids

    def purge_data(self):
        self._log.debug(f'deleting all data in collection [{self.collection}]')
        self._get_collection().delete_many({})

    def _map_to_json(self, json_dataclasses: List[JsonDataclass]) -> List[Dict[Any, Any]]:
        return list(map(lambda jd: jd.to_json(), json_dataclasses))

    def _get_collection(self):
        return self.client[self.database][self.collection]
