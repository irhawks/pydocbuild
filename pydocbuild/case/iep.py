from pydocbuild.util.executor import *
from pydocbuild.pipe.executor import *
from pydocbuild.util.markdowntrans import *

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
"""

class IepFromHtml(ComposeExecutor) :
    def __init__(self) :
        super().__init__(
            Pandoc("-f", "html", "-t", "commonmark", "--wrap=none"),
            Pandoc("-f", "commonmark", "-t", "markdown", "--wrap=none"),
            StripFigures())
