from pydocbuild.util.executor import *
from pydocbuild.pipe.executor import *
from pydocbuild.util.markdowntrans import *

__doc__ = """
适用于斯坦福大学哲学百科全书的IEP解析器
https://plato.stanford.edu/entries/computing-history/
"""

class StanfordPlatoFromHtml(ComposeExecutor) :

    def __init__(self) :
        super().__init__(
            Pandoc("-f", "html", "-t", "commonmark", "--wrap=none"),
            Pandoc("-f", "commonmark", "-t", "markdown", "--wrap=none"))
