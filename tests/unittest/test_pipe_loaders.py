from pydocbuild.pipe.loader import *

class TestPipeLoaders :

    def test_internal_loader(self) :

        func = lambda f, opts : open(f,opts).read()
        f = '/proc/sys/net/ipv4/ip_forward'

        std = open(f,'r').read()
        assert InternalLoader(func,'r').load(f) == std

    def test_external_loader(self) :

        s = ExternalLoader("cat")
        f = '/proc/sys/net/ipv4/ip_forward'
        std = open(f,'r').read()

        assert s.load(f) == std
