import os
import tornado.ioloop
import tornado.web
from request_handlers.rest_api import Index, Predict, ListAvailableModels
from request_handlers.errors import NotFoundErrorHandler

import models
import routing


class Application(object):
    def before_run(self):
        raise models.exceptions.AbstractClassUsageError

    def run(self):
        raise models.exceptions.AbstractClassUsageError


class ApplicationContext(object):
    def __init__(self,
                 configuration):
        self.configuration = configuration
        self.model_registry = models.StockPricePipelineRegistry()


class SPPApi(Application):
    def __init__(self, ctx):
        super().__init__()
        self.app_context = ctx

        self.route_builder = routing.DictRouteBuilder(self.app_context.configuration.routes)
        self.app = tornado.web.Application(handlers=[
            (self.route_builder.create('index'), Index, dict(app_context=self.app_context)),
            (self.route_builder.create('predictions'), Predict, dict(app_context=self.app_context)),
            (self.route_builder.create('availableModels'), ListAvailableModels, dict(app_context=self.app_context))
        ],
            default_host=self.app_context.configuration.host,
            debug=self.app_context.configuration.debug,
            default_handler_class=NotFoundErrorHandler)

    def run(self):
        self.app.listen(self.app_context.configuration.port)
        tornado.ioloop.IOLoop.current().start()
