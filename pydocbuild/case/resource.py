from pydocbuild.util.executor import *
from pydocbuild.pipe.executor import *
from pydocbuild.util.markdowntrans import *
from pydocbuild.util import htmltrans
from .generic import *



__doc__ = """
<http://www.iep.utm.edu/stoicism/>哲学互联网百科的parser
其实每个Filter应该和这个网站的特定的解析Pattern结合的。比如说IEP，实际上其Pattern应该是特定的，
比如许多网站是byId的main-content，也有一些网站是byClass的，这些信息也该记录下来。
需要我们为特定的网站流而定义Filter
iep的是div by class, class = entry-content，并在最后有Author的信息。
直接用VIM处理整个内容，需要使用如下的脚本：
# :%s/<.*\n*.\n.*\n.*\n<\/article>\(.*\n\)*//
# " vim当中可以使用特定行来替换
# :/^<!--\[if IE 7.*/,/^<div class="entry-content">$/s/.*\n/
# :%s/\[\]()\s*//
 " 去掉首行的列表转义
 :%s/^\\\((\d\+)\)/\1/

但是直接先处理的话，效果非常好，几乎可以直接使用pandoc将获得的HTML进行转换（by class过滤后）。
或者使用commonmark，效果也是非常不错的。
尽管如此，还是处理一下Fig吧。因为排版Figure会出现不少的错误

需要注意的是，每个网站其实URL也是相对固定的。这里再列metadata，似乎内容显得还是有一点多余。
"""

## -------------------------------------------------------------------

converter_baidu_baike_html = ComposeExecutor(
    Pandoc("-f", "html", "-t", "commonmark", "--wrap=none"),
    Pandoc("-f", "commonmark", "-t", "markdown", "--wrap=none"),
    Sed("-e", r's/\\\*\\\*//g'),
    StripHeadBlanks(),
    StripTailBlanks(),
    Sed("-e", r's/^\[编辑\].*//',
        "-e", r's/<sup>\\\[\([0-9]\+\)\\\]<\/sup>/ [^\1]/g',
        "-e", r's/\s\+-\s\+\([0-9]\+\)\\\.[^)]\+)\s\+/[^\1]: /'),
    StripFigures())

def build_baidu_baike_html(metadata, **kwargs) :
    
    yield simple_webpage_build(metadata
            , converter= converter_baidu_baike_html
            , filter=InternalHtmlSelector(
                method="class"
                , pattern="main-content")
            , **kwargs
            )

## -------------------------------------------------------------------

__iep_doc__ = r"""
" vim脚本如下，表示的是将HTML文档中的多余部分去掉
" <http://www.iep.utm.edu/stoicism/>哲学互联网百科的parser
:%s/<.*\n*.\n.*\n.*\n<\/article>\(.*\n\)*//

" vim当中可以使用特定行来替换
:/^<!--\[if IE 7.*/,/^<div class="entry-content">$/s/.*\n/
:%s/\[\]()\s*//

" 去掉首行的列表转义
:%s/^\\\((\d\+)\)/\1/
"""


converter_iep_html = ComposeExecutor(
        Pandoc("-f", "html", "-t", "commonmark", "--wrap=none"),
        Pandoc("-f", "commonmark", "-t", "markdown", "--wrap=none"),
        StripFigures())

def build_iep_html(metadata, **kwargs) :
    
    yield simple_webpage_build(metadata
            , converter= converter_iep_html
            , filter=InternalHtmlSelector(
                method="class"
                , pattern="entry-content")
            , **kwargs
            )

## -------------------------------------------------------------------

__doc_plato_stanford__ = r"""
适用于斯坦福大学哲学百科全书的SEP解析器
https://plato.stanford.edu/entries/computing-history/
" 处理stanford的学术百科
" :%s/[.\n]\+\(.\+\n========\+\)/\2/
:/^<!--\[if lt IE 7*/,/^<!--DO NOT MODIFY THIS LINE AND ABOVE-->/d
:%s/^<!--.*-->\n//
:%s/^<div class="menu-block">\(.*\n\)*//g
:%s/\n<div id="\(.*\)">\n/^M/
:%s/^<\/div>$/^M/
:%s/\n<div class="\(.*\)">\n/^M/
:%s/\n\n\n*/^M^M/

" 处理掉列表的错误
:%s/^>\s\+ --\+ ----\+$//
:%s/^>$//

" 转换数学公式(行内公式与行间公式都转换
:%s/\\\\[()]/$/g
:%s/\\\\\\\[/$$/g
:%s/\\\\\\\]/$$/g
:%s/\\\([\^_]\)/\1/g
:%s/\\\\/\\/g
"""

converter_stanford_plato_html = ComposeExecutor(
    Pandoc("-f", "html", "-t", "commonmark", "--wrap=none"),
    Pandoc("-f", "commonmark", "-t", "markdown", "--wrap=none"))

def build_stanford_plato_html(metadata, **kwargs) :
    
    yield simple_webpage_build(metadata
            , converter= converter_stanford_plato_html
            , filter=InternalHtmlSelector(method="id", pattern="article")
            , **kwargs
            )

## -------------------------------------------------------------------

desc = """
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

converter_wikipedia_wikitext = ComposeExecutor(
        Pandoc("-f", "mediawiki", "-t", "html", "--wrap=none")
        , StripHtmlTableTag()
        , Pandoc("-f", "html", "-t", "commonmark", "--wrap=none")
        , StripFigures())

def build_wikipedia_wikitext(metadata, **kwargs) :
    
    yield simple_webpage_build(metadata
            , converter= converter_wikipedia_wikitext
            , filter=IdentityExecutor()
            , **kwargs
            )


def build_generic_wikitext(metadata, **kwargs) :

    yield simple_webpage_build(metadata
            , converter= ComposeExecutor(
                #Pandoc("-f", "mediawiki", "-t", "html", "--wrap=none"),
                #htmltrans.HtmlTableToCsvCode(),
                Pandoc("-f", "mediawiki", "-t", "markdown", "--wrap=none"),
                AddTopString(metadata['themes'][0] + '\n==============================================\n\n'),
                StripHeadBlanks(),
                StripDeepLists(),
                StripFigures()
                )
            , filter=IdentityExecutor()
            , path='wikipage/%s' % metadata['savename']
            #, **kwargs
            )


## -------------------------------------------------------------------

## -------------------------------------------------------------------
