#!/usr/bin/env python3

from pydocbuild.util import *
from pydocbuild.pipe import *
import pydocbuild.task as task

## 注意在retrieve的时候使用什么样的会话来retrieve
## 缺省就使用selenium


## 1. 处理元数据
SemanticVersioningWebInfo = {
    'pattern' :  "http://semver.org/lang/%s",
    'themes' :["zh-CN", "en"],
    'filter': {'method' : 'id', 'pattern' : 'spec'}
}

SV = task.to_metadata(SemanticVersioningWebInfo)

from pydocbuild.util.browser import *
session = SeleniumContext(browser="phantomjs")

## 生成到markdown的转换任务
def task_retrieve_sv_pages() :
    yield task.custom_build_flow(SV
            , path='autofile/semantic-versioning.md'
            , loader=PhantomjsRequestUrl(session).load)


## ----------------------------------------------------------------------

if __name__ == '__main__':

    import doit
    doit.run(globals())
