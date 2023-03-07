import logging
import os


class LogawareMixin(object):
    def __init__(self):
        self._log = logging.getLogger(self.__class__.__name__)


class MissingEnvironmentVariable(Exception):
    pass


def getenv_or_fail(variable_name: str):
    try:
        return os.environ[variable_name]
    except KeyError:
        raise MissingEnvironmentVariable(f'required variable [{variable_name}] missing')
