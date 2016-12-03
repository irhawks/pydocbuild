####---------------------------------------------------------------------
### 处理各种应用的程序
### TEX_PROG tex引擎
### PPL_PROG tex文件构建程序，可以为arana或者latexmk
### WTG WWV分别是WEB系统中的tangle和weave程序
TEX_PROG := xelatex
PPL_PROG := latexmk
WTG_PROG := notangle
WWV_PROG := noweave

####---------------------------------------------------------------------

### TEXs相关的选项
### TEX_OPTS传递给tex引擎 
TEX_OPTS := -file-line-error -interaction=nonstopmode -shell-escape -8bit
### PPL_OPTS传递给tex文件构建程序
PPL_OPTS := -g -e '$$latex =q/${TEX_PROG} ${TEX_OPTS} %O %S/'
PPL_OPTS += -e '$$pdflatex =q/${TEX_PROG} ${TEX_OPTS} %O %S/'
PPL_OPTS += -e '$$pdf_previewer =q/evince %O %S/'
### 使用中文索引
PPL_OPTS += -e '$$makeindex=q/zhmakeindex %O -z bihua -s mytkz.ist -o %D %S/'
### 使用biber的时候进行按照中文的排序
PPL_OPTS += -e '$$biber=q/biber -l zh__pinyin %O %S/'
PPL_OPTS += -pdf 
#PPL_OPTS += -use-make -deps
##PPL_OPTS += -e '$$hash_calc_ignore_pattern{'abc'} = '.*';
##$hash_calc_ignore_pattern{'eps'} = '.*';
### NOTANGLE和NOWEAVE相关的选项
WWV_OPTS := -delay
WWV_OPTS += -index 

WTG_OPTS := -t4

WEB_FILES := preamble.nw

MD_FILES := chapters/regulate.md
MD_FILES += chapters/packages.md
MD_FILES += chapters/elements.md
MD_FILES += chapters/citation.md
MD_FILES += chapters/articles.md
MD_FILES += chapters/appendix.md

WEB_PHONY := hnuthesis.nw

${WEB_PHONY} : ${WEB_FILES} ${MD_FILES}
	cat preamble.nw && pandoc -f latex -t latex --filter ./nwcode.hs ${MD_FILES} && echo "\n\\end{document}"


####---------------------------------------------------------------------

### 其中有一个主要的文档可以生成，这个主cls也是我们目前引用的
### 原则上只生成一个.tex与一个.pdf，可以生成多个cls，
### 但其余的都不是本文类本身使用的cls文档。
### WEB_PHONY实际上并不生成，只是作为一个字符串来推导相应的tex与pdf文件
SRC_FILES := $(patsubst %.nw,%.cls,${WEB_PHONY})
TEX_FILES := $(patsubst %.nw,%.tex,${WEB_PHONY})
PDF_FILES := $(patsubst %.nw,%.pdf,${WEB_PHONY})


####---------------------------------------------------------------------

.PHONY : default clean

### 在本文里，我们要生成hnu{detail,report,thesis}.{cls,tex,pdf}三个文档
default : ${SRC_FILES} ${PDF_FILES} ${TEX_FILES}

### 每个cls文件都是从WEB_FILES整体中析出
%.cls : ${WEB_FILES}
	${WTG_PROG} ${WTG_OPTS} -R$@ $^ >$@

%.tex : ${WEB_FILES}
	${WWV_PROG} ${WWV_OPTS} $^ >$@

%.pdf : %.tex %.cls
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
	-rm -f hnuthesis.cls hnuthesis*.tex  hnuthesis*.pdf 


.PHONY: verbose

verbose : hnuthesis.pdf
