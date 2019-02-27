ch38test.pdf: ch38test.tex data.bib
	pdflatex ch38test.tex
	bibtex ch38test.aux
	pdflatex ch38test.tex
	pdflatex ch38test.tex

clean:
	rm -f *.aux *.log

clean_pdf:
	rm -f *.pdf
