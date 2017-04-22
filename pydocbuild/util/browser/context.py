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
from selenium.common.exceptions import TimeoutException


class SeleniumContext () : 
    """
    这里包装的只是一个Selenium的接口
    get_element返回selenium的对象
    get_content返回网页的内容
    """
    
    def __init__ (self, **kwargs) :

        #if browser == 'firefox' : self._browser = webdriver.Firefox()
        #if browser == 'phantomjs':self._browser = webdriver.PhantomJS()
        
        headers = { 'Accept':'*/*',
            'Accept-Language':'zh-CN,zh,en-US,en;q=0.8',
            'Cache-Control':'max-age=0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36' }
        
        for key in headers:
            DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = headers[key]
   
        browser=kwargs.get('browser', 'phantomjs')
        if browser == 'firefox' : 
            self._browser = WebDriver(desired_capabilities=DesiredCapabilities.FIREFOX)
        if browser == 'phantomjs':
            self._browser = WebDriver(desired_capabilities=DesiredCapabilities.PHANTOMJS)
        if 'timeout' in kwargs.keys() :
            self._browser.set_page_load_timeout(kwargs['timeout']) ## 最长加载Timeout的时间
            #self._browser.implicitly_wait(kwargs['timeout']) # seconds
        #print(self._browser.capabilities, "CAP")

    ## 需要以阻塞的方式执行
    def execute(self, url) :
        self._browser.get(url)
        return self._browser.page_source

    def get_element(self, url) :

        self._browser.get(url)
        return self._browser

    def get_content(self, url, timeout = 5) :

        ## reset timeout if needed 
        self._browser.set_page_load_timeout(timeout) ## 最长加载Timeout的时间
        try :
          self._browser.get(url)
        except TimeoutException :
          print('time out when loading page')
          self._browser.execute_script('window.stop()') #当页面加载时间超过设定时间，通过执行Javascript来stop加载，即可执行后续动作
        return self._browser.page_source

    def teardown (self) :
        self._browser.quit()
