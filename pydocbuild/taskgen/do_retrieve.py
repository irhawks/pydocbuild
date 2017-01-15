
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

