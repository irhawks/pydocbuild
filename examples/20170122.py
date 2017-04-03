#!/usr/bin/env python3

from pydocbuild.util import *
from pydocbuild.pipe import *
from pydocbuild import case
from pydocbuild import task

Task = dict()
Task['setup.py']=task.to_metadata({
    'pattern' :  "http://lingxiankong.github.io/blog/2013/12/23/%s",
    'themes' :["python-setup"],
    'filter': {
        'method' : 'xpath', 
        'pattern' : '//div[@id="content"]/div[@class="entry"]'
        },
    'savename' : 'python-setup-py.md'
    })

Task['wikitext'] = task.to_separate_metadata_list({
    'pattern' :  "https://en.wikipedia.org/w/index.php?title=%s&action=raw",
    'themes' :["Great_power", "List_of_ancient_great_powers"],
    ## 以后还可以去掉里面的等号与空格等敏感字符
    })


def task_do_wiki () :

    for k in Task['wikitext']:
        yield case.build_generic_wikitext(k)


## ----------------------------------------------------------------------

DOIT_CONFIG = { 
   #'default_tasks': ['t3']
   'backend': 'json',
   'reporter': task.MyReporter,
   'status' : True,
   'continue': True,
   'verbosity': 2
   }


if __name__ == '__main__':


    import doit
    doit.run(globals())
