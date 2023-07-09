#!/bin/bash
pdflatex -shell-escape Main.tex \
&& \
( for i in $(grep "^\\\include" Main.tex | sed -e 's/.*{\(.*\)}.*/\1/'); do bibtex $i; done; ) \
&& pdflatex -shell-escape Main.tex \
&& pdflatex -shell-escape Main.tex
