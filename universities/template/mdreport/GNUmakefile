# 处理各种应用的程序
# TEX_PROG tex引擎
# PPL_PROG tex文件构建程序，可以为arana或者latexmk
# WTG WWV分别是WEB系统中的tangle和weave程序

TEX_PROG := xelatex
PPL_PROG := latexmk
WTG_PROG := notangle
WWV_PROG := noweave

# TEXs相关的选项
# TEX_OPTS传递给tex引擎 

TEX_OPTS := -file-line-error -interaction=nonstopmode -shell-escape -8bit

# PPL_OPTS传递给tex文件构建程序

PPL_OPTS := -g -e '$$latex =q/${TEX_PROG} ${TEX_OPTS} %O %S/'
PPL_OPTS += -e '$$pdflatex =q/${TEX_PROG} ${TEX_OPTS} %O %S/'
PPL_OPTS += -e '$$pdf_previewer =q/evince %O %S/'

# 使用中文索引

PPL_OPTS += -e '$$makeindex=q/zhmakeindex %O -z bihua -s mytkz.ist -o %D %S/'

# 使用biber的时候进行按照中文的排序

PPL_OPTS += -e '$$biber=q/biber -l zh__pinyin %O %S/'
PPL_OPTS += -pdf 
#PPL_OPTS += -use-make -deps
#PPL_OPTS += -e '$$hash_calc_ignore_pattern{'abc'} = '.*';
#$hash_calc_ignore_pattern{'eps'} = '.*';

# NOTANGLE和NOWEAVE相关的选项

WWV_OPTS := -delay
WWV_OPTS += -index 

WTG_OPTS := -t4


## PANDOC的选项


PANDOC_FILTER_PATH=~/.cabal/bin
PANDOC=pandoc
PANDOC_OPTS= --biblatex -t latex --top-level-division=section --filter ./nwcode.hs
PANDOC_OPTS_R= --biblatex -t latex --top-level-division=section --filter ./nwminted.hs



####-----------------------------------------------------------------
####-----------------------------------------------------------------

### 我们相得到的是对于各个文类介绍的PDF与其cls文档，其中cls才是最重要的。
### 无论如何，分散的.nw文件就是那么从，而我们欲生成的是若干个cls。
### 从这些.nw文件中具有生成多个.cls的能力。
### 第六章是我们的附件。原则上写一本手册的话，章节数不应该太多。
## 主文件与第一章的材料、主控文件的格式

### 新的编译过程是，首先从各个markdown的文件当中得到主.nw文件。命名为omniwork.nw
### omniwork.nw由各个markdown文件和main.tex以及preamble.tex产生。
### markdown生成的.nw文件放在prologue.nw和epilogue.nw中间。

MD_FILES := chapters/usage.md
MD_FILES += chapters/regulate.md
MD_FILES += chapters/packages.md
MD_FILES += chapters/elements.md
MD_FILES += chapters/citation.md
MD_FILES += chapters/appendix.md


# 基本思想就是首先产生一个大而全的omniwork.nw，
# 然后再由这个文件生成各种需要的插件形式。


NWDOCS := hnureport.nw
TEX_MAIN=$(patsubst %.nw,%.tex,${NWDOCS})
PDF_MAIN=$(patsubst %.nw,%.pdf,${NWDOCS})
CLS_MAIN=$(patsubst %.nw,%.cls,${NWDOCS})

${NWDOCS} : prologue.tex ${MD_FILES} epilogue.tex
	cat prologue.tex > $@
	PATH=$$PATH:${PANDOC_FILTER_PATH} ${PANDOC} ${PANDOC_OPTS} ${MD_FILES} >> $@
	cat epilogue.tex >> $@

default : ${PDF_MAIN}

.PHONY : default clean all

### 改成使用nwreserve.hs来产生相应的.tex文件。

${TEX_MAIN} : prologue.tex ${MD_FILES} epilogue.tex
	cat prologue.tex > $@
	PATH=$$PATH:${PANDOC_FILTER_PATH} ${PANDOC} ${PANDOC_OPTS_R} ${MD_FILES} >> $@
	cat epilogue.tex >> $@

# {WWV_PROG} ${WWV_OPTS} $< > $@

${CLS_MAIN} : ${NWDOCS}
	${WTG_PROG} ${WTG_OPTS} -R$@ $^ >$@


${PDF_MAIN} : ${TEX_MAIN} ${CLS_MAIN}
	${PPL_PROG} ${PPL_OPTS} $(patsubst %.pdf,%.tex,$<)

####-----------------------------------------------------------------


clean :
	-latexmk -CA
	-rm -f *.log *.toc *.scn *.idx 
	-rm ${TEX_FILES} ${SRC_FILES} ${PDF_FILES}
	-rm *.ilg *.ind *.aux *.mw *.xwm *.run.xml *.bbl *.listing
	-rm -rf _minted-* *.mintedcmd *.mintedmd5 *.pyg
	-rm *.fls *.out *.bcf *.blg
	-rm -f *.fdb_latexmk
	-rm -rf hnureport.*

realtime: omniwork.tex
	${PPL_PROG} ${PPL_OPTS} -pvc $<
