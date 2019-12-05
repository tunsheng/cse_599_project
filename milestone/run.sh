#latex main.tex
inputFile='milestone'
pdflatex ${inputFile}.tex
latex ${inputFile}.tex
bibtex ${inputFile}.aux
latex ${inputFile}.tex
pdflatex ${inputFile}.tex
rm -f *.aux *.log *.toc *.bbl *.blg *.out *.dvi *.xml ${inputFile}-blx.bib
