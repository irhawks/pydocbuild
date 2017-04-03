from pydocbuild.case.iep import *

class TestBaiduBaikeHtmlFilter :

    def test_baidubaike_html_filter(self) :
        wrapper = IepFromHtml()
        out = wrapper.execute(open('testdata/baidubaike-hainan-university.html').read())
        assert True
