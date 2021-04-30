import urllib


class HTTPProxy:
    def __init__(self, name='https://www'):
        self.name = name
        
    def __getattr__(self, name):
        return HTTPProxy(self.name + '.' + name)

    def request(self):
        return urllib.request.urlopen(self.name)
    
    
www = HTTPProxy()
