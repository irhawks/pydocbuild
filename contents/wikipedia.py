#!/usr/bin/env python3

__doc__ = """
也有一些文档是直接可以获得Wiki上面的元数据，对于这类内容，似乎我们应该换种方式。
WikipediaWikitextFilter是作用在Wikitext格式上面的Filter。
但是Wiki的parsers还真的不那么容易去搞。
<https://www.mediawiki.org/wiki/Alternative_parsers>介绍了一些parsers工具
其中mwlib是标准的受到官方支持的解析库，见<http://mwlib.readthedocs.io/en/latest/index.html>，但是只支持python2
https://de.wikibooks.org/wiki/Benutzer:Dirk_Huenniger/wb2pdf,不错的工具
mediawiki-parser这个Python包也可以。
Finally, you can get the non-API part of MediaWiki to output raw article HTML using "action=render". See this example on the Stack Overflow article.
https://www.mediawiki.org/wiki/API:Parsing_wikitext，提供了相应的API函数可以帮助解析
"""

class WikipediaWikitextWrapper(Composite) :
    pass
