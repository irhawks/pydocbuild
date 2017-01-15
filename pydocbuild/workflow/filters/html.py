#!/usr/bin/env python3

__doc__ = """
使用HtmlParser来解析Html文档当中的内容，按照标准输出与标准输出的方式
"""

from .basic import Filter


class HtmlFilter(Filter) :
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

class HtmlTableConvertToCsvCode (HtmlFilter) :

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
    
    class WritableObject:
        def __init__(self):
            self.content = ""
        def write(self, string):
            self.content += string

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
              fout = csv.writer(csvtable, delimiter=args.delimiter, quotechar=args.quotechar, quoting=csv.QUOTE_MINIMAL)
        
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
