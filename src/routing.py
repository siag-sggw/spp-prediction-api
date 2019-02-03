import json


class RouteBuilder(object):
    def create(self, key):
        pass


class FileRouteBuilder(RouteBuilder):
    def __init__(self, filepath, use_prefix=True):
        self.filepath = filepath
        self.using_prefix = use_prefix
        self.__routing_dict = None

    def create(self, key):
        if self.__routing_dict is None:
            with open(self.filepath, 'r') as filestream:
                self.__routing_dict = json.load(filestream)
        prefix = ""
        if self.using_prefix:
            prefix = self.__routing_dict['prefix']
        route = self.__routing_dict['routes'][key]
        return prefix + route


class DictRouteBuilder(RouteBuilder):
    def __init__(self, routing_dict, route_prefix=""):
        self.route_prefix = route_prefix
        self.routing_dict = routing_dict

    def create(self, key):
        return self.route_prefix + self.routing_dict[key]
