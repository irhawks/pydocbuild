#!/usr/bin/env python3

import os
import subprocess

from selenium import webdriver

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

    def __init__ (self, command) :
        self._command = command

    ## 在execute当中启用多设置
    def execute(self, content) :

        self._process = subprocess.Popen(self._command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        self._process.stdin.write(content.encode())
        self._process.stdin.flush()
        out = self._process.communicate(content.encode())[0]
        self._process.stdin.close()

        return out.decode()

    def __del__ (self) :
        pass

## 这里包装的只是一个Selenium的接口
class SeleniumWrapper () : 
    
    def __init__ (self, browser) :

        if browser == 'firefox' : self._browser = webdriver.Firefox()
        if browser == 'phantomjs':self._browser = webdriver.PhantomJS()

    def execute(self, url) :
        self._browser.get(url)
        return self._browser

    def __del__ (self) :
        #self._browser.quit()
        pass

## 调用sed, 手动保持接口的一致性
class SedWrapper (PopenWrapper) :

    def __init__ (self, arguments=['']) :
        super().__init(command=['sed'] + arguments)

    def execute(self, contents) :
        return super().execute(contents)

class DefaultPandocWrapper(PopenWrapper) :

    def __init__(self) :
        super().__init__(['pandoc', "-f", "html", "-t", "markdown", "--wrap=none"])

    def execute(self, stdin) :
        return super().execute(stdin)

def test() :
    wrapper = PopenWrapper(["pandoc", "-f", "html", "-t", "markdown", "--wrap=none"])
    print(wrapper.execute("**Hello**"))
    print(wrapper.execute("**Hello, world**"))
    w2 = SeleniumWrapper('firefox')
    r = w2.execute('http://www.baidu.com')
    print(r.title)
    r2 = w2.execute('http://news.baidu.com')
    print(r2.title)
