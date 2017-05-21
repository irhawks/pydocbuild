from pydocbuild.pipe.loader import *

import requests
import chardet

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
        #r.encoding = r.apparent_encoding
        b = r.content

        ## 如果是二进制数据，提前返回内容
        if 'application/pdf' in r.headers['Content-Type'] :
          return b
        ## 如果是字符串数据，进行编码的归一化
        encoding = chardet.detect(b)['encoding']
        if encoding == 'gb2312' :
          return b.decode('GB18030')
        else :
          return b.decode(encoding)

class PhantomjsRequestUrl(InternalLoader) :
    """
    需要selenium之类的辅助，优点在于可以执行javascript
    """
    def __init__(self, session) :
        self._session = session
    def load(self, uri, timeout = 10) :
        return self._session.get_content(uri, timeout=timeout)
