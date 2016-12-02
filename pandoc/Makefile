### 第一阶段是从Markdown文件准备生成必要的LaTeX文件，
### 主要是main.md向main.tex的转变

PANDOC=pandoc

### old version --chapters
PANDOC_OPTS= --biblatex -t latex --top-level-division=chapter

MARKDOWN_FILES:=$(wildcard markdown/*.md)

GENERATE_TEX_FILES=$(patsubst %.md,%.tex,${MARKDOWN_FILES})


%.tex : %.md
	${PANDOC} ${PANDOC_OPTS} $< > $@


### 生成LaTeX文件之后，就应该是编译主文件了，这个时候使用通用Makefile

# xelatex (complier)
TEXPROG = xelatex
TEXOPTS := -8bit -file-line-error -interaction=nonstopmode -shell-escape

# latexmk (pipeline processor)
PPLPROG = latexmk

# PPLCOPT := -use-make -deps
PPLOPTS += -g -e '$$latex=q/${TEXPROG} ${TEXOPTS} %O %S/'
PPLOPTS += -e '$$pdflatex=q/${TEXPROG} ${TEXOPTS} %O %S/'

# source and target files
TEXFILE = main.tex
PDFFILE = $(patsubst %.tex,%.pdf,${TEXFILE})
ERRFILE = $(patsubst %.pdf,Make.err,${PDFFILE})

.PHONY : default clean view realtime debug verbose
default : ${PDFFILE}

##编译正文文档
DEPS_DIR = .deps
$(foreach file,$(PDFFILE),$(eval -include $(DEPS_DIR)/$(file).dep))
${PDFFILE} ${ERRFILE} : ${TEXFILE}
	if [ ! -e $(DEPS_DIR) ]; then mkdir $(DEPS_DIR); fi
	${PPLPROG} ${PPLOPTS} \
		${PPLCOPT} -deps-out=${DEPS_DIR}/${PDFFILE}.dep -pdf $<\
		2>&1 | ./Make.sh 1>Make.err

##清理相关文件夹
clean :
	${PPLPROG} -c
	-rm *.vrb *.snm *.nav *.bbl
	-rm -rf .deps
	-rm Make.err  *.listing
	-rm *.asy *.pre
	-rm *.pdf *.mx1 *.pyg *.run.xml
	-rm *.abc *.eps *.ps *.pre
	-rm -rf _minted-main
	-rm -rf ${GENERATE_TEX_FILES}
	-rm -rf out-plant*

realtime : ${TEXFILE} ${PDFFILE}
	if [ ! -e $(DEPS_DIR) ]; then mkdir $(DEPS_DIR); fi
	evince ${PDFFILE} &
	${PPLPROG} ${PPLOPTS} -pvc \
		${PPLCOPT} -deps-out=${DEPS_DIR}/${PDFFILE}.dep -pdf $< \
		2>&1 | ./Make.sh 1>Make.err

debug : 
	vim -q ${ERRFILE}

view : ${PDFFILE}
	-evince $< &


verbose : ${TEXFILE} ${GENERATE_TEX_FILES}
	if [ ! -e $(DEPS_DIR) ]; then mkdir $(DEPS_DIR); fi
	${PPLPROG} ${PPLOPTS} \
		${PPLCOPT} -deps-out=${DEPS_DIR}/${PDFFILE}.dep -pdf ${TEXFILE}
