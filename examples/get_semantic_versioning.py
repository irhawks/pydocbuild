#!/usr/bin/env python3


import os
import subprocess

from pydocbuild.workflow import wrapper
from pydocbuild.workflow import context
from pydocbuild.workflow import filters
from pydocbuild import taskgen

## 注意在retrieve的时候使用什么样的会话来retrieve
## 缺省就使用selenium


## 1. 处理元数据
SemanticVersioningWebInfo = {
    'url_pattern' :  "http://semver.org/lang/%s",
    'topic_list' :["zh-CN", "en"],
    'filter': {'method' : 'id', 'pattern' : 'spec'}
}
SV = taskgen.to_metadata(SemanticVersioningWebInfo)

## 2. 建立浏览器上下文
selenium_session = context.SeleniumContext(browser='firefox')

## 生成到markdown的转换任务
def task_retrieve_sv_pages() :
    yield taskgen.build_web_to_mkd(selenium_session, SV, 
            'autofile/semantic-versioning.md')


## others

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
