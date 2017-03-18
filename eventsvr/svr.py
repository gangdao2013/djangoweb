import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def on_message(self, message):
        print(message)

    def on_close(self):
        self.redirect("http://www.baidu.com")

def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8341)
    tornado.ioloop.IOLoop.current().start()
