import json
import logging as log

class ConfigLoader(object):
    def load(self):
        pass


class JsonConfigLoader(ConfigLoader):
    def __init__(self, filename):
        self.filename = filename
        self.config = None

    def load(self):
        try:
            with open(self.filename) as fs:
                self.config = json.load(fs)
                return self.config
        except IOError as e:
            raise IOError("""Couldn't load config file.
                            Error message {e}""")