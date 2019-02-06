import tornado.web

class NotFoundErrorHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.set_status(404)
    def get(self):
        self.write({
            "message": "Page not found"
        })