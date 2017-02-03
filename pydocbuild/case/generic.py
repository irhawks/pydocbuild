__doc__ = "simple build flow for web pages"

import pydocbuild.task as task
from pydocbuild.util import loader
from pydocbuild.util import *
from pydocbuild.pipe.executor import ComposeExecutor

def simple_webpage_build (metadata, **kwargs) : 

    kwargs['path'] = kwargs.get('path', 'download/%s' % metadata['savename'])
    kwargs['loader'] = kwargs.get('loader', loader.PyRequest().load)
    yield task.custom_build_flow(metadata, **kwargs)


def simple_selenium_build (session, metadata, **kwargs) :

    converter=kwargs.get("converter", ComposeExecutor(
            Pandoc("-f", "html", "-t", "commonmark", "--wrap=none"),
            Pandoc("-f", "commonmark", "-t", "markdown", "--wrap=none"),
            StripFigures()))
    yield task.custom_build_flow(Task[t]
        , path='download/%s' % Task[t]['savename']
        , converter=converter
        , loader=loader.PhantomjsRequestUrl(session).load, **kwargs)

def webpage_strip_table_build(metadata, **kwargs) :

    converter=kwargs.get("converter", ComposeExecutor(
            StripHtmlTableTag(),
            StripHtmlTableTag(),
            Pandoc("-f", "html", "-t", "commonmark", "--wrap=none"),
            Pandoc("-f", "commonmark", "-t", "markdown", "--wrap=none"),
            StripFigures()))
    converter=ComposeExecutor(converter, AddTopString("# "+metadata['savename']+ '\n\n')) ## 保存文件名作为顶级元素（保证顶级元素的存在）
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
    yield task.custom_build_flow(metadata
        , path='download/%s' % metadata['savename']
        , converter=converter
        , loader=loader.PyRequest(headers=header).load)
