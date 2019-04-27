import requests
import keras.models
import numpy

import src.config as config


class Predictor(object):
    def do(self, stock_name, look_ahead=1):
        pass


class StockDataProvider(object):
    def retrieve(self, stock_name):
        pass


class IEXProvider(StockDataProvider):
    def retrieve(self, stock_name):
        url = self.__current_price_endpoint()
        api_key = config.Config.current.stock_api['api_key']
        result_key = config.Config.current.stock_api['endpoints']['current_price']['key'] 
        
        url = url.format(stock=stock_name, token=api_key)
        return requests.get(url).json()[result_key]

    def __current_price_endpoint(self):
        current_conf = config.Config.current
        return current_conf.stock_api['host'] + \
               current_conf.stock_api['version'] + \
               current_conf.stock_api['endpoints']['current_price']['url']    


class KerasPredictor(Predictor):
    def __init__(self, **load_model_kwargs):
        self.model = None
        self.__price_provider = IEXProvider()
        self.__load_model_kwargs = load_model_kwargs

    def do(self, stock_name, look_ahead=1):
        self.__load_model(stock_name, look_ahead)
        current_price = self.__price_provider.retrieve(stock_name)

        nn_input = numpy.array([current_price])
        nn_input = numpy.reshape(nn_input, (nn_input.shape[0], look_ahead, 1))

        prediction = self.model.predict(nn_input) 

        return self.__format_prediction(prediction)

    def __format_prediction(self, prediction):
        result = prediction.flatten().tolist()
        if len(result) == 1:
            return result[0]
        else:
            return -1

    def __load_model(self, stock_name, look_ahead):
        model_path = config.Config.current.h5_folder + '{0}-{1}.h5' \
                                          .format(stock_name, look_ahead)
                        
        self.model = keras.models.load_model(model_path, 
                                             **self.__load_model_kwargs)