from pydocbuild.util.markdowntrans import *

class TestMarkdownTransformations :

    def test_strip_figures(self) :
        assert StripFigures().execute("![图](abc)") == "[Fig:图](abc)"

    def test_strip_headblanks(self) :
        assert StripHeadBlanks().execute("　　你好")== "\n你好"

    def test_strip_tailblanks(self) :
        assert StripTailBlanks().execute("abc \\") == "abc"
