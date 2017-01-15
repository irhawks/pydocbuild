#!/usr/bin/env python3

class BaiduBaikeHtmlWrapper(Composite) :
    
    def __init__(self) :
        super().__init__(
            PandocWrapper("-f", "html", "-t", "commonmark", "--wrap=none"),
            PandocWrapper("-f", "commonmark", "-t", "markdown", "--wrap=none"),
            SedWrapper("-e", r's/\\\*\\\*//g', 
                "-e", r's/^　\+/\n/', 
                "-e", r's/\\$//',
                "-e", r's/^\[编辑\].*//',
                "-e", r's/<sup>\\\[\([0-9]\+\)\\\]<\/sup>/ [^\1]/g',
                "-e", r's/\s\+-\s\+\([0-9]\+\)\\\.[^)]\+)\s\+/[^\1]: /',
                "-e", r's/!\[/[图片：/g'))

def testBaiduBaikeHtmlFilter() :
    wrapper = BaiduBaikeHtmlFilter()
    out = wrapper.execute(open('../testdata/baidubaike-hainan-university.html').read())
    print(out)

if __name__ == '__main__' :
    testBaiduBaikeHtmlWrapper()

