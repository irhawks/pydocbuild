from pydocbuild.contents.stanford_plato import *

class TestStanfordPlato :

    def test_stanford_html_wrapper(self) :
        wrapper = StanfordHtmlWrapper()
        out = wrapper.execute(open('../testdata/baidubaike-hainan-university.html').read())
        print(out)
        assert 1==1

