import tornado.web
import concurrent.futures
from tornado.concurrent import run_on_executor

_executor = concurrent.futures.ProcessPoolExecutor()

class BaseRequestHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')


class ApplicationContexAwareRequestHandler(BaseRequestHandler):
    def initialize(self, app_context):
        self.app_context = app_context


class Index(ApplicationContexAwareRequestHandler):
    def get(self):
        self.write({
            'message': 'Hello there!'
        })


class Predict(ApplicationContexAwareRequestHandler):
    _process_pool = _executor

    async def get(self):
        stock_name = self.get_argument('stock')

        if not (stock_name and self.__validate_argument(stock_name)):
            self.__raise_http_400()
            return

        pipeline = self.app_context.model_registry.get_pipeline_by_id(stock_name)

        predicted_price = await self.__predict(pipeline, stock_name)

        self.write({
            'predicted': predicted_price
        })

    def __validate_argument(self, stock_name):
        return stock_name in self.app_context.model_registry.get_available_pipelines_ids()

    def __raise_http_400(self):
        self.set_status(400)
        self.finish({'message': 'Invalid request, check available models'})

    @run_on_executor(executor='_process_pool')
    def __predict(self, pipeline, stock_name):
        return pipeline.predict(stock_name)


class ListAvailableModels(ApplicationContexAwareRequestHandler):
    def get(self):
        self.write({
            'availableModels': self.app_context.model_registry.get_available_pipelines_ids()
        })
