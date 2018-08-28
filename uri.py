import requests

HTTP = "http"
FILE = "file"

class UriHandler:
    def __init__(self, uri):
        self.protocol = uri.split(":")[0].lower()
        self.resource = uri.split("/")[2]
        self.uri = uri 
        print("URI handler initialized")
    def get(self):
        raise NotImplementedError()
    def get_contents(self):
        if self.protocol == HTTP:
            return HttpHandler(self.uri).get()
        if self.protocol == FILE:
            return FileHandler(self.uri).get()
    def __eq__(self, right):
        return super(UriHandler, self).__eq__(right)

class HttpHandler(UriHandler):
    def __init__(self, uri):
        super(HttpHandler, self).__init__(uri)
        print("HTTP handler initialized")
    def get(self):
        return requests.get(self.uri).text

class FileHandler(UriHandler):
    pass

print(UriHandler("http://wp.pl").get_contents())
print(50 * "=")
print(HttpHandler("http://wp.pl") == HttpHandler("http://wp.pl"))

