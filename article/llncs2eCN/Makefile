# LaTeX Project Configuration with XeLaTeX and latexmk

# xelatex (complier)
TEXPROG = xelatex
TEXOPTS := -8bit -file-line-error -interaction=nonstopmode -shell-escape

# latexmk (pipeline processor)
PPLPROG = latexmk
# PPLCOPT := -use-make -deps
PPLOPTS += -g -e '$$latex=q/${TEXPROG} ${TEXOPTS} %O  %S/'
PPLOPTS += -e '$$pdflatex=q/${TEXPROG} ${TEXOPTS} %O %S/'

# source and target files
TEXFILE = lambda.tex
PDFFILE = $(patsubst %.tex,%.pdf,${TEXFILE})
ERRFILE = $(patsubst %.pdf,Make.err,${PDFFILE})

# Main Area
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
	-rm Make.err
	-rm *.pdf *.mx1 *.pyg *.run.xml
	-rm *.abc *.eps *.ps
	-rm -rf _minted-main

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


verbose : ${TEXFILE}
	if [ ! -e $(DEPS_DIR) ]; then mkdir $(DEPS_DIR); fi
	${PPLPROG} ${PPLOPTS} \
		${PPLCOPT} -deps-out=${DEPS_DIR}/${PDFFILE}.dep -pdf ${TEXFILE}
