from pydocbuild.util.executor import *

class TestUtilExecutors :

    def test_pandoc_executor(self) :
        wrapper = Pandoc("-f", "markdown", "-t", "html")
        assert "<p><strong>Hello</strong></p>\n" == wrapper.execute("**Hello**")

    def test_sed_executor(self) :
        wrapper = Sed("-e", "s/e/abc/g")
        assert "**Habcllo**" == wrapper.execute("**Hello**")
