import tornado.web
import re

class ApplicationContexAwareRequestHandler(tornado.web.RequestHandler):
    def initialize(self, app_context):
        self.app_context = app_context


class Index(ApplicationContexAwareRequestHandler):
    def get(self):
        self.write({
            'message': 'Hello there!'
        })


class Predict(ApplicationContexAwareRequestHandler):
    def get(self):
        stock_name = self.get_argument('stock')
        
        if not(stock_name and self.__validate_argument(stock_name)):
            self.__raise_http_400()
            return

        pipeline = self.app_context.model_registry.get_pipeline_by_id(stock_name)
        self.write({
            'predicted': pipeline.predict(stock_name)
        })

    def __validate_argument(self, stock_name):
        return stock_name in self.app_context.model_registry.get_available_pipelines_ids()

    def __raise_http_400(self):
        self.set_status(400)
        self.finish({'message': 'Invalid request, check available models'})


class ListAvailableModels(ApplicationContexAwareRequestHandler):
    def get(self):
        self.write({
            'availableModels': self.app_context.model_registry.get_available_pipelines_ids()
        })
