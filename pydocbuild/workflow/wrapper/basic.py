#!/usr/bin/env python3

__doc__ = """
wrapper也有单一的wrapper和复合的wrapper，
一个复合的wrapper应该是多个单一wrapper的有序叠加。因此大概是这样的形成：
CompositeWrapper(wrapper_list).

这个时候函数的执行怎样实现呢？

这里似乎只保存基本的程序就可以了，使用SystemWrapper(GenericWrappers)
这里换名成为了Agent，主要用于代理获取信息
"""

import os
import subprocess


class Pipeline() :
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


class Popen() :
    """
    主要的pipeline包装器，使用subprocess通信，避免死锁
    """

    def __init__ (self, *command) :
        self._command = command

    def execute(self, content) :
        """
        在execute当中启用多设置
        但是这样的wrapper似乎不是并行的，怎样改造成并行的呢？
        """
        self._process = subprocess.Popen(self._command,
                stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        out = self._process.communicate(content.encode())[0]
        self._process.stdin.close()

        return out.decode()

    def __del__ (self) :
        pass

class Composite() :
    def __init__(self, *wrapper_list) :
        self._wrappers = wrapper_list
    def execute(self, content) :
        result = content
        for wrapper in self._wrappers :
            result = wrapper.execute(result)
        return result
