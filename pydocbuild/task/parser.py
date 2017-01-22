
__doc__ = """
样例: 传给topic_metadata函数的内容
args = { 
    'pattern' :  "https://mirrors.tuna.tsinghua.edu.cn/help/%s",
    'themes' :["AOSP", "AUR","CocoaPods"
        , "anaconda","archlinux","archlinuxcn"
        ,"bananian","centos","chromiumos","cygwin"
        ,"docker","elpa","epel","fedora","git-repo"
        ,"gitlab-ce","gitlab-ci-multi-runner"
        ,"hackage","homebrew","homebrew-bottles"
        ,"linux-stable.git","linux.git","lxc-images"
        ,"mongodb","msys2","nodesource"
        ,"pybombs","pypi"
        ,"raspbian","repo-ck","repoforge","rpmfusion","rubygems"
        ,"tensorflow","termux","ubuntu","virtualbox","weave"],
    'filter': {'method' : 'id', 'pattern' : 'help-content'}
    }   
生成任务的顺序是，首先读入任务列表，如果是HTML类型的任务，那么就转换HTML。
也就是说，关键还是我们需要告诉任务，何时我们得到任务类型的信息。
比如任务类型是HTML->Markdown这样的类型。
如果是这样的类型，我们就应该为这样的类型准备分析表达式。
更具体地，这样的类型还会与具体网站相绑定。也就是说，一个任务类型并不能决定处理函数
一个类型只能起到构造任务的作用。

另外，也说明任务一般是聚集起来出现的。以Python字典的形式出现，也就是以

最好元数据可以直接从YAML文件当中读取，这样的话就不用每个文件再单独写出来了。
"""

import re

## taskfunc，任务名，savefunc，保存名。
## 任务名其实是依赖于网站的。比如维基，我们希望以后缀.md结尾。
## 这个时候，要求具有定制网站保存名的能力

def to_metadata (args) :

    """
    进一步整理mirror的元数据，从元数据当中添加构造类型数据
    """

    taskfunc = lambda theme: re.sub(r'[=]', r'_', args['pattern'] % theme)
    savefunc = lambda theme: re.sub(r'[=]', r'_', theme) + ".md"
    args['taskfunc'] = args.get('taskfunc', taskfunc)
    args['savefunc'] = args.get('savefunc', savefunc)
    args['savename'] = args['savename'] \
            if 'savename' in args.keys() else 'download/'+savefunc(themes[0])


    # 在mirror当中添加task_list属性，表示获取相应topic的任务名
    args['task_list'] = [args['taskfunc'](theme)
        for theme in args['themes']]
    return args


def to_separate_metadata_list(args) :
    """
    将数据变成是元数据的各个项目，每个项目作为单独的数据列表而出现。每次获取单独生成页面。
    """
    result = []
    taskfunc = lambda theme: re.sub(r'[=]', r'_', args['pattern'] % theme)
    savefunc = lambda theme: re.sub(r'[=]', r'_', theme) + '.md'
    args['taskfunc'] = args.get('taskfunc', taskfunc)
    args['savefunc'] = args.get('savefunc', savefunc)
    for theme in args['themes'] :
        result += [{'pattern' : args['pattern'],
            'filter' : args['filter'] if 'filter' in args.keys() else None,
            'themes' : [theme],
            'taskfunc' : args['taskfunc'],
            'savename' : savefunc(theme)
            }]
    return result
