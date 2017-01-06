
## 每个执行器的结果，统一使用result来传递

from workflow.retrievers import *
from workflow.wrappers import *

## session指的是打开的selenium会话，这个会话需要用户自己管理。

def do_selenium_retrieve (session, url_pattern, topic, pattern, method) :

    ## 首先使用Selenium获取，然后再Filter
    e1 = session.execute(url_pattern % topic)
    e2 = ElementRetriever(pattern, method).filter(e1)
    e3 = ElementContentRetriever().retrieve(e2)
    return {'result' : e3}

def yield_retrieve_page_list(selenium_session, record) :

    for topic in record['topic_list'] :

        filename = 'task_page_%s' % topic
        yield {'basename' : record['taskname_func'](topic),
            'name' : record['taskname_func'](topic),
            'actions' : [(do_selenium_retrieve, [], {
                'session' : selenium_session,
                'url_pattern' : record['url_pattern'],
                'topic' : topic, 
                'pattern' : record['filter']['pattern'],
                'method'  : record['filter']['method']
                }
            )],
        }

## -------------------------------------------------------------------
# 样例: 传给topic_metadata函数的内容
# args = { 
#     'url_pattern' :  "https://mirrors.tuna.tsinghua.edu.cn/help/%s",
#     'topic_list' :["AOSP", "AUR","CocoaPods"
#         , "anaconda","archlinux","archlinuxcn"
#         ,"bananian","centos","chromiumos","cygwin"
#         ,"docker","elpa","epel","fedora","git-repo"
#         ,"gitlab-ce","gitlab-ci-multi-runner"
#         ,"hackage","homebrew","homebrew-bottles"
#         ,"linux-stable.git","linux.git","lxc-images"
#         ,"mongodb","msys2","nodesource"
#         ,"pybombs","pypi"
#         ,"raspbian","repo-ck","repoforge","rpmfusion","rubygems"
#         ,"tensorflow","termux","ubuntu","virtualbox","weave"],
#     'filter': {'method' : 'id', 'pattern' : 'help-content'}
#     }   

## 进一步整理mirror的元数据，从元数据当中添加构造类型数据
def to_metadata (args) :

        taskname_func = lambda topic : 'task_' + args['url_pattern'] % topic
        args['taskname_func'] = taskname_func

        # 在mirror当中添加task_list属性，表示获取相应topic的任务名
        args['task_list'] = [args['taskname_func'](topic)
        for topic in args['topic_list']]
        return args

## 能够生成task (yield a series of tasks) 的一些辅助函数

## 该函数用来组合之前的若干任务的输出，将它们的stdout联结起来。

def combine_previous_task_results_as(taskname_list, new_task_name) :

    ## task关键字可以帮助我们获得任务的所有的参数的信息
    ## previous_result_key_list : 之前的结果被传递的key
    ## 这里的result是新的结果。

    def combine(**keywords) :

        previous_result_list = [keywords['result_'+t][t] for t in taskname_list]

        from functools import reduce
        return {'result' : reduce (lambda x, y : x + "\n" + y, previous_result_list, "")}

    return {
        'basename' : new_task_name,
        'name' : new_task_name,
        'actions' : [ combine ],
        'task_dep': taskname_list,
        'getargs' : {'result_' + taskname :
            (taskname, 'result')
                for taskname in taskname_list}
    }


## 使用缺省的pandoc转换器把HTML文件转换成markdown文件

def builder_for_html_to_markdown(task_dep_list, task_html_generator, taskname) :

    """ 
        task_dep_list 是执行该程序之前应该执行的任务
        task_html_generator 表示的是能够生成html的任务，我们需要从这个任务中提取result
        taskname是生成的任务名
    """

    def pandoc_convert(stdin) :

        return {'result' : DefaultPandocWrapper().execute(stdin[task_html_generator])}

    return {
        'basename' : taskname,
        'name' : taskname,
        'actions' : [pandoc_convert],
        'task_dep': task_dep_list,
        'getargs' : {'stdin' : (task_html_generator, 'result')}
    }


def builder_for_save_a_file(taskname, path, previous_task, task_dep_list) :

    def save(path, **keywords) :
        open(path,'w').write(keywords['markdown'][previous_task])

    return {
        'basename' : taskname,
        'name' : taskname,
        'actions' : [save],
        'task_dep': task_dep_list,
        'getargs' : {'markdown' : (previous_task, 'result'), },
        'targets' : [path]
    }

## 缺省task_dep_list就是previous_task

def builder_for_save_a_file(taskname, path, previous_task) :

    def save(path, **keywords) :
        open(path,'w').write(keywords['markdown'][previous_task])

    return {
        'basename' : taskname,
        'name' : taskname,
        'actions' : [(save, [], {'path' : path})],
        'task_dep': [previous_task],
        'getargs' : {'markdown' : (previous_task, 'result'), },
        'targets' : [path]
    }

## 结果都保存在results里面，应该是没有错误了。
