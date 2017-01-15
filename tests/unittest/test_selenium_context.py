from pydocbuild.workflow.context.html_contexts import SeleniumContext

class TestSeleniumContext :

    def test_selenium_phantomjs_context(self) :

        wrapper = SeleniumContext(browser='phantomjs')

        e1 = wrapper.get_element('http://www.baidu.com')
        e1 = e1.title
        e2 = wrapper.get_content('http://www.qq.com')

        wrapper.teardown()

        assert "百度一下，你就知道" in e1
        assert 'QQ' in e2

    def test_selenium_firefox_context(self) :

        wrapper = SeleniumContext(browser='firefox')

        e1 = wrapper.get_element('http://www.baidu.com')
        e1 = e1.title
        e2 = wrapper.get_content('http://www.qq.com')

        wrapper.teardown()

        assert "百度一下，你就知道" in e1
        assert 'QQ' in e2
