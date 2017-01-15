
from pydocbuild.workflow.context.html_contexts import SeleniumContext

class TestSeleniumSelectors :

    def test_webpage_filter(self) :
    
        w2 = SeleniumContext(browser='firefox')
        r = w2.execute('https://www.baidu.com')
        title = r.title
        w2.teardown()
        assert "百度" in title
