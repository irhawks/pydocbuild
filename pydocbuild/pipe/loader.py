## 导入器，给出一个URL之类参数，得到里面的内容，类似于selenium

from .executor import *

class Loader (Executor):
    """
    load的第一个参数必须被定义为URI
    """

    def load(self, uri, args) :
        pass

class ExternalLoader (ExternalExecutor) :

    def load(self, uri) :

        self._process = subprocess.Popen([self._name] + [*self._args] + [uri],
                stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        out = self._process.communicate()[0]
        self._process.stdin.close()
        return out.decode()

class InternalLoader (InternalExecutor) :

    def load(self, uri) :
        return self.execute(uri)
