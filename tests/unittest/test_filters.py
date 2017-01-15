
from pydocbuild.workflow.context.html_contexts import SeleniumContext

class TestSeleniumSelectors :

    def test_selenium_firefox_filter(self) :
    
        session = SeleniumContext(browser='firefox')
        r = session.get_element('https://www.baidu.com')
        title = r.title
        session.teardown()
        assert "百度" in title
