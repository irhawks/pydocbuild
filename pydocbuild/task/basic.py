__doc__ = """
能够生成task (yield a series of tasks) 的一些辅助函数

generator表示元任务生成器
basic.py生成基本任务
common.py生成常见任务
"""

from .basic import *
from pydocbuild.util.executor import Pandoc
from pydocbuild.util.loader import PyRequest

from functools import reduce



def lift_process_to_task(name, process, taskdep, **options) :
    """
    将一个过滤器之类的处理程序包装成一个任务
    该任务只依赖于前面的一个任务
    注意process是一个pandoc之类的对象，调用对象的execute方法
    """

    flowdep = options.get('flowdep', taskdep[0])
    def do_process(inflow) :

        r = {'result' : process.execute(inflow[flowdep])}
        return r


    return {
        'basename' : name,
        'name' : name,
        'actions' : [ do_process ],
        'task_dep': taskdep,
        'getargs' : {'inflow' : (flowdep, 'result')}
    }

def combine_result_list(name, taskdep) :

    """
    该函数用来组合之前的若干任务的输出，将它们的stdout联结起来。
    task关键字可以帮助我们获得任务的所有的参数的信息
    previous_result_key_list : 之前的结果被传递的key
    这里的result是新的结果。

    以后建议可以自定义相应的reducer
    """
    reducer_builder = lambda prev_result, sep, init : reduce (lambda x, y: x + sep + y, prev_result, init)
        ## reduce (lambda x, y : x + "\n" + y, previous_result_list, "")}

    def combine(**keywords) :

        prev_result_list = [keywords['result_'+t][t] for t in taskdep]

        return {'result' : reducer_builder(prev_result_list, "\n\n", "")}

    return {
        'basename' : name,
        'name' : name,
        'actions' : [ combine ],
        'task_dep': taskdep,
        'getargs' : {'result_' + taskname :
            (taskname, 'result')
                for taskname in taskdep}
    }


## -------------------------------------------------------------------

## 加载/获取、转换/过滤、生成/保存


def generate_converter(name, taskdep, **options) :

    """ 
        taskdep 是执行该程序之前应该执行的任务
        task_html_generator 表示的是能够生成html的任务，我们需要从这个任务中提取result
        taskname是生成的任务名
    """
    converter = options.get('converter', 
            Pandoc("-f", "html", "-t", "markdown", "--wrap=none"))
    flowdep = options.get('flowdep', taskdep[0])
    return lift_process_to_task(name, converter, taskdep, flowdep=flowdep)

def generate_filter(name, taskdep, **options) :
    
    return generate_converter(name, taskdep, **options)

def generate_saver(name, path, taskdep, **options) :

    flowdep=options.get('flowdep', taskdep[0])

    save = options.get('saver'
            , lambda path, content : open(path,'w').write(content))
    def do_save(path, content) :
        save(path, content[flowdep])

    return {
        'basename' : name,
        'name' : name,
        'actions' : [(do_save, [], {'path': path})],
        'task_dep': taskdep,
        'getargs' : {'content' : (flowdep, 'result'), },
        'targets' : [path]
    }

def generate_loader(name, uri, taskdep, **options) :

    """
    loader是负责根据URI获取URI的语义内容的程序，URI是其唯一参数
    """
    loader = options.get('loader', PyRequest(allow_redirects=True).load)
    def do_load(uri) :
        
        r = {'result': loader(uri)}
        return r

    return {
        'basename' : name,
        'name' : name,
        'actions' : [(do_load, [], {'uri' : uri})],
        'task_dep': taskdep
        }
