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
        super().__init__('pandoc', "-f", "html", "-t", "markdown", "--wrap=none")

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

## 适用于斯坦福大学哲学百科全书的IEP解析器
## https://plato.stanford.edu/entries/computing-history/

class StanfordHtmlFilter(CompositeWrapper) :

    def __init__(self) :
        super().__init__(
            PandocWrapper("-f", "html", "-t", "commonmark", "--wrap=none"),
            PandocWrapper("-f", "commonmark", "-t", "markdown", "--wrap=none"))

def testStanfordHtmlFilter() :
    wrapper = StanfordHtmlFilter()
    out = wrapper.execute(open('../testdata/baidubaike-hainan-university.html').read())
    print(out)

def testBaiduBaikeHtmlFilter() :
    wrapper = BaiduBaikeHtmlFilter()
    out = wrapper.execute(open('../testdata/baidubaike-hainan-university.html').read())
    print(out)


# <http://www.iep.utm.edu/stoicism/>哲学互联网百科的parser
## 其实每个Filter应该和这个网站的特定的解析Pattern结合的。比如说IEP，实际上其Pattern应该是特定的，
## 比如许多网站是byId的main-content，也有一些网站是byClass的，这些信息也该记录下来。
## 需要我们为特定的网站流而定义Filter
## iep的是div by class, class = entry-content，并在最后有Author的信息。
## 直接用VIM处理整个内容，需要使用如下的脚本：
### :%s/<.*\n*.\n.*\n.*\n<\/article>\(.*\n\)*//
### " vim当中可以使用特定行来替换
### :/^<!--\[if IE 7.*/,/^<div class="entry-content">$/s/.*\n/
### :%s/\[\]()\s*//
## " 去掉首行的列表转义
## :%s/^\\\((\d\+)\)/\1/

## 但是直接先处理的话，效果非常好，几乎可以直接使用pandoc将获得的HTML进行转换（by class过滤后）。
## 或者使用commonmark，效果也是非常不错的。
## 尽管如此，还是处理一下Fig吧。因为排版Figure会出现不少的错误

class InternetEncycloPhilosophyHtmlFilter(CompositeWrapper) :
    def __init__(self) :
        super().__init__(
            PandocWrapper("-f", "html", "-t", "commonmark", "--wrap=none"),
            PandocWrapper("-f", "commonmark", "-t", "markdown", "--wrap=none"),
            SedWrapper("-e", r's/!\[/[Fig：/g'))
    

## ---------------------------------------------------------------------------

## 也有一些文档是直接可以获得Wiki上面的元数据，对于这类内容，似乎我们应该换种方式。
## WikipediaWikitextFilter是作用在Wikitext格式上面的Filter。
## 但是Wiki的parsers还真的不那么容易去搞。
## <https://www.mediawiki.org/wiki/Alternative_parsers>介绍了一些parsers工具
## 其中mwlib是标准的受到官方支持的解析库，见<http://mwlib.readthedocs.io/en/latest/index.html>，但是只支持python2
## https://de.wikibooks.org/wiki/Benutzer:Dirk_Huenniger/wb2pdf,不错的工具
## mediawiki-parser这个Python包也可以。
## Finally, you can get the non-API part of MediaWiki to output raw article HTML using "action=render". See this example on the Stack Overflow article.
## https://www.mediawiki.org/wiki/API:Parsing_wikitext，提供了相应的API函数可以帮助解析

class WikipediaWikitextFilter(CompositeWrapper) :
    pass

## -------------------------------------------------------------------


if __name__ == '__main__' :
    #test()
    #testCompositeWrapper()
    #testBaiduBaikeHtmlFilter()
    testStanfordHtmlFilter()


__doc__ = """
wrapper也有单一的wrapper和复合的wrapper，一个复合的wrapper应该是多个单一wrapper的有序叠加。因此大概是这样的形成：
CompositeWrapper(wrapper_list).

这个时候函数的执行怎样实现呢？

"""
