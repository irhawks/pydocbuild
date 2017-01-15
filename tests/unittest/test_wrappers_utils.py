from pydocbuild.workflow.wrapper.utils import *

class TestUtilWrappers :

    def test_pandoc_wrapper(self) :
        wrapper = Pandoc("-f", "markdown", "-t", "html")
        assert "<p><strong>hello</strong></p>" == wrapper.execute("**Hello**")

    def test_sed_wrapper(self) :
        wrapper = Sed("-e", "s/e/abc/g")
        assert "**Habcllo**" == wrapper.execute("**Hello**")
