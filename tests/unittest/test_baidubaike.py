from pydocbuild.contents.baidubaike import *

class TestBaiduBaikeHtmlFilter :

    def test_baidubaike_html_filter(self) :
        wrapper = BaiduBaikeHtmlWrapper()
        out = wrapper.execute(open('testdata/baidubaike-hainan-university.html').read())
        print(out)
        assert True
