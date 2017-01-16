from pydocbuild.util.executor import *
from pydocbuild.pipe.executor import *
from pydocbuild.util.markdowntrans import *

class BaiduBaikeFromHtml(ComposeExecutor) :
    
    def __init__(self) :
        super().__init__(
            Pandoc("-f", "html", "-t", "commonmark", "--wrap=none"),
            Pandoc("-f", "commonmark", "-t", "markdown", "--wrap=none"),
            Sed("-e", r's/\\\*\\\*//g'),
            StripHeadBlanks(),
            StripTailBlanks(),
            Sed("-e", r's/^\[编辑\].*//',
                "-e", r's/<sup>\\\[\([0-9]\+\)\\\]<\/sup>/ [^\1]/g',
                "-e", r's/\s\+-\s\+\([0-9]\+\)\\\.[^)]\+)\s\+/[^\1]: /'),
            StripFigures())
