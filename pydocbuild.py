#!/usr/bin/env python3

import os
import subprocess

from workflow import wrappers
from helpers.do_retrieve import *

## -------------------------------------------------------------------

## 在pydoit当中，任务指的是什么呢？任务指的是生成的顺序，或者计算顺序。一个任务产生确定的输出。简单来说，任务之间有单纯依赖关系而不是参数关系。

## 测试一下selenium吧。

### 构造一个tasklist的对象之后再进行处理。
tsinghua_mirror = {
    'url_pattern' :  "https://mirrors.tuna.tsinghua.edu.cn/help/%s",
    'topic_list' :["AOSP", "AUR","CocoaPods"],
#        , "anaconda","archlinux","archlinuxcn"
#        ,"bananian","centos","chromiumos","cygwin"
#        ,"docker","elpa","epel","fedora","git-repo"
#        ,"gitlab-ce","gitlab-ci-multi-runner"
#        ,"hackage","homebrew","homebrew-bottles"
#        ,"linux-stable.git","linux.git","lxc-images"
#        ,"mongodb","msys2","nodesource"
#        ,"pybombs","pypi"
#        ,"raspbian","repo-ck","repoforge","rpmfusion","rubygems"
#        ,"tensorflow","termux","ubuntu","virtualbox","weave"],
    'filter': {'method' : 'id', 'pattern' : 'help-content'}
    }

model_tsinghua = to_metadata(tsinghua_mirror)


## 注意在retrieve的时候使用什么样的会话来retrieve
global_selenium = wrappers.SeleniumWrapper('phantomjs')

def task_retrieve_tsinghua_pages() :

    yield yield_retrieve_page_list(global_selenium, model_tsinghua)


def task_combine_to_html () :

    yield combine_previous_task_results_as(model_tsinghua['task_list'], 'combine_to_html')


def task_html_to_markdown () :

    yield builder_for_html_to_markdown(['combine_to_html'], 'combine_to_html', "html_to_markdown")


def task_save_markdown () :

    yield builder_for_save_a_file(taskname="save_markdown ：保存markdown文件到磁盘中", 
            path='new-tsinghua.md',
            previous_task='html_to_markdown')

from doit.reporter import ConsoleReporter

class MyReporter(ConsoleReporter):
    def execute_task(self, task):
        self.outstream.write('Reporter : Running --> %s\n' % task.title())
        self.outstream.write('Reporter : %s depends --> %s\n' % (task.title(), task.task_dep) )

DOIT_CONFIG = {#'default_tasks': ['t3']
    'backend': 'json',
    'reporter': MyReporter,
    'status' : True,
    'continue': True,
    'verbosity': 2
}


if __name__ == '__main__':

    import doit
    doit.run(globals())
