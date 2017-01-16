from pydocbuild.case.baidubaike import *

class TestBaiduBaikeHtmlFilter :

    def test_baidubaike_html_filter(self) :
        wrapper = BaiduBaikeFromHtml()
        out = wrapper.execute(open('testdata/baidubaike-hainan-university.html').read())
        assert True
