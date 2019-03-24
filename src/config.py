import json
import re
import logging as log

class ConfigLoader(object):
    def load(self):
        pass

    @staticmethod
    def create(file_path):
        if '.json' in file_path:
            return JsonConfigLoader(file_path)



class Config(object):
    def __init__(self):
        self.debug = None
        self.routes = None
        self.port = None
    
    def load(self, file_path):
        config = ConfigLoader.create(file_path).load()

        self.debug = config['debug']
        self.routes = config['networking']['routes']
        self.port = config['networking']['port']
        return self


class JsonConfigLoader(ConfigLoader):
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = None

    def load(self):
        try:
            with open(self.file_path) as fs:
                self.config = json.load(fs)
                return self.config
        except IOError as e:
            raise IOError("""Couldn't load config file.
                            Error message {0}""".format(e))