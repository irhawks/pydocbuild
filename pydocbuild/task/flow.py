
from pydocbuild.util.executor import Pandoc
from pydocbuild.util.loader import PyRequest
from pydocbuild.util.htmltrans import InternalHtmlSelector

from pydocbuild.task.basic import *

def custom_build_flow(metadata, **kwargs) :

    custom_loader = kwargs.get('loader'
            , PyRequest(allow_redirects=True).load)
    custom_filter = kwargs.get('filter'
            , InternalHtmlSelector(**metadata['filter']))
    ## 注意filter因此必须重载execute方法，虽然是filter，标准方法还是executor
    custom_saver = kwargs.get('saver'
            , lambda path, content : open(path,'w').write(content))
    custom_converter = kwargs.get('converter'
            , Pandoc("-f", "html", "-t", "markdown", "--wrap=none"))

    # Every item should be retrieved separately
    for theme in metadata['themes'] :
        yield generate_loader(name="LOAD "+metadata['taskfunc'](theme)
                , uri=metadata['pattern'] % theme
                , taskdep=[]
                , loader=custom_loader)
    # Every item should be filtered separately
    for theme in metadata['themes'] :
        yield generate_filter(name="FILTER "+metadata['taskfunc'](theme)
                , taskdep=["LOAD "+metadata['taskfunc'](theme)]
                , converter=custom_filter
                )
        
    path = kwargs.get('path', 'autofile/default.md')
    themes = reduce (lambda x, y : x + "|" + y, metadata['themes'], "")
    ## 注意pattern和themes里面可能含有不能作为任务名的字符，比如等号。
    combinator_name = 'COMBINE ' + themes + " FOR " + metadata['savename']
    converter_name  = 'CONVERT ' + themes + " FOR " + metadata['savename']
    saver_name      = 'SAVE ' + path


    ## combine separate topic to a single stream
    filter_task_list = ["FILTER "+metadata['taskfunc'](theme) 
            for theme in metadata['themes']]
    yield combine_result_list(name = combinator_name
            , taskdep=filter_task_list)

    ## Convert single stream
    yield generate_converter(name=converter_name
            , taskdep=[combinator_name]
            , converter=custom_converter)

    ## save converted stream
    yield generate_saver(name=saver_name
            , path=path
            , taskdep=[converter_name]
            , saver=custom_saver)
