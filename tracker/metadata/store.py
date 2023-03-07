from tracker.database import DatabaseRecorder


class LiftMetadataDatabaseRecorder(DatabaseRecorder):
    def __init__(self, password):
        super().__init__('dolomiti-ski', 'lift-metadata', password)
