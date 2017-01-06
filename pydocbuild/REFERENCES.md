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
