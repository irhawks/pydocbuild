from pydocbuild.pipe.loader import *

import requests

class Cat (ExternalLoader) :

    def __init__(self, *args) :
        super().__init__('cat', *args)

class PyRequest(InternalLoader) :

    def __init__(self, **opts) :
        self._opts = opts

    def load(self, uri) :
        r = requests.get(uri, **(self._opts))
        r.encoding='utf-8'
        return r.text

class PhantomjsRequestUrl(InternalLoader) :
    """
    需要selenium之类的辅助，优点在于可以执行javascript
    """
    def __init__(self, session) :
        self._session = session
    def load(self, uri) :
        return self._session.get_content(uri)
