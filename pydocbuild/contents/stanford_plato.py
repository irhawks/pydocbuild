#!/usr/bin/env python3
from pydocbuild.workflow.wrapper import *

__doc__ = """
适用于斯坦福大学哲学百科全书的IEP解析器
https://plato.stanford.edu/entries/computing-history/
"""

class StanfordPlatoHtmlWrapper(Composite) :

    def __init__(self) :
        super().__init__(
            Pandoc("-f", "html", "-t", "commonmark", "--wrap=none"),
            Pandoc("-f", "commonmark", "-t", "markdown", "--wrap=none"))
