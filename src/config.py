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
    current = None
    def __init__(self):
        self.debug = None

        # Networking
        self.routes = None
        self.port = None
        self.host = None
        
        #NN Model
        self.h5_folder = None

        # Stock API
        self.stock_api = None
    
    def load(self, file_path):
        config = ConfigLoader.create(file_path).load()

        self.debug = config['debug']
        
        self.routes = config['networking']['routes']
        self.port = config['networking']['port']
        self.host = config['networking']['host']

        self.h5_folder = config['h5_location']
        self.stock_api = config['stock_api']

        Config.current = self # Set the new config to be accessible as a static variable
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