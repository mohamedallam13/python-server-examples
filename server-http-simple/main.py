from http.server import HTTPServer, SimpleHTTPRequestHandler


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        match self.path:
            case '/':
                self.path = 'index.html'
                return SimpleHTTPRequestHandler.do_GET(self)           
            case '/lion':
                self.path = 'lion.html'
                return SimpleHTTPRequestHandler.do_GET(self)
            case '/giraffe':
                self.path = 'giraffe.html'
                return SimpleHTTPRequestHandler.do_GET(self)
            case _:
                self.path = 'notFound.html'
                return SimpleHTTPRequestHandler.do_GET(self)


def main():
    PORT = 8000
    server = HTTPServer(('', PORT), Handler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()
