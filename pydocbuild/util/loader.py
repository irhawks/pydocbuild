from pydocbuild.pipe.loader import *

import requests

class Cat (ExternalLoader) :

    def __init__(self, *args) :
        super().__init__('cat', *args)

class PyRequest(InternalLoader) :

    def __init__(self) :
        pass

    def load(self, uri, *args) :
        r = requests.get(uri, *args)
        return r.text
