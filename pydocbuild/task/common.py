from .basic import *

from functools import reduce

from pydocbuild.util.executor import Pandoc
from pydocbuild.util.browser.selector import SeleniumSelector

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

## 使用缺省的pandoc转换器把HTML文件转换成markdown文件

def html_to_markdown(name, taskdep, **options) :

    """ 
        task_dep_list 是执行该程序之前应该执行的任务
        task_html_generator 表示的是能够生成html的任务，我们需要从这个任务中提取result
        taskname是生成的任务名
    """
    return generate_converter(name, taskdep, **options)



def build_page_list(session, record) :

    for topic in record['topic_list'] :

        filename = 'task_page_%s' % topic
        yield {'basename' : record['taskname_func'](topic),
            'name' : record['taskname_func'](topic),
            'actions' : [(selenium_get_a_page, [], {
                'session' : session,
                'url_pattern' : record['url_pattern'],
                'topic' : topic, 
                'pattern' : record['filter']['pattern'],
                'method'  : record['filter']['method']
                }
            )],
        }

def build_web_to_mkd (session, record, savename) :

    """
    将整个流程都进行转换
    """

    all_topic = reduce (lambda x, y : x + "," + y, record['topic_list'], "")
    generator_name = 'HTML:' + record['url_pattern'] + all_topic
    converter_name = 'HTML->mkd:' + record['url_pattern'] + all_topic
    saver_name = 'Save mkd:' + savename + record['url_pattern'] + all_topic

    yield build_page_list(session, record) 
    yield combine_result_list(generator_name, record['task_list'])
    yield html_to_markdown(converter_name, [generator_name])
    yield save_a_file(saver_name, savename, [converter_name])

## get through selenium

def get_a_page_with_selenium (session, uri, theme, pattern, method) :
    
        """
        首先使用Selenium获取，然后再Filter。
        应该生成一个任务类型。
        uri + theme + pattern + method可以唯一地决定输入
        """
        e1 = session.get_element(uri % theme)
        e2 = SeleniumSelector(pattern, method).select_content_from(e1)
        return {'result' : e2}

def get_a_page_with_requests (uri, theme, pattern, method) :

    PyRequest().execute(uri)
