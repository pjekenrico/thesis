#!/bin/bash
for i in $(grep "^\\\include" Main.tex | sed -e 's/.*{\(.*\)}.*/\1/'); do bibtex $i; done;