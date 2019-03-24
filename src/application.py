import tornado.ioloop
import tornado.web

from request_handlers.api import Index
from request_handlers.errors import NotFoundErrorHandler


class Application(object):
    def __init__(self, config):
        self.config = config

    def run(self):
        pass

    def terminate(self):
        pass


class SPPApi(Application):
    def __init__(self,
                 config,
                 route_builder):
        super().__init__(config)
        self.route_builder = route_builder
        self.app = tornado.web.Application(handlers=[
            (self.route_builder.create('index'), Index)
        ],
            default_host=self.config.host,
            debug=self.config.debug,
            default_handler_class=NotFoundErrorHandler)
        self.app.listen(config.port)

    def run(self):
        tornado.ioloop.IOLoop.current().start()

    def terminate(self):
        pass
