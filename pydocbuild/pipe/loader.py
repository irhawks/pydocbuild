## 导入器，给出一个URL之类参数，得到里面的内容，类似于selenium

from .executor import *

class Loader (Executor):

    def load(self, uri, args) :
        pass

class ExternalLoader (ExternalExecutor) :

    def load(self, path) :

        self._process = subprocess.Popen([self._name] + [*self._args] + [path],
                stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        out = self._process.communicate()[0]
        self._process.stdin.close()
        return out.decode()

class InternalLoader (InternalExecutor) :

    def load(self, path) :
        return self.execute(path)
