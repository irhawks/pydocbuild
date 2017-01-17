技术手册
========

Python的打包
------------

distutils - Python自带的基本安装工具, 适用于非常简单的应用场景使用,
不支持依赖包的安装
　　通过distutils来打包，生成安装包，安装python包等工作，需要编写名为setup.py
python脚本文件。

setuptools - 针对 distutils 做了大量扩展,
尤其是加入了包依赖机制。不支持python3，安装完setuptools后会有easy\_install

distribute
-类似于setuptools，支持python3，安装完distribute后会有easy\_install。

easy\_install - setuptools 和 distribute 自带的安装脚本,
也就是一旦setuptools或distribute安装完毕, easy\_install 也便可用了。

pydoit使用的指南\[01-06-2017 15:12:49 CST\]
-------------------------------------------

[官网](pydoit.org)是我们的主要参考。仔细阅读我们就会发现一些技巧。比如给函数直接传递task关键字可以直接获取任务的所有的元数据。还有就是我们可以直接传递参数`**keywords`可以试图捕获所有类型的输入。

脚本的使用指南 \[01-06-2017 15:21:43 CST\]
------------------------------------------

自己觉得数据流与命名对于该脚本是关键的。在ETL框架之下我们起了Generator等等名子，但是这些名子似乎也并不总是能够全面地描述资源格式。

当前我们的任务大概可以这样说，在工作流的开始，是对于网页当中的内容的获取。这里，使用特定的Retriever和Wrapper来得到页面当中真正有用的内容。其实主要是通过打开浏览器或者使用一些Xpath过滤器之类的完成的任务。这个时候，任务名或许应该命名为`download_page_%(type)_%(topic)`。比如，假如我们是从清华大学网站上来获取页面资源，那么应该是`download_tsinghua_mirror_AOSP`这样的页面提示。这样就构成了一个任务。

对于其它的获取器，应该取怎样的名子呢？比如我们想从CDBLP当中得到期刊的介绍，应该怎样命名呢？这个时候，似乎应该是`download_cdblp_journal_计算机学报`了吧。但是有些时候，我们需要得到期刊的介绍这一目的的时候，我们又需要从多个路径查找。这个时候又该怎样办呢？似乎必须建立一个词典来保存内容。

对于计算机学报，其主页在[http://cjc.ict.ac.cn/](http://cjc.ict.ac.cn/\)
上面。我们或许应该这样组织资源：

    网站 = "http://cjc.ict.ac.cn/"
    刊物介绍 = """//table[@id="table10"]/tbody"""
    状态介绍 = """table[@id="table14"]/tbody"""
    下载专区 = """table[@id="table19"]/tbody"""
    ## 征稿指南之类的，链接到<http://cjc.ict.ac.cn/wltg/zgjz.htm>
    征稿指南 = """table[@id="table22"]/tbody"""
    ## 编委会人员列表
    http://cjc.ict.ac.cn/bwh/index.htm
    编辑委员会列表 = """table[@id="table21"]/tbody"""

我们发现，这样的网站本身结构是非常不规则的，它需要我们对于链接的生成具有高度的控制力才行。

    http://cjc.ict.ac.cn/bjb/index.htm
    上面的编辑部介绍是"""table[@id="table21"]/tbody"""，以后都是table21了。

    《计算机学报》2016年全年论文
    http://cjc.ict.ac.cn/qwjs/2016-all%20in%20one.htm
    //div[@class="Section1"]
    2015年的全年论文
    http://cjc.ict.ac.cn/qwjs/2015-all%20in%20one.htm

    大致来说CDBLP的定位应该是对于了解学科的发展有用的一个资讯文章。放在LIST分类当中或许更有用吧。

再比如介绍CCF的[http://www.ccf.org.cn/sites/ccf/ccfdsj.jsp?contentId=2526897246516](http://www.ccf.org.cn/sites/ccf/ccfdsj.jsp?contentId=2526897246516\)
网址。每页面大致是相同的，但是也有不同的地方。里面有各种不同的格式，在转换起来实在是难度有点大了。还有CCF的各个专业委员会的介绍页。

-   CCF专业委员会的介绍

CCF的奖项的首页[http://www.ccf.org.cn/sites/ccf/ccfawards.jsp](http://www.ccf.org.cn/sites/ccf/ccfawards.jsp\)
。我们需要得到各个奖项的获得情况。

doit的插件
----------

有一个doit-graphx的插件，可以帮助我们生成依赖图

<https://github.com/pydoit/doit-graphx>



# 技术手册

## Python的打包

distutils - Python自带的基本安装工具, 适用于非常简单的应用场景使用, 不支持依赖包的安装
　　通过distutils来打包，生成安装包，安装python包等工作，需要编写名为setup.py python脚本文件。

setuptools - 针对 distutils 做了大量扩展, 尤其是加入了包依赖机制。不支持python3，安装完setuptools后会有easy_install

distribute - 类似于setuptools，支持python3，安装完distribute后会有easy_install。

easy_install - setuptools 和 distribute 自带的安装脚本, 也就是一旦setuptools或distribute安装完毕, easy_install 也便可用了。


## pydoit使用的指南[01-06-2017 15:12:49 CST]

[官网](pydoit.org)是我们的主要参考。仔细阅读我们就会发现一些技巧。比如给函数直接传递task关键字可以直接获取任务的所有的元数据。还有就是我们可以直接传递参数`**keywords`可以试图捕获所有类型的输入。


## 脚本的使用指南 [01-06-2017 15:21:43 CST]

自己觉得数据流与命名对于该脚本是关键的。在ETL框架之下我们起了Generator等等名子，但是这些名子似乎也并不总是能够全面地描述资源格式。

当前我们的任务大概可以这样说，在工作流的开始，是对于网页当中的内容的获取。这里，使用特定的Retriever和Wrapper来得到页面当中真正有用的内容。其实主要是通过打开浏览器或者使用一些Xpath过滤器之类的完成的任务。这个时候，任务名或许应该命名为`download_page_%(type)_%(topic)`。比如，假如我们是从清华大学网站上来获取页面资源，那么应该是`download_tsinghua_mirror_AOSP`这样的页面提示。这样就构成了一个任务。

对于其它的获取器，应该取怎样的名子呢？比如我们想从CDBLP当中得到期刊的介绍，应该怎样命名呢？这个时候，似乎应该是`download_cdblp_journal_计算机学报`了吧。但是有些时候，我们需要得到期刊的介绍这一目的的时候，我们又需要从多个路径查找。这个时候又该怎样办呢？似乎必须建立一个词典来保存内容。

对于计算机学报，其主页在<http://cjc.ict.ac.cn/>上面。我们或许应该这样组织资源：

```
网站 = "http://cjc.ict.ac.cn/"
刊物介绍 = """//table[@id="table10"]/tbody"""
状态介绍 = """table[@id="table14"]/tbody"""
下载专区 = """table[@id="table19"]/tbody"""
## 征稿指南之类的，链接到<http://cjc.ict.ac.cn/wltg/zgjz.htm>
征稿指南 = """table[@id="table22"]/tbody"""
## 编委会人员列表
http://cjc.ict.ac.cn/bwh/index.htm
编辑委员会列表 = """table[@id="table21"]/tbody"""
```

我们发现，这样的网站本身结构是非常不规则的，它需要我们对于链接的生成具有高度的控制力才行。

```
http://cjc.ict.ac.cn/bjb/index.htm
上面的编辑部介绍是"""table[@id="table21"]/tbody"""，以后都是table21了。

《计算机学报》2016年全年论文
http://cjc.ict.ac.cn/qwjs/2016-all%20in%20one.htm
//div[@class="Section1"]
2015年的全年论文
http://cjc.ict.ac.cn/qwjs/2015-all%20in%20one.htm

大致来说CDBLP的定位应该是对于了解学科的发展有用的一个资讯文章。放在LIST分类当中或许更有用吧。
```


再比如介绍CCF的<http://www.ccf.org.cn/sites/ccf/ccfdsj.jsp?contentId=2526897246516>网址。每页面大致是相同的，但是也有不同的地方。里面有各种不同的格式，在转换起来实在是难度有点大了。还有CCF的各个专业委员会的介绍页。

* CCF专业委员会的介绍


CCF的奖项的首页<http://www.ccf.org.cn/sites/ccf/ccfawards.jsp>。我们需要得到各个奖项的获得情况。

## doit的插件

有一个doit-graphx的插件，可以帮助我们生成依赖图

<https://github.com/pydoit/doit-graphx>

## 在Web挖掘当中的僵化的思维[01-07-2017 09:10:34 CST]

现在我们意识到我们个体只是期望获取知识而已。这个时候，版面分析或许比直接分析DOM更为直接。这个时候自己也想起来一些现象。比如身边的人经常说挖掘Web的时候关键不是取下来，而是知道如何使用。但是对于递归下载，我们有网页爬虫可以使用。它可以帮助我们镜像一个网站生成本地的版本，从而加快预取的速度。不过，最为本质的方法，可能还是需要借助于网页的版面分析找到网页当中的关键内容。因为网页当中的重要的内容展示，都是展示出来面向人的。比如标题与导航栏的识别，就可以借助于CSS元素所计算出来的网页的宽度与位置等信息。借助于宽度与位置信息，或许我们能够更智能一些地分析问题。比如分析一个网站，并把网站的“重要信息”提取出来。所以，我们可以不只借助于DOM之类的内容。

另外，即使是对于DOM，我们也可以设计一些转换的程序。比如HTML表格，可以使用XSLT转换程序。该转换程序在linux下面是xlstproc命令。因为目前现在也有许多的XSLT的脚本了，所以把table等不易于展示的内容变换成易于展示的内容，也比较不错吧。这种处理方法以前自己觉得很难操作。但是现在既然linux下面有这样的命令，那么其实我们还是可以试一下XSLT转换语言的。再比如linux下面的xmllint工具。其实相对来说可能是更实用的方案吧。<http://stackoverflow.com/questions/9365810/simple-tool-to-learn-xquery>上面介绍了一系列的xquery的工具。除了xmllint之外，还有一个著名的工具就是[xqilla](http://xqilla.sourceforge.net/HomePage)。这个工具也可以直接在ubuntu上面下载。(其实我们可以找ubuntu的package列表)。在Ubuntu的Packages.gz文件当中很容易就能够找到软件包的数据库，metadata。这样的话也可以方便我们的检索（其实在ubuntu的官网上面就可以检索）。

这样的话，我们在寻找软件包的时候又有新的路线了。那就是各大语言的packagelist可以做成一个更大的软件包。形成一个软件库的百科大全。

另外，还有一个挖掘的技巧是涉及格式转换的。那就是有一些HTML表格可以使用libreoffice之类的打开。它们能够正确处理HTML的table元素。因此这也算是一种不错的方法。

<https://conversiontools.io/convert_html_to_csv/>上面还有一个自动的格式转换的工具。可以实现XML、PDF、CSV、XLS等多种格式的转换。另外，PDF也并非是不可修改。它可以使用pdfoo或者pdf2odt之类的工具。另外，libreoffice实际上能够编辑pdf，但是不能把pdf逆过来转成odt。<https://github.com/gutschke/pdf2odt>（然而pdfodt得到的是全图像的pdf）。其它的PDF工具用来抽取PDF里面的图片之类的也是有一些用处的。

<http://www.freeformatter.com/xsl-transformer.html>是类似于conversiontools.io的一个东西，提供在线的转换。

    In [89]: [e.text for e in e4[0].find_elements_by_xpath('./child::*')]

可以使用xpath帮助我们找到一个元素的子元素，然后计算其属性：

    traverse NULL = 0
    traverse [e] = [[e.width, traverse(e)] for e in list]

<http://blog.csdn.net/deng0jun/article/details/49869531>介绍了HTML文件的自动下载。
