# python-proxy-www
A simple implementation of [proxy-www](https://github.com/justjavac/proxy-www) using the power of python language

```python
import urllib


class HTTPProxy:
    def __init__(self, name='https://www'):
        self.name = name
        
    def __getattr__(self, name):
        return HTTPProxy(self.name + '.' + name)

    def request(self):
        return urllib.request.urlopen(self.name)


www = HTTPProxy()
```

Visit google:

```python
response = www.google.com.request()
response.status
# 200
```
