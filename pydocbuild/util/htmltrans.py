from pydocbuild.util.executor import *

__doc__ = """
使用HtmlParser来解析Html文档当中的内容，按照标准输出与标准输出的方式
"""

class HtmlFilter :
    """
    内部函数，使用的是BeautifulSoup，
    它们的任务是，接受一个Html文档，返回经过修整之后的Html文档
    在Html的级别进行工作
    """
    def __init__(self) :
        pass


from bs4 import BeautifulSoup
import sys
import csv
import argparse
import re

class WritableObject:
    def __init__(self):
        self.content = ""
    def write(self, string):
        self.content += string

class HtmlTableToCsvCode (HtmlFilter) :

    """
    基于BeautifulSoup的Parser
    Richard's html2csv converter <rbarnes@umn.edu>
    初始化函数传递参数，以字典的形式，比如delimiter属性
    属性来自于csv模块。
    """

    def __init__(self, **args) :
        self._args = args

    def build_table_datamodel(table) :
    
        def build_field_datamodel(field) :
            r = field["rowspan"] if field.has_attr("rowspan") else 1
            c = field["colspan"] if field.has_attr("colspan") else 1
            return [field.text, r,c]
        def build_row_datamodel(row) :
            cols = row.findAll(['td','th'])
            return [build_field_datamodel(col) for col in cols]
        return [build_row_datamodel(row) for row in table.findAll('tr')]

    ## 分析每行每列是否是一致的
    def analyze_table_datamodel(model) :
    
        def analyze_row(row) :
            return sum([field[2] for field in row])
        return [analyze_row(row) for row in model]
    
    def expand_table_datamodel(model) :
        def expand_row_datamodel():
            pass

    def execute(self, content) :
        return self.filter(content)

    def filter(self, content) :

        #print("Parsing file")
        soup = BeautifulSoup(content, "lxml")
        
        #print("Preemptively removing unnecessary tags")
        [s.extract() for s in soup('script')]
        
        #print("CSVing file")
        tablecount = -1
        for table in soup.findAll("table"):
            tablecount += 1
            #print("Processing Table #%d" % (tablecount))
            csvtable = WritableObject()
            #with open(sys.argv[1]+str(tablecount)+'.csv', 'w') as csvfile:
            #with sys.stdout as csvfile:
            if 1 :
              fout = csv.writer(csvtable, quoting=csv.QUOTE_MINIMAL, **self._args)
        
              #model = build_table_datamodel(table)
              #print(analyze_table_datamodel(model))
        
              for row in table.findAll('tr'):
                cols = row.findAll(['td','th'])
                if cols:
                  for col in cols :
                      r = col['rowspan'] if col.has_attr("rowspan") else 1
                      c = col['colspan'] if col.has_attr("colspan") else 1
                  cols = ["|%d-%d|%s" % (int(r),int(c),re.sub('[\n\r\xa0]','',x.text)) for x in cols]
                  fout.writerow(cols)
            #print(csvtable.content)
            inner = soup.new_tag("code")
            inner.string = re.sub('[\r\f]','', csvtable.content)
            surrounding = soup.new_tag("pre")
            surrounding["class"]='csv'
            surrounding.append(inner)
            table.replace_with(surrounding)
        
        return str(soup)

from lxml import etree
from lxml.html.clean import Cleaner

class LxmlHtmlCleaner (InternalExecutor) :

    def __init__(self, **args) :
        if args : 
            self._cleaner = Cleaner(**args)
        else :
            self._cleaner = Cleaner(style=True, 
                    scripts=True,page_structure=False, 
                    safe_attrs_only=False)

    def clean_from(self, html) :
        return self._cleaner.clean_html(html)


from bs4 import BeautifulSoup as bs

class InternalHtmlSelector(InternalExecutor) :
    def __init__(self, method, pattern) :
        self._pattern = pattern
        self._method = method
    
    def select_from(self, html) :
        """
        只可以选择其中的一个元素。如果分析不成功，应该给出一个警告才对
        """
        try :
            if (self._method == 'id')    :   
                root = bs(html, "lxml")
                return str( root.find(attrs={'id': self._pattern}) )
            if (self._method == 'class') : 
                root = bs(html, "lxml")
                return str( root.find(attrs={'class': self._pattern}) )
            if (self._method == 'css')   :   
                root = bs(html, "lxml")
                return str( root.select(self._pattern)[0] )
            if (self._method == 'xpath')   :   
                root = etree.HTML(html.encode('utf-8'), parser=etree.HTMLParser(encoding='utf-8'))
                ## 注意保持所使用的编码的一致
                ## http://www.cnblogs.com/xieqiankun/p/lxmlencoding.html
                #print(self._pattern)
                #print(etree.tounicode(root))
                #print(etree.tounicode(root.xpath(self._pattern)[0]))
                return etree.tounicode(root.xpath(self._pattern)[0])
            return ""
        except :
            return ""

    def execute(self, html) :
        return self.select_from(html)

class  StripHtmlEntities(Sed) :
    
    def __init__(self) :
        super().__init__("-e", "s/&nbsp;/,/g")


def innerHTMLLxmlVersion(node):
    return ''.join([etree.tostring(child).decode() for child in node])

def innerHTMLbs4Version(node) :
    return "".join([str(x) for x in node.contents]) 

class StripHtmlTableTag(HtmlFilter): 

    def __init__(self, **args) :
        self._args = args

    def filter(self, content) :
        return self.execute(content)

    def execute(self, content) : 
        soup = BeautifulSoup(content, "lxml")
        while soup.findAll("table") :
            for table in soup.findAll("table"):
                if not table.findAll("table"):
                    target = "".join([str(x) for x in table.contents]) 
                    table.replace_with(BeautifulSoup(target, "lxml"))
        return soup.prettify()

class StripHtmlTableTagWithRe(HtmlFilter): 

    def __init__(self, **args) :
        self._args = args

    def filter(self, content) :
        return self.execute(content)

    def execute(self, content) : 
        v=re.sub(r'<table[^<]*>', '', content)
        return re.sub(r'</table>', '', v)

## 将tr/td标记变成ul/li标记，每个li代表一个标签项，一个li变成一个tr吧
class HtmlTrTdTagToUlLi(HtmlFilter): 

    def __init__(self, **args) :
        self._args = args

    def filter(self, content) :
        return self.execute(content)

    def execute(self, content) : 
        v=re.sub(r'<table[^<]*>', '<ul>', content)
        w=re.sub(r'</table>', '</ul>', v)
        x=re.sub(r'<tr', '<li', w)
        y=re.sub(r'</tr>', '</li>', x)
        return y
## 将HTML当中的svg图片以code的形式保存一来
class SvgTagToCodeTag(HtmlFilter): 

    def __init__(self, **args) :
        self._args = args

    def filter(self, content) :
        return self.execute(content)

    def execute(self, content) : 
        x=re.sub(r'<svg ', '<pre><code ', content)
        y=re.sub(r'</svg>', '</code></pre>', x)
        return y
