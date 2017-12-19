from tornado import web, httpserver, ioloop
import re
import json

class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write('Hello World')
        self.render('html/helloworld.html')
        print(*args)
        print(**kwargs)
    pass

class GetPythonHtml(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('html/hellopython.html')
        print(*args)
        print(**kwargs)
    pass

# class SayHello(web.RequestHandler):
#     def post(self,*args, **kwargs):
#         print(1111)
#     pass

application = web.Application([
    (r'/', MainPageHandler),
    (r'/python',GetPythonHtml),
    # (r'/sayhello',SayHello)
])

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()
    pass