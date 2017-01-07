
## 每个执行器的结果，统一使用result来传递

from workflow.retrievers import *
from workflow.wrappers import *

from functools import reduce

## session指的是打开的selenium会话，这个会话需要用户自己管理。


def yield_retrieve_page_list(selenium_session, record) :

    def do_selenium_retrieve (session, url_pattern, topic, pattern, method) :
    
        ## 首先使用Selenium获取，然后再Filter
        e1 = session.execute(url_pattern % topic)
        e2 = ElementRetriever(pattern, method).filter(e1)
        e3 = ElementContentRetriever().retrieve(e2)
        return {'result' : e3}

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

## 将数据变成是元数据的各个项目，每个项目作为单独的数据列表而出现。每次获取单独生成页面。

def to_separate_metadata_list(args) :

        result = []
        taskname_func = lambda topic : 'task_' + args['url_pattern'] % topic
        args['taskname_func'] = taskname_func
        #print(args)
        for topic in args['topic_list'] :
            result += [{'url_pattern' : args['url_pattern'],
                'filter' : args['filter'], 
                'topic_list' : [topic],
                'task_list' : [args['taskname_func'](topic)],
                'taskname_func' : args['taskname_func']}]
        #print("结果")
        #print(result)
        return result       

## 能够生成task (yield a series of tasks) 的一些辅助函数

## 该函数用来组合之前的若干任务的输出，将它们的stdout联结起来。

def combine_previous_task_results_as(taskname_list, new_task_name) :

    ## task关键字可以帮助我们获得任务的所有的参数的信息
    ## previous_result_key_list : 之前的结果被传递的key
    ## 这里的result是新的结果。

    def combine(**keywords) :

        previous_result_list = [keywords['result_'+t][t] for t in taskname_list]

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

    def pandoc_convert(content) :

        return {'result' : StanfordHtmlFilter().execute(content[task_html_generator])}

    return {
        'basename' : taskname,
        'name' : taskname,
        'actions' : [pandoc_convert],
        'task_dep': task_dep_list,
        'getargs' : {'content' : (task_html_generator, 'result')}
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

## 缺省task_dep_list就是previous_task，这类任务不再返回result，而是产生文件之类的。

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

## 将整个流程都进行转换

def webpages_to_markdown (selenium_session, record, savename) :

    all_topic = reduce (lambda x, y : x + "," + y, record['topic_list'], "")
    generator_taskname = '生成HTML:' + record['url_pattern'] + all_topic
    converter_taskname = '转换HTML到markdown:' + record['url_pattern'] + all_topic
    saver_taskname = '保存markdown:' + savename + record['url_pattern'] + all_topic
    yield yield_retrieve_page_list(selenium_session, record) 
    yield combine_previous_task_results_as(record['task_list'], generator_taskname)
    yield builder_for_html_to_markdown([generator_taskname], generator_taskname, converter_taskname)
    yield builder_for_save_a_file(taskname= saver_taskname, 
            path=savename,
            previous_task=converter_taskname)



__doc__ = """

如果抽象起来，应该抽象一个名为TaskGenenerator的类别。
它们完成的任务是TaskGeneration，也就是任务生成。完成任务的过程称为Generate。

基本的task任务是获取任务，也就是从任务元数据描述中生成基本任务，比如根据列表生成任务

然后是一些composite任务与转换器生成器的任务。生成一些转换格式的任务。

或者一些Filter任务的生成，用于对于一些细节内容进行过滤。

即使纯粹从抽象的角度考虑，面向对象/类型也是不错的。它给了我们一种体系化结构的方法。

TaskGenerator = ShellTaskGenerator 
    | CompositeTaskGenerator
    | FilterTaskGenerator
    | SaverTaskGenerator
于是关键的内容，就是如何找到TaskGenerator的类型。自然而然地，需要有任务类型。

常见的任务类型有哪些呢？还是需要查表。这个时候是需要有一些经验知识的。

## 我们需要了解任务之间关联的方式，并讨论这些关联的方式所遵守的规律。

比如，最基本的是通过类似于管道的机制，一个任务传递另外一个任务结果，这个时候标准的做法应该是通过result关键字。

其次的过程，比如一些读取文件或者保存文件的东西，它们需要从文件当中读取内容，
并不是接着上一个任务的输出。它们在这里扮演着任务系统的输入输出的作用。
比如读入文件，读出文件的任务，ReaderTask, WriterTask。
* ReaderTask需要把所读取的文件写到file_dep变量当中。
* WriterTask需要把自己所生成的文件写到targets变量当中。
这可以称为这两类变量的特征，它们的动作与它们的元数据的关联关系。

这样的话，才方便任务的继续依赖的执行。（形成计算图的结构）

"""

