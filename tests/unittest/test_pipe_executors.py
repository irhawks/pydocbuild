from pydocbuild.pipe.executor import *

class TestPipeExecutors :

    def test_internal_executor(self) :
        func = lambda x, opts: x*x if opts == '2' else x*x*x
        assert InternalExecutor(func,'2').execute(2) == 4
        assert InternalExecutor(func,'2').execute(3) == 9
        assert InternalExecutor(func,'x').execute(2) == 8
        assert InternalExecutor(func,'x').execute(3) == 27

    def test_external_executor(self) :
        s = ExternalExecutor("sed", "-e", "s/e/abc/g")
        assert s.execute("e") == 'abc'
        assert s.execute("ea")== 'abca'

    def test_compose_executor(self) :
        a = ComposeExecutor(
                ExternalExecutor("sed", "-e", "s/e/abc/g"), 
                ExternalExecutor("sed", "-e", "s/a/def/g"))
        assert "hdefbcllo" == a.execute("hello")

    def test_compose_mixed_executor(self) :
        func = lambda x, opts: x+x if opts == '2' else x+x+x
        internal = InternalExecutor(func,'2')
        external = ExternalExecutor("sed", "-e", "s/e/abc/g")
        mixed = ComposeExecutor(internal, external)
        assert mixed.execute("a") == "aa"
        assert mixed.execute("e") == "abcabc"
