
from functools import reduce

__doc__ = """
能够生成task (yield a series of tasks) 的一些辅助函数

generator表示元任务生成器
basic.py生成基本任务
common.py生成常见任务
"""


def lift_process_to_task(name, process, taskdep, **options) :
    """
    将一个过滤器之类的处理程序包装成一个任务
    该任务只依赖于前面的一个任务
    注意process是一个pandoc之类的对象，调用对象的execute方法
    """

    flowdep = options.get('flowdep', taskdep[0])
    def do_process(inflow) :
        return {'result' : process.execute(inflow[flowdep])}


    return {
        'basename' : name,
        'name' : name,
        'actions' : [ do_process ],
        'task_dep': taskdep,
        'getargs' : {'inflow' : (flowdep, 'result')}
    }

def combine_result_list(name, taskdep_list) :

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

        prev_result_list = [keywords['result_'+t][t] for t in taskdep_list]

        return {'result' : reducer_builder(prev_result_list, "\n", "")}

    return {
        'basename' : name,
        'name' : name,
        'actions' : [ combine ],
        'task_dep': taskdep_list,
        'getargs' : {'result_' + taskname :
            (taskname, 'result')
                for taskname in taskdep_list}
    }
