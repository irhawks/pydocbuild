from pydocbuild.workflow.context.html_contexts import SeleniumContext

class TestSeleniumContext :

    def test_selenium_context(self) :
        wrapper = SeleniumContext(browser='phantomjs')
        wrapper.execute('http://www.baidu.com')
        wrapper.execute('http://www.qq.com')
        wrapper.teardown()

if __name__ == '__main__' :
    test() 

