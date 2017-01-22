__doc__ = "simple build flow for web pages"

import pydocbuild.task as task
from pydocbuild.util import loader

def simple_webpage_build (metadata, **kwargs) : 

    yield task.custom_build_flow(metadata
        , path='download/%s' % metadata['savename']
        , loader=loader.PyRequest().load, **kwargs)


def simple_selenium_build (session, metadata, **kwargs) :

    converter=kwargs.get("converter", ComposeExecutor(
            Pandoc("-f", "html", "-t", "commonmark", "--wrap=none"),
            Pandoc("-f", "commonmark", "-t", "markdown", "--wrap=none"),
            StripFigures()))
    yield task.custom_build_flow(Task[t]
        , path='download/%s' % Task[t]['savename']
        , converter=converter
        , loader=loader.PhantomjsRequestUrl(session).load, **kwargs)
