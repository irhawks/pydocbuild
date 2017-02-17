__doc__ = """
转换markdown格式，比如去掉图片显示
"""

from pydocbuild.util.executor import *

class StripFigures (Sed) :
    
    def __init__(self) :
        super().__init__("-e", r's/!\[/[Fig:/g')

class StripHeadBlanks (Sed) :

    def __init__(self) :
        super().__init__("-e", r's/^　\+/\n/')

class StripTailBlanks (Sed) :

    def __init__(self) :
        super().__init__("-e", r's/[ \n\t\\]\+$//')

class StripDeepLists (Sed) :

    def __init__(self) :
        super().__init__("-e", r's/^-   \(-   \)\+/- /', "-e", r's/^\([0-9]\.  \)\([0-9]\.  \)\+/\1/')
