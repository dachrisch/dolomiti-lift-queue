from tracker.database import DatabaseRecorder


class SkiAreaMetadataDatabaseRecorder(DatabaseRecorder):
    def __init__(self, password):
        super().__init__('dolomiti-ski', 'skiarea-metadata', password)
