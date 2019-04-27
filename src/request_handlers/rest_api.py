import tornado.web
import src.models.api

class Index(tornado.web.RequestHandler):
    def get(self):
        self.write({
            'message': 'Hello there!'
        })

class Predict(tornado.web.RequestHandler):
    def get(self):
        model = src.models.api.KerasPredictor()
        
        stock_name = self.get_argument('stock')
        if not stock_name:
            self.set_status(400)
            return self.finish("Invalid request")
        
        look_ahead = 1
        try:
            given_look_ahead = self.get_argument('look_ahead')
            print(given_look_ahead)

            if look_ahead:
                look_ahead = given_look_ahead  
        except tornado.web.MissingArgumentError:
            pass
        
        self.write({
            'stock': model.do(stock_name, look_ahead=look_ahead),
        })