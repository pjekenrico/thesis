
ifeq ($(origin WS_TOP), undefined)
export WS_TOP := $(shell git rev-parse --show-toplevel)
endif

WS_MK =$(WS_TOP)/mk
WS_BIB=$(WS_TOP)/bib
WS_TEX=$(WS_TOP)/tex
WS_CLS=$(WS_TEX)/classes
WS_MCR=$(WS_TEX)/macros

ENV=env
RM =rm -f

BIBINPUTS=:$(WS_BIB)
TEX_ENV+= BIBINPUTS="$(BIBINPUTS)"

TEXINPUTS=:$(WS_CLS):$(WS_MCR)
TEX_ENV+= TEXINPUTS="$(TEXINPUTS)"

MAIN=main
MAINTEX=$(MAIN).tex

BIBTEX=bibtex
MAINBIB=$(MAINTEX:%.tex=%.bib)
BIBTEX_CMD=$(BIBTEX)

PDFLATEX=pdflatex
MAINPDF=$(MAINTEX:%.tex=%.pdf)
PDFTEX_CMD=$(PDFLATEX)

ifeq ($(BUILD_TYPE), teaching)
include $(WS_MK)/teaching.mk
endif

TEXSRC=$(wildcard *.tex)

$(MAINPDF): $(MAINTEX) $(TEXSRC)
	@$(ENV) $(TEX_ENV) $(PDFTEX_CMD) $<
	@if test -f $(MAINBIB); then $(ENV) $(TEX_ENV) $(BIBTEX_CMD) $(<:%.tex=%); fi;
	@$(ENV) $(TEX_ENV) $(PDFTEX_CMD) $<
	@$(ENV) $(TEX_ENV) $(BIBTEX_CMD) $(MAIN) 
	@$(ENV) $(TEX_ENV) $(PDFTEX_CMD) $<

all: $(MAINPDF) $(TEXSRC)

CLEAN_PATHS = $(MAINPDF)
CLEAN_PATHS+= $(MAINTEX:%.tex=%.aux)
CLEAN_PATHS+= $(MAINTEX:%.tex=%.bbl)
CLEAN_PATHS+= $(MAINTEX:%.tex=%.blg)
CLEAN_PATHS+= $(MAINTEX:%.tex=%.idx)
CLEAN_PATHS+= $(MAINTEX:%.tex=%.log)
CLEAN_PATHS+= $(MAINTEX:%.tex=%.nlo)
CLEAN_PATHS+= $(MAINTEX:%.tex=%.toc)

clean:
	@$(RM) $(CLEAN_PATHS)
