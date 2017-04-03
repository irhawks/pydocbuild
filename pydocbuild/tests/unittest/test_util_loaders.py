from pydocbuild.util.loader import *

class TestUtilLoaders :

    def test_cat_loader(self) :

        loader = Cat()
        f = '/proc/sys/net/ipv4/ip_forward'
        std = open(f,'r').read()

        assert loader.load(f) == std

    def test_pyrequests_loader(self) :

        loader = PyRequest()
        assert loader.load("http://www.baidu.com")[0] == "<"
