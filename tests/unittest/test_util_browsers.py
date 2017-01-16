from pydocbuild.util.browser import SeleniumContext

class TestSeleniumContext :

    def test_selenium_phantomjs_context(self) :

        wrapper = SeleniumContext(browser='phantomjs')

        e1 = wrapper.get_element('http://www.baidu.com')
        e1 = e1.title
        e2 = wrapper.get_content('http://www.baidu.com')

        wrapper.teardown()

        assert "百度一下，你就知道" in e1
        assert '百度' in e2

    def test_selenium_firefox_context(self) :

        wrapper = SeleniumContext(browser='firefox')

        e1 = wrapper.get_element('http://www.baidu.com')
        e1 = e1.title
        e2 = wrapper.get_content('http://www.baidu.com')

        wrapper.teardown()

        assert "百度一下，你就知道" in e1
        assert '百度' in e2


class TestSeleniumSelectors :

    def test_selenium_firefox_filter(self) :
    
        session = SeleniumContext(browser='firefox')
        r = session.get_element('https://www.baidu.com')
        title = r.title
        session.teardown()
        assert "百度" in title
