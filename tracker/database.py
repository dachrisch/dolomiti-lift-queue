from pymongo import MongoClient
from pymongo.server_api import ServerApi

from tracker import LogawareMixin


class DatabaseRecorder(LogawareMixin):
    def __init__(self, password):
        super().__init__()
        self.client = MongoClient(
            f'mongodb+srv://dachrisch:{password}@base1.v0w2j1s.mongodb.net/?retryWrites=true&w=majority',
            server_api=ServerApi('1'))
        # invoke connect
        self.client.server_info()
        self._log.info(f'connecting to {self.client.primary}')
