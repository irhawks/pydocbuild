######################################################################
## Project Hierachy Management ( pre-defined directories )
######################################################################

## Markdown extension (e.g. md, markdown, mdown).
MARKDOWN_EXT = md

## Location of Pandoc support files.
CONFIG_FILE = ~/.pandoc
CONFIG_PATH = .

## Resources files and addons
ADDONS_DIR := ./addons
TEMPLATE_DIR = ${ADDONS_DIR}/templates
FILTERS_DIR = ${ADDONS_DIR}/filters
CSL_DIR = ${ADDONS_DIR}/csl
BIB_DIR = ${ADDONS_DIR}/bib


######################################################################
## Pandoc (as a compiler) options

PANDOC_OPTS := -r markdown+simple_tables+table_captions+yaml_metadata_block
PANDOC_OPTS += --biblatex
PANDOC_OPTS += --filter ${FILTERS_DIR}/abc.py
PANDOC_OPTS += --filter ${FILTERS_DIR}/tikz.py
#PANDOC_OPTS += --filter ${FILTERS_DIR}/graphviz.py

## Note:
## --csl, --filter, --bibliography options should be put in metadata.yaml

## The following options should be put in metadata.yaml, but not yet 
## be implemented as a key:value
## options: --templates, --listings, --latex-engine

PANDOC_OPTS += --latex-engine=xelatex
#PANDOC_OPTS += --template=


########################################################################
## Source and target files specified
########################################################################

## Sources files should be put in the src/ directory,
## generated files like pdf, html should be put in the target/ directory.

SRC_FILES = $(wildcard src/articles/union.md)
SRC_BASENAME = $(patsubst src/articles/%.md,%.md,${SRC_FILES})
PDF_FILES = $(patsubst %.md,target/latex/%.pdf,${SRC_BASENAME})
HTML_FILES =$(patsubst %.md,target/html/%.html,${SRC_BASENAME})
TEX_FILES = $(patsubst %.md,target/latex/%.tex,${SRC_BASENAME})


#####################################################################
## Target Requirements
#####################################################################

.PHOHY : default all clean html

default : ${PDF_FILES}

all: ${PDF_FLIES} ${HTML_FILES} ${TEX_FILES}

html : ${HTML_FILES}

latex : ${TEX_FILES}

clean: clean-pdf clean-tex clean-html
clean-pdf:
	rm -rf ${PDF_FILES}
clean-tex:
	rm -rf ${TEX_FILES}
clean-html:
	rm -rf ${HTML_FILES}


#####################################################################
## Concret targets
#####################################################################

${HTML_FILES} : ${SRC_FILES}
	pandoc ${PANDOC_OPTS} -s -S -w html -o $@ $< metadata.yaml
	

${TEX_FILES} : ${SRC_FILES}
	pandoc ${PANDOC_OPTS} -s -S -w latex -o $@ $< metadata.yaml
