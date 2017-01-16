
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

