#!/usr/bin/env python3

import os
import subprocess

# from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

## 基本的pipeline包装器

class PipelineWrapper() :

    def __init__ (self, command) :
        self._command = command

    def execute(self, content) :
        r,w = os.pipe()
        os.write(w, content.encode())
        os.close(w)
        subprocess.check_call(self._command, stdin=r)

    ## 直接这样放的话，会弄到stdout里面，

## 主要的pipeline包装器

class PopenWrapper () :

    def __init__ (self, *command) :
        self._command = command

    ## 在execute当中启用多设置
    def execute(self, content) :

        self._process = subprocess.Popen(self._command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        out = self._process.communicate(content.encode())[0]
        self._process.stdin.close()

        return out.decode()

    def __del__ (self) :
        pass

## 这里包装的只是一个Selenium的接口
class SeleniumWrapper () : 
    
    def __init__ (self, browser) :

        #if browser == 'firefox' : self._browser = webdriver.Firefox()
        #if browser == 'phantomjs':self._browser = webdriver.PhantomJS()
        if browser == 'firefox' : self._browser = WebDriver(desired_capabilities=DesiredCapabilities.FIREFOX)
        if browser == 'phantomjs':self._browser = WebDriver(desired_capabilities=DesiredCapabilities.PHANTOMJS)

    def execute(self, url) :
        self._browser.get(url)
        return self._browser

    def teardown (self) :
        #self._browser.quit()
        pass

    def __del__ (self) :
        self.teardown()
        pass

## 调用sed, 手动保持接口的一致性
class SedWrapper (PopenWrapper) :

    def __init__ (self, *arguments) :
        super().__init__('sed', *arguments)

    ## 注，*是python的Use the unpacking operator: set.intersection(*List_of_Sets)，它表示的是可以把一个列表中的元素抽取出来，即去掉列表里面的括号

class PandocWrapper(PopenWrapper) :

    def __init__(self, *args) :
        super().__init__('pandoc', *args)

class DefaultPandocWrapper(PopenWrapper) :

    def __init__(self) :
        super().__init__('pandoc', "-f", "html", "-t", "commonmark", "--wrap=none")

def test() :
    wrapper = DefaultPandocWrapper()
    print(wrapper.execute("**Hello**"))
    w = SedWrapper("-e", "s/e/abc/g")
    print(w.execute("**Hello**"))
    #print(wrapper.execute("**Hell*o*, world**"))
    #w2 = SeleniumWrapper('firefox')
    #r = w2.execute('http://www.baidu.com')
    #print(r.title)
    #r2 = w2.execute('http://news.baidu.com')
    #print(r2.title)

class CompositeWrapper() :
    def __init__(self, *wrapper_list) :
        self._wrappers = wrapper_list
    def execute(self, content) :
        result = content
        for wrapper in self._wrappers :
            result = wrapper.execute(result)
        return result

def testCompositeWrapper() :
    a = CompositeWrapper(SedWrapper("-e", "s/e/abc/g"), SedWrapper("-e", "s/a/def/g"))
    print(a.execute("hello"))


## ---------------------------------------------------------------------------
## 定义一些实用的filter，比如百度百科的filter

class BaiduBaikeHtmlFilter(CompositeWrapper) :
    
    def __init__(self) :
        super().__init__(
            PandocWrapper("-f", "html", "-t", "commonmark", "--wrap=none"),
            PandocWrapper("-f", "commonmark", "-t", "markdown", "--wrap=none"),
            SedWrapper("-e", r's/\\\*\\\*//g', 
                "-e", r's/^　\+/\n/', 
                "-e", r's/\\$//',
                "-e", r's/^\[编辑\].*//',
                "-e", r's/<sup>\\\[\([0-9]\+\)\\\]<\/sup>/ [^\1]/g',
                "-e", r's/\s\+-\s\+\([0-9]\+\)\\\.[^)]\+)\s\+/[^\1]: /',
                "-e", r's/!\[/[图片：/g'))

def testBaiduBaikeHtmlFilter() :
    wrapper = BaiduBaikeHtmlFilter()
    out = wrapper.execute(open('../testdata/baidubaike-hainan-university.html').read())
    print(out)

if __name__ == '__main__' :
    #test()
    #testCompositeWrapper()
    testBaiduBaikeHtmlFilter()


__doc__ = """
wrapper也有单一的wrapper和复合的wrapper，一个复合的wrapper应该是多个单一wrapper的有序叠加。因此大概是这样的形成：
CompositeWrapper(wrapper_list).

这个时候函数的执行怎样实现呢？

"""
