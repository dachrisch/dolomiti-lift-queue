from tracker.fetch.base import JsonFetcher
from tracker.schema.mixin import LogawareMixin
from tracker.schema.state import LiftState


class LiftStateRetriever(LogawareMixin):
    def __init__(self, json_fetcher: JsonFetcher):
        super().__init__()
        self.fetcher = json_fetcher

    def current_lift_states(self):
        _all_states = self.fetcher.fetch()
        self._log.debug(f'fetched [{len(_all_states)}] entries')
        _lift_states = filter(lambda state: state['slopeOrLift']['type'] == 'lift', _all_states)
        _mapped_lift_states = list(map(lambda lift_state: LiftState.from_json(lift_state), _lift_states))
        self._log.debug(f'[{len(_mapped_lift_states)}] entries of lifts')
        return _mapped_lift_states
