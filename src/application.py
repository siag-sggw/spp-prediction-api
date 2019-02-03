import tornado.ioloop
import tornado.web

from request_handlers.index import Index

class Application(object):
    def __init__(self, config):
        self.config = config

    def run(self):
        pass

    def terminate(self):
        pass


class TornadoApplication(Application):
    def __init__(self, config):
        super().__init__(config)
        self.app = tornado.web.Application([
            ('/', Index)
        ])
        self.app.listen(config['networking']['port'])

    def run(self):
        tornado.ioloop.IOLoop.current().start()

    def terminate(self):
        pass
