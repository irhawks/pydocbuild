说明
=========================================

使用latex所写的小组周会记录加上每周报告的模板。

使用的时候添加TEXINPUS变量为"$YOURPATH:"，然后就可以直接使用csweekly.cls文件了。包括图形在内都可以使用。

为latex文件添加如下的git ignore，以下内容插自<https://github.com/LeZuse/gitignore/blob/master/LaTeX.gitignore>。

``` {.config}
*.aux
*.bbl
*.blg
*.dvi
*.glg
*.glo
*.gls
*.idx
*.ilg
*.ind
*.ist
*.lof
*.log
*.lot
*.nlo
*.out
*.toc
*.fdb_latexmk
*.pdfsync
*.synctex.gz
*.nav
*.snm
*.vrb
```


##  TEX CONFIGURATIONS

在.bashrc中添加如下的环境变量，就可以直接使用csweekly.cls了

```{.shell}
CSWEEKLY_CLS_DIR=~/git-repo/csweekly/appendix/group-template
NOTEBOOK_CLS_DIR= ~/note/extra/texclass
export TEXINPUTS="$CSWEEKLY_CLS_DIR:"
export TEXINPUTS="$NOTEBOOK_CLS_DIR:$TEXINPUTS"
```
