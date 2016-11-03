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


## 理想情况下的Pandoc编译

如下的例子：

    ```{.js .nwcode title="主文件的结构"}

    ```

其中.noweb和.js表明了这是接受nwcode(noweb的编译说明)的一种结构。title表明了主文件的结构。也就是相当于起到了定义Chunk的作用。但是我们知道，noweb是可以附加定义的，也就是利用它需要变换成LaTeX当中的特定的结构``<<title>>=``。也就是返回的.nw文件当中必须有它们。

自己搜索pandoc literate programming的时候，发现还是有一些预处理器可以做这些工具的。比如pandoc-lit只能处理literate haskell的格式<https://github.com/Toxaris/pandoc-lit>。也可以参考<http://members.shaw.ca/akochoi/articles/haskell-literate-programming-pandoc-carbon-xemacs/index.html>。再比如说，PP，它是一个pandoc的预处理器。<https://github.com/CDSoft/pp>可以阻止直接从pandoc生成文档，而首先进行一些预处理的工作。

    ```{.python execute=yes}

    ```

再比如spiralweb<https://github.com/michaeljmcd/spiralweb>系统。

其实文学编程是很简单的事情，只要从文章当中抽出来块名称和块定义就可以了。当然，块名称可以有许多个，块定义也可以有许多个。在块定义当中，应该能够智能地分辨出来哪些是代码，哪些是插入块的标记。于是本质上，还是需要我们能够根据块，推导块与块之间的依赖关系。本质上就是程序理解。比如一个函数调用了另一个函数，比如一个定义使用了另一个定义。深入理解程序之间的依赖关系是非常难的，因为需要深入到程序的数据结构当中。

Markdoc也是一个关于文学编程的工具，支持非常多的格式<http://markdoc.org/>。以及<https://github.com/haghish/MarkDoc>。但是需要配合Stata使用。
