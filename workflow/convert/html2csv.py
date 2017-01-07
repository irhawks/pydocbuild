#!/usr/bin/env python
#Richard's html2csv converter
#rbarnes@umn.edu

from bs4 import BeautifulSoup
import sys
import csv
import argparse
import re


parser = argparse.ArgumentParser(description='Reads in an HTML and attempts to convert all tables into CSV files.')
parser.add_argument('--delimiter', '-d', action='store', default=',',help="Character with which to separate CSV columns")
parser.add_argument('--quotechar', '-q', action='store', default='"',help="Character within which to nest CSV text")
parser.add_argument('filename',nargs="?",help="HTML file from which to extract tables")
args = parser.parse_args()

#if sys.stdin.isatty() and not args.filename:
#  parser.print_help()
#  sys.exit(-1)
#elif not sys.stdin.isatty():
#  args.filename = sys.stdin
#else:
#  args.filename = open(sys.argv[1],'r')
args.filename=sys.stdin

print("Opening file")
fin  = args.filename.read()

print("Parsing file")
soup = BeautifulSoup(fin, "lxml")

print("Preemptively removing unnecessary tags")
[s.extract() for s in soup('script')]

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

print("CSVing file")
tablecount = -1
for table in soup.findAll("table"):
  tablecount += 1
  print("Processing Table #%d" % (tablecount))
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

open('new.html','w').write(str(soup))
