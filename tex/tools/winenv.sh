#!/bin/bash
MKTEXROOT="/c/Program\ Files/MiKTeX\ 2.9/miktex/"
export MKTEXROOT
export PATH=${MKTEXROOT}/bin/x64:$PWD/tex/bin:$PATH
alias bibtex="${MKTEXROOT}/bin/x64/bibtex.exe"
alias latex="${MKTEXROOT}/bin/x64/latex.exe"
alias pdflatex="${MKTEXROOT}/bin/x64/pdflatex.exe"
export BIBINPUTS=$PWD/bib
export TEXINPUTS=$PWD/tex/classes:$PWD/tex/macros
