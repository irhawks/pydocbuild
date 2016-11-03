项目目录示范@2015年 05月 25日 星期一 22:03:52 CST
======================================================================

metadata.yaml是元配置文档。在里面定义各种字符串，如标题、作者、机构。Pandoc调用的时候，可以使用--metadata=your.yaml来指定元数据文档。

Metadata.yaml的配置可以参考 http://blog.martinfenner.org/2013/06/29/metadata-in-scholarly-markdown/ 这篇文章。

*正确配置参考文献* 参考文献需要使用--biblio-files=file-list而不是pandoc-citeproc。因为该程序的工作方式不正确。可以参考https://github.com/jgm/pandoc/issues/2041来解决这个问题。

学但是在我们学习Pandoc的时候，好像还没有办法使用Pandoc来排版。刚开始学习的时候我们没有办法做这件事，所以先把笔记记在纸上。

目前清楚的几点有：

* Pandoc具有~/.pandoc配置文件，该配置文件可能用于配置一些变量。
* Pandoc-gpp预处理器好像比较有用，后者好像是另外一种标记语言。
* 用Markdown写学术文档的话，应该使用所谓的ScholarMarkdown，
参考Writting Academic Papers in Markdown这篇文章。
* 在输出成LaTeX的时候，Pandoc借助于模板头文件实现LaTeX的排版。
这个模板是可以在pandoc命令中指定的。
* 过滤器很重要。应当好好使用。因为过滤器可以实现很多的功能扩展。
但是目前不知道过滤器是否支持多个参数。是否可以一次使用多个过滤器。
* github/kjhealy/pandoc-templates里面给出了一些工程配置参考。
* 自己也想过使用sbt构建Haskell的Pandoc。但是想想，还是比较复杂。
* 采用工程化的管理的时候，可以考虑把filters, csl, templates都放在一个子目录里面。这样会便于管理一些。
* 可在pandoc官方文档的Demo中找到一些有意义的例子。比如example9。
* pandoc一次可以编译多个文档。但是其中有一个是主要的，而且也包含yaml配置。
