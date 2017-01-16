#!/usr/bin/env python3

from pydocbuild.pipe.executor import *

__doc__ = """
基本的对于程序的包装，如果只适用于特定的网站，则不放在workflow里面
"""

class Sed (ExternalExecutor) :
    """
    调用sed, 手动保持接口的一致性
    """
    def __init__ (self, *args) :
        """
        注，*是python的Use the unpacking operator: 
        set.intersection(*List_of_Sets)，
        它表示的是可以把一个列表中的元素抽取出来，即去掉列表里面的括号
        """
        super().__init__('sed', *args)

class Pandoc(ExternalExecutor) :

    def __init__(self, *args) :
        super().__init__('pandoc', *args)

class DefaultPandoc(Executor) :
    """
    缺省是从html转换成markdown
    """
    def __init__(self) :
        super().__init__('pandoc', "-f", "html", "-t", "markdown", "--wrap=none")
