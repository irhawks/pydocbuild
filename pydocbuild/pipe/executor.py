__doc__ = """
wrapper也有单一的wrapper和复合的wrapper，
一个复合的wrapper应该是多个单一wrapper的有序叠加。因此大概是这样的形成：
CompositeWrapper(wrapper_list).

这个时候函数的执行怎样实现呢？

这里似乎只保存基本的程序就可以了，使用SystemWrapper(GenericWrappers)
这里换名成为了Agent，主要用于代理获取信息

执行器指的是对于一个程序的代理。这个执行器可以是内部执行器或者外部执行器

执行器最好能够将内部的程序与外部的程序联系起来。有一般的执行器，也有使用上下文的执行器。使用上下文的执行器不妨单独放在一个位置。

执行器有External和Internal，同样地，filter是一个executor、loader是一个executor、save也是一个executor。
"""

import os
import subprocess

class Executor :

    """Executor的标准的接口，应该是传递参数构建一个Executor，
    然后通过executor来执行一个操作，获得相应的输出
    """


class InternalExecutor (Executor) :

    """
    接受一个Python3的函数，然后调用这个函数
    """
    def __init__(self, func, *args) :
        self._func = func
        self._args = args

    def execute(self, content) :

        return self._func(content, *(self._args))

class ExternalExecutor (Executor) :

    """
    接受一个外部程序，然后执行这个程序
    """
    def __init__ (self, name, *args) :
        self._name = name
        self._args = args

    def execute(self, content) :
        """
        在execute当中启用多设置
        但是这样的wrapper似乎不是并行的，怎样改造成并行的呢？
        """
        self._process = subprocess.Popen([self._name] + [*self._args],
                stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        out = self._process.communicate(content.encode())[0]
        self._process.stdin.close()

        return out.decode()

class ContextExecutor (Executor) :

    """
    上下文执行器在指定的上下文当中执行任务
    """
    def __init__(self, context, func, *args) :
        self._func = func
        self._args = args
        self._context = context
    def execute(self, content) :
        pass

class ComposeExecutor(Executor) :
    def __init__(self, *executors) :
        self._executors = executors
    def execute(self, content) :
        result = content
        for e in self._executors :
            result = e.execute(result)
        return result

##--------------------------------------------------------------------
## 具体的执行器，能够包装Shell命令，以及Python的内部函数。
## 不建议使用

class Pipe (ExternalExecutor) :
    """
    基本的pipeline包装器
    """

    def __init__ (self, command) :
        self._command = command

    def execute(self, content) :
        r,w = os.pipe()
        os.write(w, content.encode())
        os.close(w)
        subprocess.check_call(self._command, stdin=r)
