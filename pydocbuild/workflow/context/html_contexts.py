#!/usr/bin/env python3

__doc__ = """provide context for running programs (selenium context)
html contexts
可以使用不同的程序获取HTML的信息，并将其写入到暂存区当中。比如urllib
暂时也好像只有selenium需要context，其它的可以直接从HTML获取
"""

import os
import subprocess

# from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

## 这里包装的只是一个Selenium的接口

class SeleniumContext () : 
    
    def __init__ (self, **kwargs) :

        #if browser == 'firefox' : self._browser = webdriver.Firefox()
        #if browser == 'phantomjs':self._browser = webdriver.PhantomJS()
        browser=kwargs.get('browser', 'firefox')
        if browser == 'firefox' : 
            self._browser = WebDriver(desired_capabilities=DesiredCapabilities.FIREFOX)
        if browser == 'phantomjs':
            self._browser = WebDriver(desired_capabilities=DesiredCapabilities.PHANTOMJS)

    ## 需要以阻塞的方式执行
    def execute(self, url) :
        self._browser.get(url)
        return self._browser.page_source

    def get_element(self, url) :

        self._browser.get(url)
        return self._browser

    def teardown (self) :
        self._browser.quit()
