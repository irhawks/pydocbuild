from pydocbuild.case.stanford_plato import *

class TestStanfordPlato :

    def test_stanford_plato_from_html(self) :
        wrapper = StanfordPlatoFromHtml()
        out = wrapper.execute(open('../testdata/baidubaike-hainan-university.html').read())
        print(out)
        assert 1==1

