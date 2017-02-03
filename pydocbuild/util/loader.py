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
        ## 不使用这个方法进行判断了，使用apparent_encoding函数
        #if r.encoding=='ISO-8859-1' : r.encoding='GB18030'
        #else: r.encoding='utf-8'
        # 见<http://liguangming.com/python-requests-ge-encoding-from-headers>
        r.encoding = r.apparent_encoding
        return r.text

class PhantomjsRequestUrl(InternalLoader) :
    """
    需要selenium之类的辅助，优点在于可以执行javascript
    """
    def __init__(self, session) :
        self._session = session
    def load(self, uri) :
        return self._session.get_content(uri)
