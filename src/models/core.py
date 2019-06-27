from models.exceptions import AbstractClassUsageError
from keras.models import load_model
import numpy as np
import json
import requests
import os


class BaseModel(object):
    def predict(self, x):
        raise AbstractClassUsageError


class KerasNeuralNetwork(BaseModel):
    def __init__(self, model):
        self.__model = model

    def predict(self, x):
        input = np.ndarray(shape=(1, 1, 1))
        input[0][0][0] = x
        return self.__model.predict(input)[0][0]


class StockDataProvider(object):
    def retrieve(self, stock_name):
        raise AbstractClassUsageError


class IEXProvider(StockDataProvider):
    def retrieve(self, stock_name):
        url = self.__current_price_endpoint(stock_name)
        price = requests.get(url).json()["latestPrice"]
        return price

    def __current_price_endpoint(self, stock_name):
        return "https://cloud.iexapis.com/beta/stock/{0}/quote?token=pk_72c946f9fa884fde8abbe6b7e2ed4a3d" \
            .format(stock_name)


class BaseTransformer(object):
    def fit_transform(self, x):
        raise AbstractClassUsageError

    def inverse_transform(self, x):
        raise AbstractClassUsageError


class StockNameToCurrentStockPriceTransformer(BaseTransformer):
    def __init__(self):
        super(StockNameToCurrentStockPriceTransformer, self).__init__()
        self.provider = IEXProvider()

    def fit_transform(self, x):
        return self.provider.retrieve(x)

    def inverse_transform(self, x):
        return x


class StandardScaler(BaseTransformer):
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def fit_transform(self, x):
        return (x - self.mean) / self.std

    def inverse_transform(self, x):
        return self.mean + (x * self.std)


class MinMaxScaler(BaseTransformer):
    def __init__(self, min_value=None, max_value=None, file=None):
        if file:
            self.__load_from_file(file)
        elif max and min:
            self.__set_from_arguments(min_value, max_value)
        else:
            self.__raise_value_error_if_no_argument()

    def __load_from_file(self, file):
        self.path = 'static/{0}/transformers/'.format(file) + 'min_max_scaler.json'
        with open(self.path) as fs:
            data = json.load(fs)
        self.min = data['min']
        self.max = data['max']

    def __set_from_arguments(self, min_value, max_value):
        self.min = min_value
        self.max = max_value

    def __raise_value_error_if_no_argument(self):
        raise ValueError

    def fit_transform(self, x):
        return (x - self.min) / (self.max - self.min)

    def inverse_transform(self, x):
        return (x * (self.max - self.min)) + self.min


class BasePipeline(object):
    def __init__(self):
        self.model = None
        self.transformers = []

    def predict(self, x):
        raise AbstractClassUsageError


class StockPricePipeline(BasePipeline):
    def __init__(self, pipeline_id):
        super(StockPricePipeline, self).__init__()
        self.pipeline_id = pipeline_id
        self.target_stock = pipeline_id
        self.transformers.append(StockNameToCurrentStockPriceTransformer())
        self.transformers.append(MinMaxScaler(file=self.target_stock))
        try:
            self.model = KerasNeuralNetwork(load_model('static/{0}/neural_networks/1.h5'.format(self.target_stock)))
        except OSError:
            raise FileNotFoundError

    def predict(self, x):
        data = x
        for t in self.transformers:
            data = t.fit_transform(data)
        data = self.model.predict(data)
        for inv_t in reversed(self.transformers):
            data = inv_t.inverse_transform(data)
        return data


class BasePipelineRegistry(object):
    def get_pipeline_by_id(self, x):
        raise AbstractClassUsageError

    def get_available_pipelines_ids(self):
        raise AbstractClassUsageError


class StockPricePipelineRegistry(BasePipelineRegistry):
    def __init__(self):
        self.pipelines = {}
        files_in_static = os.listdir('static/')
        try:
            files_in_static.remove('.DS_Store')
        except ValueError:
            pass
        for dir_in_static in files_in_static:
            try:
                self.pipelines[dir_in_static] = StockPricePipeline(dir_in_static)
            except FileNotFoundError:
                pass
        print('Found {0} complete pipelines'.format(len(self.pipelines.keys())))

    def get_pipeline_by_id(self, x):
        return self.pipelines[x]

    def get_available_pipelines_ids(self):
        return list(self.pipelines.keys())
