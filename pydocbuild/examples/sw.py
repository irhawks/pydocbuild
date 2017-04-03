#!/usr/bin/env python3


import os
import subprocess

from workflow import wrappers
from helpers.do_retrieve import *

## 注意在retrieve的时候使用什么样的会话来retrieve
## 缺省就使用selenium

global_selenium = wrappers.SeleniumWrapper('phantomjs')

## -------------------------------------------------------------------
SemanticVersioningWebInfo = {
    'url_pattern' :  "http://semver.org/lang/%s",
    'topic_list' :["zh-CN", "en"],
    'filter': {'method' : 'id', 'pattern' : 'spec'}
}
SV = to_metadata(SemanticVersioningWebInfo)

def task_retrieve_tsinghua_pages() :
    yield webpages_to_markdown(global_selenium, SV, 'autofile/semantic-versioning.md')

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
