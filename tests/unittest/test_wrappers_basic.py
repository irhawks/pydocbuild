from pydocbuild.workflow.wrapper.basic import *

class TestCompositeWrapper :

    def test_compose_sed_filters() :
        a = Composite(
                Popen("sed", "-e", "s/e/abc/g"), 
                Popen("sed", "-e", "s/a/def/g"))
        assert "hdefbcllo" == a.execute("hello")
